/*
Testing program that moves the steering to position to one defined point that is hardcoded.  This is just to test the system.
The process is to move the wheels and therefore the angle sensor value outside of the target position and confirm the system brings
the wheels to the target angle.  I tested first with power not connectect to the motor and watched the LED lights that light
when left and right signals are being sent.  Also keep the steer_effort low in case something goes bad.

Al's lawn tractor
hard right = 1683
hard left = 380
in practice 1233 appears to be straight

Not finished
- Nalculate how many readings the filter routine is taking out - decide if further analysis is needed
- Confirm the left, right and straight settings are not moving after multiple starts

*/
#include "ros.h"
#include <Wire.h>

int AS5600_ADR = 0x36;  // the address of the board on the SDA bus, printed on the circut board
const int raw_ang_hi = 0x0c;
const int raw_ang_lo = 0x0d;

float steering_angle_target = 1233; // straight ahead
float steer_angle_val = 0;
float steer_err_value = 0;
int steer_effort = 30;
int DIRPin = 14; 
int PWMPin = 20;
char buffer[50];

ros::NodeHandle nh;

float returnRawAngle()
{
  // Read Raw Angle Low Byte
  Wire.beginTransmission(AS5600_ADR);  // the address of the board on the SDA bus, printed on the circut board
  Wire.write(raw_ang_lo);
  Wire.endTransmission();
  Wire.requestFrom(AS5600_ADR, 1);
  int lo_raw = Wire.read();

  // Read Raw Angle High Byte
  Wire.beginTransmission(AS5600_ADR);
  Wire.write(raw_ang_hi);
  Wire.endTransmission();
  Wire.requestFrom(AS5600_ADR, 1);
  word hi_raw = Wire.read();
  hi_raw = hi_raw << 8; //shift raw angle hi 8 left
  hi_raw = hi_raw | lo_raw; //AND high and low raw angle value
  delay(5);  // very fast, but can handle the speed.  Go as fast as you can.  "intervalR" will control the publishing rate
  return hi_raw; 
}

void setup() 
{
	Wire.begin();
	pinMode(DIRPin, OUTPUT);
	nh.initNode();
	while (!nh.connected())
	{
	  nh.spinOnce();
	}
	nh.loginfo("Tractor is connected");
	delay(1);

}

void loop() 
{
	steer_angle_val = returnRawAngle(); // read the current angle
	if (steer_angle_val > 200 && steer_angle_val < 1800) {
		steer_err_value = steering_angle_target - steer_angle_val; // calculate the delta to the target angle
	    sprintf (buffer, "Steer angle : %02.01f", steer_angle_val);  
	    nh.loginfo(buffer);
		if (steer_err_value < -20){
		  nh.loginfo("steer_left");
		  digitalWrite(DIRPin, HIGH);
		  analogWrite(PWMPin, steer_effort); 
		} else if (steer_err_value > 20){
		  nh.loginfo("steer_right");
		  digitalWrite(DIRPin, LOW);
		  analogWrite(PWMPin, steer_effort); 
		} else {
		  analogWrite(PWMPin, 0);
		  sprintf (buffer, "At goal : %02.01f", steer_angle_val);
		}
	}
    delay(50);
    nh.spinOnce();
}
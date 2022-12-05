/*

Reads a list of targets; Sends commands to motor controller connected to Teensy using commands digitalWrite(DIRPin, HIGH); 
and analogWrite(PWMPin, steer_effort); Stops sending commands once the angle sensor returns a value very near the target by 
reading returnRawAngle() and comparing to the target.  The program uses: sprintf (buffer, "Steer angle 2 : %02.01f", steer_angle_val);
and nh.loginfo("pausing"); to communicate status information.

Caution:
1. This is just to test the system.
2. Test first on the desk; Then test the single point program before using this multi-point test.
3. Keep the steer_effort low in case something goes bad.

Al's lawn tractor: hard right: 1600; hard left: 368; Straight appears to be 1075 - total: 1232

Not finished
- Calculate how many readings the filter routine is taking out - decide if further analysis is needed
- Confirm the left, right and straight settings are not moving after multiple starts

*/
#include "ros.h"
#include <Wire.h>

int AS5600_ADR = 0x36;  // the address of the board on the SDA bus, printed on the circut board
const int raw_ang_hi = 0x0c;
const int raw_ang_lo = 0x0d;

//int steering_angle_target[] = {1075, 1180, 1285, 1390, 1075, 934, 792, 650};  // left to right, but not to extreme
float steering_angle_target[] = {.65, 0, -.65};
int next_pos = 0;
float steer_angle_val = 0;
float steer_err_value = 0;
int steer_effort = 50;
int DIRPin = 14; 
int PWMPin = 20;
char buffer[50];

ros::NodeHandle nh;
//std_msgs::Float32 front_angle_avg_msg; 
//std_msgs::Float32 &front_angle_avg_msg; 
void get_front_angle(const std_msgs::Float32& front_angle_avg_msg)
{
	steer_angle_val = front_angle_avg_msg.data;
}

ros::Subscriber <std_msgs::Float32> sub("/front_angle_avg", get_front_angle);

/*
float returnRawAngle()
{
  // Read Raw Angle Low Byte
  Wire.beginTransmission(AS5600_ADR);
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
  delay(5);  // Go as fast as you can.  
  return hi_raw; 
}
*/

void setup() {
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
	for (byte i = 0; i < (sizeof(steering_angle_target) / sizeof(steering_angle_target[0])); i++) {
		while (next_pos == 0) {
			//steer_angle_val = returnRawAngle(); // read the current angle
			if (steer_angle_val > -1.01 && steer_angle_val < 1.01) {
				steer_err_value = steering_angle_target[i] - steer_angle_val; // calculate the delta to the target angle
			    sprintf (buffer, "Steer angle : %02.01f", steer_angle_val);
			    //nh.loginfo(buffer, "Steer angle : %02.01f", steer_angle_val);
			    nh.loginfo(buffer);
				if (steer_err_value < -.01){
				  nh.loginfo("steer_left");
				  digitalWrite(DIRPin, HIGH);
				  analogWrite(PWMPin, steer_effort); 
				} else if (steer_err_value > .01){
				  nh.loginfo("steer_right");
				  digitalWrite(DIRPin, LOW);
				  analogWrite(PWMPin, steer_effort); 
				} else {
				  analogWrite(PWMPin, 0);
				  //nh.loginfo(buffer, "At goal : %02.01f", steer_angle_val);
				  sprintf (buffer, "At goal : %02.01f", steer_angle_val);
				  sprintf (buffer, "Steer angle 2 : %02.01f", steer_angle_val);
				  nh.loginfo("pausing");
				  next_pos = 1;
				  delay(5000);
				}
			}
		    delay(50);
		    nh.spinOnce();
		}
		next_pos = 0;
	}
}
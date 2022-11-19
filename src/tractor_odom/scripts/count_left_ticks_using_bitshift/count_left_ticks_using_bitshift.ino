/*
 * Description: Calculate the accumulated ticks for left wheel using the AS5048 magnetic encoder
 * another example at: Website: https://automaticaddison.com
 * When moving forward the tick count is negative
 */

#include <Wire.h>

#include <ros.h>
#include <std_msgs/Int32.h>
 
// Handles startup and shutdown of ROS
ros::NodeHandle nh;

int print_info_interval = 2000;
int tick_pub_interval = 100;
long prev_time_print_info = 0;
long prev_time_tick_pub = 0;
long currentMillis = 0;

#define AS5048B_ANGLMSB_REG 0xFE //bits 0..7
#define AS5048B_RESOLUTION 16384.0 //14 bits
#define AS5048_ADDRESS 0x40
const int poll_AS5048B_Interval = 100; // 1000/10 or 10 Hz
unsigned long prev_time_poll_AS5048B = 0;
uint16_t current_position;
uint16_t last_position;
int16_t position_movement;
int16_t ticks_at_rest = 10;
int32_t rotational_position = 0;
uint16_t bitshift_cur_pos = 0;
uint16_t bitshift_last_pos = 0;
int16_t bitshift_pos_delta = 0;

std_msgs::Int32 left_wheel_tick_count;
ros::Publisher leftPub("left_ticks", &left_wheel_tick_count);

uint16_t AMS_AS5048B_readReg16() {  //reference: https://github.com/sosandroid/AMS_AS5048B
  byte requestResult;
  byte readArray[2];
  uint16_t readValue = 0;
  Wire.beginTransmission(AS5048_ADDRESS);
  Wire.write(AS5048B_ANGLMSB_REG);
  requestResult = Wire.endTransmission(false);
  if (requestResult){
    Serial.print("I2C error: ");
    Serial.println(requestResult);
  }
  Wire.requestFrom(AS5048_ADDRESS, 2);
  for (byte i=0; i < 2; i++) {
    readArray[i] = Wire.read();
  }
  readValue = (((uint16_t) readArray[0]) << 6);
  readValue += (readArray[1] & 0x3F);
  return readValue;

}

void setup() {
  Serial.begin(115200);
  Serial.print("left tick counter program has started ");
  Serial.println();
  Serial.println();      
  Wire.begin();
  current_position = AMS_AS5048B_readReg16();
  last_position = current_position;

  // ROS Setup
  nh.getHardware()->setBaud(115200);
  nh.initNode();
  nh.advertise(leftPub);  
}
 
void loop() {
  currentMillis = millis(); 
  if (currentMillis - prev_time_poll_AS5048B >= poll_AS5048B_Interval) {
    prev_time_poll_AS5048B = currentMillis;
    current_position = AMS_AS5048B_readReg16();      
    perform_calc();
    last_position = current_position;        
    left_wheel_tick_count.data = rotational_position;
    }  

  if (currentMillis - prev_time_print_info > print_info_interval) {
    prev_time_print_info = currentMillis;
    //Serial.println();
    //Serial.println();    
    Serial.print("last_position: ");
    Serial.print(last_position);  
    Serial.print(", current_position: ");
    Serial.print(current_position);  
    Serial.print(", ticks last poll: ");
    Serial.print(position_movement);       
    Serial.print(", total_ticks_moved: ");
    Serial.print(rotational_position);   
    Serial.print(", full revolutions: ");
    Serial.print(rotational_position/AS5048B_RESOLUTION);       
    Serial.println();
  }

  if (currentMillis - prev_time_tick_pub > tick_pub_interval) {
    prev_time_tick_pub = currentMillis;
    leftPub.publish( &left_wheel_tick_count );
    nh.spinOnce();
    }
  
}
void perform_calc(){
    bitshift_cur_pos = current_position << 2; //Bitshiftleft - The leftmost 2 bits in current_position are shifted out of existence
    bitshift_last_pos = last_position << 2;
    bitshift_pos_delta = (bitshift_cur_pos - bitshift_last_pos);
    position_movement = bitshift_pos_delta >> 2; //BitshiftRight 2 bits
    if (position_movement > ticks_at_rest){  //ticks need to be more than 10
      rotational_position += position_movement; // Update the absolute position values. (Position of this encoder since CPU reset.)
      }
    if (position_movement < (ticks_at_rest*-1)) {  // negative for the left wheel is moving forward
      rotational_position += position_movement; // Update the absolute position values. (Position of this encoder since CPU reset.)
      }
}

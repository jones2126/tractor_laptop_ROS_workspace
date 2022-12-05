/*
 * Author: Automatic Addison
 * Website: https://automaticaddison.com
 * Description: Calculate the accumulated ticks for each wheel using the 
 * built-in encoder (forward = positive; reverse = negative) 
 */

#include <Wire.h>

// Minumum and maximum values for 14-bit integers
const int encoder_minimum = -16384;
const int encoder_maximum = 16384;
 
// Keep track of the number of wheel ticks
int left_wheel_tick_count = 0;
 
// One-second interval for measurements
int interval = 1000;
long previousMillis = 0;
long currentMillis = 0;

#define AS5048B_ANGLMSB_REG 0xFE //bits 0..7
#define AS5048B_RESOLUTION 16384.0 //14 bits
#define AS5048_ADDRESS 0x40
const int poll_AS5048B_Interval = 100; // 1000/10 or 10 Hz
unsigned long prev_time_poll_AS5048B = 0;
uint16_t current_position;
uint16_t last_position;
int16_t position_movement;
int32_t rotational_position;

uint16_t bitshift_cur_pos;
uint16_t bitshift_last_pos;
int16_t bitshift_pos_delta;
    uint16_t readValue = 0;

uint16_t AMS_AS5048B_readReg16() {  //reference: https://github.com/sosandroid/AMS_AS5048B
    byte requestResult;
    byte readArray[2];
    //uint16_t readValue = 0;
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
    //reference: next 5 lines are based on magic code from Jeff Sampson - thank you!
    bitshift_cur_pos = readValue << 2; //Bitshiftleft - The leftmost 2 bits in current_position are shifted out of existence
    bitshift_last_pos = last_position << 2;
    bitshift_pos_delta = (bitshift_cur_pos - bitshift_last_pos);
    position_movement = bitshift_pos_delta >> 2; //BitshiftRight 2 bits
    rotational_position += position_movement; // Update the absolute position values. (Position of this encoder since CPU reset.)
    last_position = readValue;

    if (rotational_position > 10000) {
      Serial.print(">10000, ");
      rotational_position = 0 - (65535 - rotational_position);
    }
    else if (rotational_position < -10000) {
      Serial.print("<10000, ");
      rotational_position = 65535-rotational_position;
    }  
    prev_time_poll_AS5048B = millis();  
    return rotational_position;
}


void setup() {
  Serial.begin(115200);
  Serial.print("left tick counter ");
  Wire.begin();
  current_position = AMS_AS5048B_readReg16();
  last_position = current_position;
  rotational_position = 0;  
}
 
void loop() {
  currentMillis = millis();
  if (millis() - prev_time_poll_AS5048B >= poll_AS5048B_Interval) {
    left_wheel_tick_count = AMS_AS5048B_readReg16();
    }  

  // If one second has passed, print the number of ticks
  if (currentMillis - previousMillis > interval) {
    previousMillis = currentMillis;
    Serial.print("Number of Ticks: ");
    Serial.print(left_wheel_tick_count);
    Serial.print(", readvalue: ");
    Serial.println(readValue);    
    Serial.println();
  }
}

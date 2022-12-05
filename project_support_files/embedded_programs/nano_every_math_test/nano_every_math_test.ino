#define AS5048B_RESOLUTION 16384.0 //14 bits
const float wheel_circumfrence = 1.59593; // the wheel has a diameter of 20" or 0.508 meters
float meters_travelled = 0;
int16_t position_movement;
int32_t rotational_position;
//float rotational_position;
  char buffer[40];
  char meters_travelled_str[10];
  char rotation_str[10];
  float rotation = 0;
  int16_t numBurritos = 3;
  float temp = 147.3;

void setup() {
    // put your setup code here, to run once:
    Serial.begin(115200);
    rotational_position = 2;
    //rotational_position += position_movement;
    Serial.println("In setup");
    Serial.print("(rotational_position / AS5048B_RESOLUTION):");
    Serial.println((rotational_position / AS5048B_RESOLUTION));
    //rotation = rotational_position / AS5048B_RESOLUTION;
    rotation = 2.0 / 16384;
    dtostrf(rotation,3,5,rotation_str);
    sprintf(buffer, "2.0 / 16384: %s", rotation_str);
    Serial.println(buffer);
    rotation = 2.0 / AS5048B_RESOLUTION;
    dtostrf(rotation,3,5,rotation_str);
    sprintf(buffer, "2.0 / AS5048B_RESOLUTION: %s", rotation_str);
    Serial.println(buffer);
    rotation = 2 / AS5048B_RESOLUTION;
    dtostrf(rotation,3,5,rotation_str);
    sprintf(buffer, "2 / AS5048B_RESOLUTION: %s", rotation_str);
    Serial.println(buffer); 
    rotation = 2 / 16384;
    dtostrf(rotation,3,5,rotation_str);
    sprintf(buffer, "2 / 16384: %s", rotation_str);
    Serial.println(buffer);  
    meters_travelled = ((rotational_position / AS5048B_RESOLUTION) * wheel_circumfrence); 
    dtostrf(meters_travelled,3,5,meters_travelled_str);
    sprintf(buffer, "meters_travelled: %s", meters_travelled_str);
    Serial.println(buffer);
}

void loop() {
  // put your main code here, to run repeatedly:

}

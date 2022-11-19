

uint16_t current_position = 0;
uint16_t last_position = 0;
int16_t position_movement;
int32_t rotational_position = 0;
uint16_t bitshift_cur_pos = 0;
uint16_t bitshift_last_pos = 0;
int16_t bitshift_pos_delta = 0;
int a = 1;

void setup() {
    Serial.begin(115200);
    Serial.print("code tester program has started ");
    Serial.println();
    Serial.println();     
    current_position = 1;  
}

void loop() {
    // put your main code here, to run repeatedly:
    while( a < 18 ) {
        perform_calc();
        print_info();      
        printf("value of a: %d ", a);
        a++;
        current_position = current_position + 8192;
        if (current_position > (pow(2,14))){ 
          current_position = 1;  
          }
        }

}

void print_info(){
    Serial.print("last pos: "); Serial.print(last_position);
    Serial.print(", bitshift_last_pos: "); Serial.print(bitshift_last_pos);  
    Serial.print(", current pos: "); Serial.print(current_position);
    Serial.print(", bitshift_cur_pos: "); Serial.print(bitshift_cur_pos);    
    Serial.print(", movement: "); Serial.print(position_movement); 
    Serial.print(", total movement: "); Serial.print(rotational_position);
    Serial.println(); 
    last_position = current_position;    
}
void perform_calc(){
    bitshift_cur_pos = current_position << 2; //Bitshiftleft - The leftmost 2 bits in current_position are shifted out of existence
    bitshift_last_pos = last_position << 2;
    bitshift_pos_delta = (bitshift_cur_pos - bitshift_last_pos);
    position_movement = bitshift_pos_delta >> 2; //BitshiftRight 2 bits
    rotational_position += position_movement; // Update the absolute position values. (Position of this encoder since CPU reset.)
}

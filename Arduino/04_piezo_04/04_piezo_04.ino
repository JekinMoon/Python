const int piezo_pin = 8;
const int switch_pin = 2;

void setup() {
  Serial.begin(9600);
  pinMode(piezo_pin, OUTPUT);
  pinMode(switch_pin, INPUT_PULLUP);
}

void loop() {
  int ButtonState = digitalRead(switch_pin);
  digitalWrite(piezo_pin, LOW);
  
  if(ButtonState==LOW){
    Serial.println("BUZZER ON");
    digitalWrite(piezo_pin, HIGH);
  } else {
    Serial.println("BUZZER OFF");
  }
  delay(100);   
}

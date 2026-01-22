int BTN = 2; 


void setup() {
  Serial.begin(9600);
  pinMode(BTN, INPUT);
}

void loop() {
  int BTNstate = digitalRead(BTN);
  Serial.println(BTNstate);
  delay(500);
}

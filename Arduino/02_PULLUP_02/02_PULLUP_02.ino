int switch1 = 12;
int switch2 = 11;

int ledRed = 4;
int ledGreen = 3;

void setup() {
  Serial.begin(9600);
  pinMode(switch1, INPUT_PULLUP);
  pinMode(switch2, INPUT_PULLUP);
  pinMode(ledRed, OUTPUT);
  pinMode(ledGreen, OUTPUT);
}

void loop() {
  int SW1 = digitalRead(switch1);
  int SW2 = digitalRead(switch2);

  digitalWrite(ledRed, LOW);
  digitalWrite(ledGreen, LOW);

  if(SW1==LOW){
    Serial.println("Switch : RED");
    digitalWrite(ledRed, HIGH);
  }
  if(SW2==LOW){
    Serial.println("Switch : Green");
    digitalWrite(ledGreen, HIGH);
  }
  delay(100);
}

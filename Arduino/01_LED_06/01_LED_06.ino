// 함수로 분리

int LEDS[] = {10, 11, 12};
int count = 3;

void turnOnALL() {
  for (int i = 0; i < count; i++) {
    digitalWrite(LEDS[i], HIGH);
    // delay(500);
  }
}

void turnOffALL() {
  for (int i = 0; i < count; i++) {
    digitalWrite(LEDS[i], LOW);
    delay(500);
  }
}

void setup() {
  for (int i = 0; i < count; i++) {
    pinMode(LEDS[i], OUTPUT);
  }
}

void loop() {
  turnOnALL();
  delay(500);

  turnOffALL();
}

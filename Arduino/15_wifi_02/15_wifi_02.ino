#include <SoftwareSerial.h>

SoftwareSerial myESP(2,3); 

// ESP 모듈 속도가 9600으로 바뀌었는지 확인

void setup() {
  Serial.begin(9600);
  myESP.begin(9600);
  Serial.println("=== TEST 9600 ===");
}

void loop() {
  if (myESP.available()) {
    Serial.write(myESP.read());
  }
  if (Serial.available()) {
    myESP.write(Serial.read());
  }
}
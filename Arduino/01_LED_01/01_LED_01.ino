void setup() {
  pinMode(3, OUTPUT); // 디지털 3번 핀을 출력으로 사용한다 정의
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(3, HIGH);  //digitalWrite = 출력 // 3번 핀을 HIGH(5V)로 출력해라
  delay(1000);            // LED 켜진 상태로 1초 중지          
  digitalWrite(3, LOW);   // 3번 핀을 LOW(0V)로 출력해라 => LED 꺼짐
  delay(1000);            // LED 꺼진 상태로 1초 중지          
}

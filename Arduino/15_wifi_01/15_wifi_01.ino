#include <SoftwareSerial.h>

SoftwareSerial myESP(2,3); // 02=RX(ESP TX), 03=TX(ESP RX)

// 우리가 사용하는 와이파이 모듈은 115200 속도를 지원함
// 115200 속도로 연결한 뒤 9600으로 다운그레이드할 예정

void setup() {
  Serial.begin(115200);
  myESP.begin(115200);
  Serial.println("준비 완료, AT 명령어를 입력하세요");
  // AT : begin이나 init처럼 초기화(시작)하는 명령어
  // 뒤에 +를 붙여서 AT로 명령도 보낼 수 있음
  // 예) AT+UART_DEF=9600,8,1,0,0
  // 위 명령어는 통신 속도를 9600으로 영원히 바꿔라
}

void loop() {
  if (myESP.available()) {
    Serial.write(myESP.read());
  }
  if (myESP.available()){
    myESP.write(myESP.read());
  }
}

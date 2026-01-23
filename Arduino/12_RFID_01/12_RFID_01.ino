#include <SPI.h> // 단거리간 통신 방법 중 하나
#include <MFRC522.h>

#define SS_PIN 10
#define RST_PIN 9 

MFRC522 myMFRC(SS_PIN, RST_PIN); // MFRC522 라이브러리를 사용해서 나만의 myMFRC객체 생성

void setup() {
  Serial.begin(9600);
  SPI.begin(); // SPI 통신 초기화(실행)
               // SPI 통신: 하나의 master(아두이노)와 다수의 slave(종속적인 역할, RFID리더)간의 통신 방식
  myMFRC.PCD_Init(); // RFID리더기 초기화(실행)
  myMFRC.PCD_DumpVersionToSerial(); // 연결 확인용 버전 정보 출력 코드
  Serial.println("RFID 통신 준비 완료");
}

void loop() {
  // 예외 처리
  // 1. 근체에 카드가 있는지 확인
  if (!myMFRC.PICC_IsNewCardPresent()) 
    return;

  // 2. 근처 태그의 UID 확인
  if (!myMFRC.PICC_ReadCardSerial()) 
    return;

  Serial.print("Car UID: ");
  // 태그의 UID 값을 받아 출력
  // 아두이노는 한 번의 통신에 1바이트만 통신이 가능하기 때문에
  // 근처 태그의 UID 길이만큼 반복문을 통해서 시리얼 모니터에 출력
  for (byte i = 0; i < myMFRC.uid.size; i++) {
    Serial.print(myMFRC.uid.uidByte[i]);
    Serial.print(" ");
  }

  Serial.println(""); // 하나의 태그 UID 출력 완료 시 줄 바꿈

  // 통신 종료 (통신 종료를 안하면 다음 루프에서 근처의 태그 UID를 인식하지 못하는 경우가 많음)
  myMFRC.PICC_HaltA();
  myMFRC.PCD_StopCrypto1();

  delay(1000); // 연속 일치 방지
}

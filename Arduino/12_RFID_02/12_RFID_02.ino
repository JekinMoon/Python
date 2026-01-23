#include <SPI.h> // 단거리간 통신 방법 중 하나
#include <MFRC522.h>

#define SS_PIN 10
#define RST_PIN 9 

MFRC522 myMFRC(SS_PIN, RST_PIN); // MFRC522 라이브러리를 사용해서 나만의 myMFRC객체 생성

int LED_B = 3;
int LED_R = 4;
int PIEZO = 6;


void setup() {
  Serial.begin(9600);
  SPI.begin(); // SPI 통신 초기화(실행)
               // SPI 통신: 하나의 master(아두이노)와 다수의 slave(종속적인 역할, RFID리더)간의 통신 방식
  myMFRC.PCD_Init(); // RFID리더기 초기화(실행)
  myMFRC.PCD_DumpVersionToSerial(); // 연결 확인용 버전 정보 출력 코드
  Serial.println("RFID 통신 준비 완료");

  pinMode(LED_B, OUTPUT);
  pinMode(LED_R, OUTPUT);
  pinMode(PIEZO, OUTPUT);
}

void loop() {
  // 예외 처리
  // 1. 근체에 카드가 있는지 확인
  if (!myMFRC.PICC_IsNewCardPresent()) 
    return;

  // 2. 근처 태그의 UID 확인
  if (!myMFRC.PICC_ReadCardSerial()) 
    return;


  if (myMFRC.uid.uidByte[0] = 91 && myMFRC.uid.uidByte[1] == 72
      && myMFRC.uid.uidByte[2] == 176 && myMFRC.uid.uidByte[3] == 1) {
    digitalWrite(LED_B, HIGH);
    digitalWrite(LED_R, LOW);
    Serial.println("BLUE LED PIN ON!");
    digitalWrite(PIEZO, HIGH);
    delay(1000);
    digitalWrite(PIEZO, LOW);
    digitalWrite(LED_B, LOW);

  } else{
    digitalWrite(LED_R, HIGH);
    digitalWrite(LED_B, LOW);
    Serial.println("Error!");
    digitalWrite(PIEZO, HIGH);
    delay(500);
    digitalWrite(PIEZO, LOW);
    delay(500);
    digitalWrite(PIEZO, HIGH);
    delay(500);
    digitalWrite(PIEZO, LOW);
    digitalWrite(LED_R, LOW);
  }

}


#define GAS_AO A0
#define GAS_DO 8
#define PIEZO 12
#define LED 13


void setup() {
  pinMode(PIEZO, OUTPUT);
  pinMode(LED, OUTPUT);

  Serial.begin(9600);
  pinMode(GAS_AO, INPUT);
  pinMode(GAS_DO, INPUT);
  Serial.println("히터 가열 시작");
  delay(1000);
  Serial.println("히터 가열 종료 동작 시작");
}

void loop() {
  float sensorValue = analogRead(GAS_AO);
  int sensorDValue = digitalRead(GAS_DO);

  Serial.print("아날로그 센서 입력: ");
  Serial.print(sensorValue);

  Serial.print(" | ");
  Serial.println(" ");

  Serial.print("디지털 센서 입력: ");
  Serial.print(sensorDValue);
 
  if (sensorValue > 300) {
    Serial.print("연기 감지 !!");
    Serial.println(" ");
    digitalWrite(PIEZO, HIGH);
    digitalWrite(LED, HIGH);
 }
  else {
    digitalWrite(PIEZO, LOW);
    digitalWrite(LED, LOW);
  }
  delay(500);
 
}

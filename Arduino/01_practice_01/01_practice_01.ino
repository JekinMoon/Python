//현재 온습도와 AO 출력값을 시리얼 모니터에 출력
//현재 가스농도는 깨끗한 공기 상태의 저항값을 측정해 코드에 반영해야하고,
//AO 출력값은 ADC값임 그렇기 때문에 가스농도로 출력하는 것은 코드가 너무 어려워지니 간단하게 AO 출력값 출력하기

#include <DHT.h>

#define DHTPIN 3
#define DHTTYPE DHT11   
#define GAS_AO A0

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  float t = dht.readTemperature();
  float h = dht.readHumidity();
  int gas = analogRead(A0);

  Serial.print("온도: ");
  Serial.print(t);
  Serial.print(" C | 습도: ");
  Serial.print(h);
  Serial.print(" % | 가스 AO: ");
  Serial.println(gas);

  delay(1000);
}
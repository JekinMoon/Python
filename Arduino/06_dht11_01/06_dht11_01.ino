#include <DHT.h>
#define DHTPIN 2
#define DHTTYPE DHT11

DHT myDHT(DHTPIN, DHTTYPE);


void setup() {
  Serial.begin(9600);
  myDHT.begin();
  
}

void loop() {
  delay(2000);
  float h = myDHT.readHumidity(); // 습도 값 읽어옴
  float c = myDHT.readTemperature(); // 섭씨 온도 값 읽어옴
  float f = myDHT.readTemperature(true); // 화씨 온도 값 읽어옴

  // 측정 실패 시 예외 처리
  if(isnan(h) || isnan(c) || isnan(f) ) {
    Serial.println("값을 읽어오지 못했습니다.");
    return; // 아래 코드를 실행시키지 않기 위해 loop 함수 자체를 나감
  }

  // 정상 측정이 되었을 때 실행되는 코드 
  Serial.print("습도: ");
  Serial.print(h); 
  Serial.print("섭씨온도: ");
  Serial.print(c);
  Serial.print("화씨온도: ");
  Serial.print(f);
  Serial.println();

}

#include <DHT.h>

#define DHTPIN 3
#define DHTTYPE DHT11   
#define GAS_AO A0
#define GAS_DO 2

#define LED_RED 10
#define LED_BLUE 9
#define LED_GREEN 8

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();

  pinMode(LED_RED, OUTPUT);
  pinMode(LED_GREEN, OUTPUT);
  pinMode(LED_BLUE, OUTPUT);
}

void loop() {
  float t = dht.readTemperature();
  float h = dht.readHumidity();
  int gas = analogRead(GAS_AO);

  Serial.print("온도: ");
  Serial.print(t);
  Serial.print(" C | 습도: ");
  Serial.print(h);
  Serial.print(" % | 가스 AO: ");
  Serial.println(gas);


  if (gas < 300) {
    digitalWrite(LED_GREEN, HIGH);
    digitalWrite(LED_BLUE, LOW);
    digitalWrite(LED_RED, LOW);
  }
  else if (gas < 600) {
    digitalWrite(LED_GREEN, LOW);
    digitalWrite(LED_BLUE, HIGH);
    digitalWrite(LED_RED, LOW);
  }
  else {
    digitalWrite(LED_GREEN, LOW);
    digitalWrite(LED_BLUE, LOW);
    digitalWrite(LED_RED, HIGH);
    
  
  }

  delay(500); 

}
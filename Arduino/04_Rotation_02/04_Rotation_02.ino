
void setup() {
  Serial.begin(9600);
  pinMode(10, OUTPUT);
}

void loop() {
  int resistor = analogRead(A0);
  Serial.println(resistor);
  resistor = map(resistor, 0, 1023, 0, 255); // map(매핑하고자 하는값, 기존의 최소값, 기존의 최대값, 매핑할 값의 최소값, 매핑할 값의 최대값)
  // map() => 첫번째 매개변수를 네/다섯번째 범위로 1:1 매핑해주는 역할
  // map(50, 50, 100, 0, 50) 
  // => 첫번째 매개변수는 50 => 50~100
  // 결과값 => 0~50 => 0
  
  analogWrite(10, resistor);
  delay(100);
}

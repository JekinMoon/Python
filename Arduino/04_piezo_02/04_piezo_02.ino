const int piezo_pin = 8; // 읽기 전용 상수 선연 => 이후 값 수정 불가

const int melody[] ={
  // 도, 레, 미, 파, 솔, 라, 시, 도
  262, 294, 330, 349, 392, 440, 494, 523
};

void setup() {
  tone(piezo_pin, melody[0], 500); delay(500);
  tone(piezo_pin, melody[1], 500); delay(500);
  tone(piezo_pin, melody[2], 500); delay(500);
  tone(piezo_pin, melody[3], 500); delay(500);
  tone(piezo_pin, melody[4], 500); delay(500);
  tone(piezo_pin, melody[5], 500); delay(500);
  tone(piezo_pin, melody[6], 500); delay(500);
  tone(piezo_pin, melody[7], 500); delay(500);
}

void loop() {
  
}

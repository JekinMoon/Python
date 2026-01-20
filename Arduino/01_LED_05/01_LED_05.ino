// for문 사용

/*
for문을 사용해 배열을 순회하도록 할 것

배열 선언 방법 : 자료형 변수[] = {요소}

C기반 언어에서 배열 초기화하는 문법
C++에서도 동일하게 사용

int LEDS[] = {10, 11, 12};

배열 접근
LEDS[0] = 10
*/

int LEDS[] = {10, 11, 12};
int count = 3; // 배열 요소의 수가 달라져도 해당 변수값만 수정하면 됨

void setup() {
  for (int i = 0; i < count; i++) {
    pinMode(LEDS[i], OUTPUT);
  }
}

void loop() {
  for (int i = 0; i < count; i++) {
    digitalWrite(LEDS[i], HIGH);
    delay(500);
  }
    // delay(500); // 여기에 써도 괜찮음. 그냥 동작 방식이 달라지는 것

  for (int i = 0; i < count; i++) {
    digitalWrite(LEDS[i], LOW);
    delay(500);
  }
}

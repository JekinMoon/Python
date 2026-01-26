int data;

void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  digitalWrite(13, LOW);
}

void loop() {
  while(Serial.available()){ // 시리얼 통신이 가능한지 확인 및 시리얼 통신이 되는동안 아래 스코프(중괄호) 코드 반복
    data = Serial.read(); // 아두이노가 PC에서 받은 1바이트를 가져와 data 변수에 저장
  }

  if (data == '1'){
    digitalWrite(13, HIGH);
  } else if (data == '0') {
    digitalWrite(13, LOW);
  }
}


// 동작하지 않는 이유
// 1. 아두이노에서 시리얼 모니터를 열고 파이썬 실행 시 동작 X
  // 시리얼 통신을 하는 곳은 1곳만 가능(복수 통신 불가)
  // 같은 이유로 파이썬 코드 실행 중 아두이노 새로운 코드 업로드 시도 시 에러 발생
// 2. 따옴표
  // ''(작은 따옴표): 조금 더 느슨하게 비교
  // ""(큰 따옴표): 문자열로 인식하고 **메모리 주소**까지 비교


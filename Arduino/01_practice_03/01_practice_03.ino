#define LED_RED1 10
#define LED_RED2 11
#define TRIG 7
#define ECHO 6

void setup() {
  Serial.begin(9600);
  pinMode(LED_RED1, OUTPUT);
  pinMode(LED_RED2, OUTPUT);
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);
}

void loop() {
  digitalWrite(TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);
  long duration = pulseIn(ECHO, HIGH);
  long distance = duration * 0.034 / 2;

  if (distance > 0 && distance <= 5) {
    digitalWrite(LED_RED1, HIGH);
    digitalWrite(LED_RED2, HIGH);
    delay(100); 
    
    digitalWrite(LED_RED1, LOW);
    digitalWrite(LED_RED2, LOW);
    delay(100); 
  } 
  else {
    digitalWrite(LED_RED1, HIGH); 
    digitalWrite(LED_RED2, LOW);  
  }
}
void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
}

void loop() {
  int light = analogRead(A0);
  Serial.println(light);

  if (light > 700) 
    digitalWrite(13, HIGH);
  else
    digitalWrite(13, LOW);
}

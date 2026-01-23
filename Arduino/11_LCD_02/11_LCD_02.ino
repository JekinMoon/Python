#include <Servo.h>
#include <LiquidCrystal_I2C.h>

Servo myServo;
LiquidCrystal_I2C myLCD(0x27, 16, 2);

int angle = 0;

void setup() {
  Serial.begin(9600);
  myServo.attach(8);
  myLCD.init();
  myLCD.backlight();
}

void loop() {
  int angleVal = analogRead(A0);
  Serial.println(angleVal);
  angle = map(angleVal, 0, 1023, 0, 180);

  myServo.write(angle);

  myLCD.setCursor(0,0);
  myLCD.print("Servo Angle");
  myLCD.setCursor(0,1);
  myLCD.print(angle);
  delay(500);

  myLCD.clear();
}

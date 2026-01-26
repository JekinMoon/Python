#include <wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

bye dino[8]
{ B0000,
  B00111,
  B00101,
  B10111,
  B11100,
  B11111,
  B01101,
  B01100
};

bye tree[8]
{ B00011,
  B11011,
  B11011,
  B11011,
  B11011,
  B11111,
  B01110,
  B01110
};

void setup() {
  // put your setup code here, to run once:

}

void loop() {
  // put your main code here, to run repeatedly:

}

#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

byte dino[8]
{ B0000,
  B00111,
  B00101,
  B10111,
  B11100,
  B11111,
  B01101,
  B01100
};

byte tree[8]
{ B00011,
  B11011,
  B11011,
  B11011,
  B11011,
  B11111,
  B01110,
  B01110
};

const int BUTTON_ENTER = 2;
const int LCD_COLUMN = 16;
const int DINO_CHAR = 7;
const int TREE_CHAR = 6;

boolean isPlaying = true;
boolean isDinoOnGround = true;

int score = 0;
boolean buttonPressed = false;


void setup() {
  Wire.begin();
  lcd.init();
  lcd.backlight();
  lcd.createChar(DINO_CHAR, dino);
  lcd.createChar(TREE_CHAR, tree);
  pinMode(BUTTON_ENTER, INPUT_PULLUP);
}

void loop() {
  if(isPlaying) {
    handleGame();
  } else{
    if(digitalRead(BUTTON_ENTER) == LOW && !buttonPressed){
      buttonPressed = true;
      isPlaying = true;
      delay(500);
    } else if (digitalRead(BUTTON_ENTER) == HIGH && buttonPressed){
      buttonPressed = false;
    }
  }

  delay(300);
}

void handleGame(){
  lcd.clear();

  int buttonPressedTimes = 0;

  int secondPosition = random(4, 9);
  int thirdPosition = random(4,9);
  int firstTreePosition = LCD_COLUMN;
  const int columnValueToStopMoveTrees = -(secondPosition + thirdPosition);

  for (; firstTreePosition >= columnValueToStopMoveTrees; firstTreePosition--){
    lcd.setCursor(13, 0);
    lcd.print(score);

  defineDinoPosition();

  int secondTreePosition = firstTreePosition + secondPosition;
  int thirdTreePosition = secondTreePosition + thirdPosition;

  showTree(firstTreePosition);
  showTree(secondTreePosition);
  showTree(thirdTreePosition);

  if (isDinoOnGround) {
    if (firstTreePosition == 1 || secondTreePosition == 1 || thirdTreePosition == 1) {
      handleGameOver();
      isPlaying = false;
      delay(5000);
      break;
    }
    buttonPressedTimes = 0;
  } else {
    if (buttonPressedTimes > 2) {
      score -= 3;
    }

    buttonPressedTimes++;
  } 
  
  score++;
  delay(500);
  }
}

void handleGameOver(){
  lcd.clear();
  lcd.print("GAME OVER");

  lcd.setCursor(0, 1);
  lcd.print("SCORE: ");
  lcd.print(score);

  score = 0;

  delay(2000);
}

void showTree(int position) {
  lcd.setCursor(position, 1);
  lcd.write(TREE_CHAR);
  lcd.setCursor(position + 1, 1);
  lcd.print(" ");
}

void defineDinoPosition() {
  if(digitalRead(BUTTON_ENTER) == LOW) {
    putDinoOnAir();
  } else {
    putDinoOnGround();
  }
}

void putDinoOnGround() {
  lcd.setCursor(1,1);
  lcd.write(DINO_CHAR);
  lcd.setCursor(1,0);
  lcd.print(" ");

  isDinoOnGround = true;
}

void putDinoOnAir(){
  lcd.setCursor(1,0);
  lcd.write(DINO_CHAR);
  lcd.setCursor(1,1);
  lcd.print(" ");

  isDinoOnGround = false;
}

























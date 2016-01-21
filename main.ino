#include <Time.h>
#include <LiquidCrystal.h>
#include <Timer.h>
Timer t;
String napis;
String nowyNapis;
int valueInput;
String value;

// REJESTR
int dataPin = 2; //DS
int latchPin = 3;  //ST_CP
int clockPin = 4;  //SH_CP
byte data = 0;
int on[] = {0, 0, 0, 0, 0, 0, 0, 0};

// WYŚWIETLACZ
int saver;
int saver2;
LiquidCrystal lcd(13, 12, 8, 7, 6, 5);

// RGB
int rLED = 9;
int sr = 0;
int srt = 0;
int rSin;
int gLED = 10;
int sg = 0;
int sgt = 0;
int gSin;
int bLED = 11;
int sb = 0;
int sbt = 0;
int bSin;
unsigned long int tme;


////////////////////////////////////  SETUP
void setup() {
  Serial.begin(9600);
  saver = t.after(10000, screenSaver);
  lcd.begin(16, 2);
  lcd.setCursor(1, 0);
  lcd.print("Inicjalizacja");
  lcd.setCursor(1, 1);
  lcd.print("systemu...");
  napis = "";

  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  pinMode(A3, INPUT);
  pinMode(A4, INPUT);
  pinMode(A5, INPUT);

  pinMode(rLED, OUTPUT);
  pinMode(gLED, OUTPUT);
  pinMode(bLED, OUTPUT);

  pinMode(latchPin, OUTPUT);
  pinMode(clockPin, OUTPUT);
  pinMode(dataPin, OUTPUT);
  digitalWrite(latchPin, LOW);
  shiftOut(dataPin, clockPin, MSBFIRST, 0);
  digitalWrite(latchPin, HIGH);
}

///////////////////////////////////    SCREENSAVER
void screenSaver() {
  saver2 = t.every(1000, lcdClock);
}

void lcdClock() {
  if (Serial.available() == 0) {
    lcd.clear();
    lcd.print(hour());
    printDigits(minute());
    printDigits(second());
    lcd.setCursor(0, 1);
    lcd.print(day());
    lcd.print(" ");
    lcd.print(month());
    lcd.print(" ");
    lcd.print(year());
  }
}
void printDigits(int digits) {
  lcd.print(":");
  if (digits < 10)
    lcd.print('0');
  lcd.print(digits);
}
//////////////////////////////////////   OUTPUT
void printuj() {
  lcd.print("Odczyt z A");
  lcd.print(nowyNapis);
  Serial.println(analogRead(nowyNapis.toInt()));
}

//////////////////////////////////// LED
void toggleLED() {
  int suma = 0;
  for (int i = 0; i < 8; i++) {
    if (on[i] == 1) {
      int turnOn = potega(i);
      suma = suma + turnOn;
    }
  }
  digitalWrite(latchPin, LOW);
  shiftOut(dataPin, clockPin, MSBFIRST, suma);
  digitalWrite(latchPin, HIGH);
}

int potega(int i) {
  int x = 1;
  for (int j = 0; j < i; j++) {
    x = x * 2;
  }
  return x;
}

void rSIN() {
  analogWrite(rLED, sr);
  if (srt == 0) {
    sr++;
    if (sr == 255) {
      srt = 1;
    }
  } else {
    sr--;
    if (sr == 0) {
      srt = 0;
    }
  }
}
void rSINRun() {
  rSin = t.every(5, rSIN);
}


void gSIN() {
  analogWrite(gLED, sg);
  if (sgt == 0) {
    sg++;
    if (sg == 255) {
      sgt = 1;
    }
  } else {
    sg--;
    if (sg == 0) {
      sgt = 0;
    }
  }
}
void gSINRun() {
  gSin = t.every(5, gSIN);
}


void bSIN() {
  analogWrite(bLED, sb);
  if (sbt == 0) {
    sb++;
    if (sb == 255) {
      sbt = 1;
    }
  } else {
    sb--;
    if (sb == 0) {
      sbt = 0;
    }
  }
}
void bSINRun() {
  bSin = t.every(5, bSIN);
}


////////////////////////////////////  MAIN
void loop() {
  if (Serial.available() > 0) {
    char z = Serial.read();
    lcd.setCursor(0, 0);
    if (z == '#') { //////////////////  SET
      t.stop(saver);
      t.stop(saver2);
      lcd.clear();
      ///////////////////////  TOGGLE
      if (napis ==  "TOGGLE") {
        if (value == "OFF") {
          digitalWrite(latchPin, LOW);
          shiftOut(dataPin, clockPin, MSBFIRST, 0);
          digitalWrite(latchPin, HIGH);
          for (int i = 0; i < 8; i++) {
            on[i] = 0;
          }
        } else if (value == "ON") {
          digitalWrite(latchPin, LOW);
          shiftOut(dataPin, clockPin, MSBFIRST, 255);
          digitalWrite(latchPin, HIGH);
          for (int i = 0; i < 8; i++) {
            on[i] = 1;
          }
        } else {
          if (on[value.toInt()] == 0) {
            on[value.toInt()] = 1;
          } else {
            on[value.toInt()] = 0;
          }
          toggleLED();
        }
      }
      lcd.print("Zmiana pinu");
      lcd.print(' ');
      lcd.print(value);
      lcd.setCursor(0, 1);
      for (int i = 0; i < 8; i++) {
        if (on[i] == 1) {
          lcd.print('X');
          lcd.print(' ');
        } else {
          lcd.print('O');
          lcd.print(' ');
        }
      }
      napis = "";
      value = "";
      valueInput = 0;
      saver = t.after(10000, screenSaver);
    } else if (z == '!') { ///////////////  ANALOGWRITE
      t.stop(saver);
      t.stop(saver2);
      lcd.clear();
      ///////////////////////
      if (napis == "RED") {
        if ( value == "SIN") {
          rSINRun();
          lcd.print("Sygnal");
          lcd.setCursor(1, 1);
          lcd.print("modulowany (R)");
        } else if (value == "ON") {
          t.stop(rSin);
          lcd.print("Wlacz czerwony");
          analogWrite(rLED, 255);
          analogWrite(gLED, 0);
          analogWrite(bLED, 0);
        } else if (value == "OFF") {
          lcd.print("Wylacz czerwony");
          t.stop(rSin);
          analogWrite(rLED, 0);
        } else {
          lcd.print("Ustaw czerwony");
          lcd.setCursor(1, 1);
          lcd.print("na");
          lcd.print(value);
          t.stop(rSin);
          analogWrite(rLED, value.toInt());
        }
      } else if (napis == "GREEN") {
        if ( value == "SIN") {
          gSINRun();
          lcd.print("Sygnal");
          lcd.setCursor(1, 1);
          lcd.print("modulowany (G)");
        } else if (value == "ON") {
          lcd.print("Wlacz zielony");
          t.stop(gSin);
          analogWrite(rLED, 0);
          analogWrite(gLED, 255);
          analogWrite(bLED, 0);
        } else if (value == "OFF") {
          lcd.print("Wylacz zielony");
          t.stop(gSin);
          analogWrite(gLED, 0);
        } else {
          lcd.print("Ustaw zielony");
          lcd.setCursor(1, 1);
          lcd.print("na");
          lcd.print(value);
          t.stop(gSin);
          analogWrite(gLED, value.toInt());
        }
      } else if (napis == "BLUE") {
        if ( value == "SIN") {
          bSINRun();
          lcd.print("Sygnal");
          lcd.setCursor(1, 1);
          lcd.print("modulowany (B)");
        } else if (value == "ON") {
          lcd.print("Wlacz niebieski");
          t.stop(bSin);
          analogWrite(rLED, 0);
          analogWrite(gLED, 0);
          analogWrite(bLED, 255);
        } else if (value == "OFF") {
          lcd.print("Wylacz niebieski");
          t.stop(bSin);
          analogWrite(bLED, 0);
        } else {
          lcd.print("Ustaw niebieski");
          lcd.setCursor(1, 1);
          lcd.print("na");
          lcd.print(value);
          t.stop(bSin);
          analogWrite(bLED, value.toInt());
        }
      }
      napis = "";
      value = "";
      valueInput = 0;
      saver = t.after(10000, screenSaver);
    } else if (z == '$') { ///////////// GET
      t.stop(saver);
      t.stop(saver2);
      lcd.clear();
      t.after(200, printuj);
      nowyNapis = napis;
      napis = "";
      saver = t.after(10000, screenSaver);
    } else if (z == '@') { /////////////  TIME
      lcd.clear();
      lcd.print("Ustawiono godzine");
      lcd.setCursor(1, 1);
      lcd.print("i date");
      setTime(napis.toInt());
      napis = "";
    } else if (z == ' ') {
      valueInput = 1;
    } else {
      if (valueInput == 0) {
        napis += z;
      } else {
        value += z;
      }
    }
  }
  t.update();
}

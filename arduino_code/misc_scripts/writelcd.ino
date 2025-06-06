#include <Wire.h>

#include <LiquidCrystal.h>

#include <TimeLib.h>

#include <DS3231.h>

#define DS3231_I2C_ADDRESS 0x68

LiquidCrystal lcd(5, 6, 7, 8, 9, 10);

// TODO -- NEED TO UPDATE RTC

void setup() {
  // rtc.begin();
  // rtc.setTime(15, 18, 00);
  // rtc.setDate(25, 4, 2024);
  lcd.begin(16,2);
  lcd.clear();
  Serial.begin(9600);
  // lcd.clear();
  lcd.setCursor(0, 0);
  //print the gamescore string over lcd
  lcd.print("Gyro out");
}

void loop() {
  
}
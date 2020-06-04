#include <Servo.h>
#include <string.h>

Servo horizontal;
Servo vertical;

String incomingByte = ""; // for incoming serial data

void setup() {
  Serial.begin(9600); // opens serial port, sets data rate to 9600 bps
  horizontal.attach(8);
  vertical.attach(9);
}

void eraseSubStr(String & mainStr, const String & toErase) {
	// Search for the substring in string
	size_t pos = mainStr.indexOf(toErase);
  size_t npos = -1;

	if (pos != npos)
	{
		// If found then erase it from string
		mainStr.remove(pos, toErase.length());
	}
}

void loop() {
  // send data only when you receive data:
  if (Serial.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial.readString();
    String amount = incomingByte;
    String servo = incomingByte;
    eraseSubStr(amount, "servo1 ");
    eraseSubStr(amount, "servo2 ");
    eraseSubStr(servo, amount);
    eraseSubStr(servo, " ");

    if (servo == "servo1") {
      horizontal.write(amount.toInt());
    }

    else if (servo == "servo2") {
      vertical.write(amount.toInt());
    }


    // // say what you got:
    // Serial.print("I received: ");
    // Serial.println(incomingByte, DEC);
  }
}

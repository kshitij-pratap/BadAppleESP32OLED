#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SH110X.h>
#include "byteStream.h"

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64

Adafruit_SH1106G display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

int currentFrame = 0;

void setup() {
    Serial.begin(115200);
    Wire.begin(21, 22);
    Wire.setClock(800000);

    if (!display.begin(0x3C, true)) {
        Serial.println(F("SH110X allocation failed"));
        for (;;);
    }

    display.clearDisplay();
    display.display();
}

void loop() {
    if (currentFrame >= totalFrames) {
        currentFrame = 0; // Loop video
    }

    display.clearDisplay();
    // Pulls each exact frame directly from flash memory
    display.drawBitmap(0, 0, byteStream[currentFrame], SCREEN_WIDTH, SCREEN_HEIGHT, SH110X_WHITE);
    display.display();

    currentFrame++;
    delay(33); // ~30 FPS playback pacing
}
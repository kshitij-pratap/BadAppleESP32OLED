# Bad Apple ESP32 OLED

A hardware-optimized implementation of the classic "_Bad Apple!!_" silhouette art animation, engineered for the ESP32 microcontroller and a 1.3-inch SH1106 OLED display.

This project utilizes a custom Python-based frame extraction pipeline to convert standard video files into a lightweight, flash-ready hexadecimal byte array. This approach bypasses standard C++ compiler bottlenecks and handles memory overflow issues inherent in large uncompressed image buffers.

## Hardware Architecture
* **Microcontroller:** ESP32 Development Board
* **Display Module:** 1.3-inch SH1106 OLED (I2C Interface)

## Pin Configuration
| OLED Pin | ESP32 GPIO | Description |
| :--- | :--- | :--- |
| GND | GND | Common Ground |
| VCC | 3.3V | Logic Power |
| SCL | GPIO 22 | I2C Clock Line |
| SDA | GPIO 21 | I2C Data Line |

## Software Pipeline
1. **gen.py:** A pure Python OpenCV script that processes the source video, downsamples the frame rate to optimize flash memory usage, and encodes the binary pixel data into a structured `byteStream.h` header file.
2. **BadAppleOLED.ino:** The primary execution sketch. It bypasses complex parsing algorithms by reading the 1024-byte frame blocks directly from flash memory and pushing them to the SH1106 buffer sequentially to maintain stable framerates.

## Build & Flash Instructions
1. **Dependencies:** Install the `Adafruit GFX` and `Adafruit SH110X` libraries via the Arduino IDE Library Manager.
2. **Memory Allocation:** The raw frame array requires approximately 1.8 MB of storage, which exceeds the default ESP32 app partition. In the Arduino IDE, navigate to **Tools > Partition Scheme** and select **Huge APP (3MB No OTA / 1.2MB SPIFFS)**.
3. **Execution:** Ensure `byteStream.h` is located in the same directory as `BadAppleOLED.ino`. Compile and upload to the ESP32.

import cv2
import os

video_path = input("Enter video filename (e.g., BadApple.mp4): ").strip()
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

width, height = 128, 64
frames_data = []
frame_count = 0
skip_frames = 3  # Export every 3rd frame to save flash space

print("Processing frames...")
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    if frame_count % skip_frames == 0:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        resized = cv2.resize(gray, (width, height))
        
        frame_bytes = []
        for h in range(height):
            byte = 0
            for w in range(width):
                pixel = 1 if resized[h, w] > 127 else 0
                byte = (byte << 1) | pixel
                if (w + 1) % 8 == 0:
                    frame_bytes.append(byte)
                    byte = 0
        frames_data.append(frame_bytes)
    
    frame_count += 1

cap.release()

total_saved_frames = len(frames_data)
with open("byteStream.h", "w") as f:
    f.write(f"#ifndef BYTE_STREAM_H\n#define BYTE_STREAM_H\n\n")
    f.write(f"const int totalFrames = {total_saved_frames};\n")
    f.write(f"const unsigned char byteStream[][1024] = {{\n")
    for frame in frames_data:
        f.write("  {")
        f.write(", ".join(f"0x{b:02x}" for b in frame))
        f.write("},\n")
    f.write("};\n\n#endif\n")

print(f"Successfully generated lightweight byteStream.h with {total_saved_frames} frames!")
import cv2
import os
import time

# Create directory for captured images if it doesn't exist
output_dir = "data"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create subdirectories for different classes (modify as needed)
classes = [0,1,2]  # Replace with your actual class names
for class_name in classes:
    class_dir = os.path.join(output_dir, str(class_name))
    if not os.path.exists(class_dir):
        os.makedirs(class_dir)

# Initialize webcam
cap = cv2.VideoCapture(0)  # 0 is usually the default camera

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Set camera resolution (optional)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

print("Image capture instructions:")
print("1. Press '0', '1', or '2' to save image to 0, 1, 2 respectively")
print("2. Press 'q' to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break
    
    # Display the live feed
    cv2.imshow('Webcam Feed - Press 0/1/2 to save, q to quit', frame)
    
    # Check for key presses
    key = cv2.waitKey(1) & 0xFF
    
    # Save images based on key press
    if key in [ord('0'), ord('1'), ord('2')]:
        class_idx = key - ord('0')  # 0, 1, or 2
        class_name = classes[class_idx]
        
        # Generate timestamp for unique filename
        timestamp = int(time.time() * 1000)
        filename = f"{class_name}_{timestamp}.jpg"
        filepath = os.path.join(output_dir, str(class_name), filename)
        
        # Save the image
        cv2.imwrite(filepath, frame)
        print(f"Saved image to: {filepath}")
    
    # Quit if 'q' is pressed
    elif key == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
print("Image capture completed.")
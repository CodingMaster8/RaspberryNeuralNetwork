from picamera2 import Picamera2
from time import sleep
import keyboard

# Initialize the camera
camera = Picamera2()
config = camera.create_still_configuration(main={"size": (800, 600)})
camera.configure(config)

# Start the camera
camera.start()
sleep(2)  # Allow the camera to warm up

print("Press 'space' to capture an image, 'q' to quit...")

# Initialize image counter
image_counter = 1

try:
    while True:
        if keyboard.is_pressed('space'):
            image_filename = f'/home/admin/Imágenes/image_{image_counter}.jpg'
            print(f"Capturing image {image_counter}...")
            camera.capture_file(image_filename)
            print(f"Image captured and saved to {image_filename}")
            image_counter += 1
            # Debounce the space key press
            while keyboard.is_pressed('space'):
                sleep(0.1)
        elif keyboard.is_pressed('q'):
            print("Quitting...")
            break
        sleep(0.1)
finally:
    # Stop the camera
    camera.stop()
    camera.close()
import cv2

# Initialize webcam
cap = cv2.VideoCapture(0)

# Set to keep track of image names
used_names = set()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # Wait for user input to set image name
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('s'):
        while True:
            # Ask user to input image name
            img_name = input("Enter image name: ")

            # Check if name already used
            if img_name in used_names:
                print("Name already used. Please enter a new name.")
            else:
                used_names.add(img_name)
                break

        # Save image
        cv2.imwrite(img_name + '.jpg', frame)

        # Read saved image to verify if it's proper
        img = cv2.imread(img_name + '.jpg')
        if img is None:
            print("Error: Failed to read image.")
            # Remove name from used_names set
            used_names.remove(img_name)
            continue

        # If image is not proper, ask user to capture again
        cv2.imshow('image', img)
        key2 = cv2.waitKey(0) & 0xFF
        if key2 == ord('c'):
            # Remove name from used_names set
            used_names.remove(img_name)
            continue
        else:
            used_names.add(img_name) # Add the image name to used_names set since it was saved successfully
            break

# Release the capture
cap.release()
cv2.destroyAllWindows()

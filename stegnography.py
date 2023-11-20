import cv2
import os

# Read the image (replace "test.jpg" with the correct image path)
img = cv2.imread("test.jpg")

# Get the shape of the image
height, width, channels = img.shape

# Flatten the image array to a 1D array
flat_img = img.flatten()

# Convert the pixel values to a string
pixel_values_str = ",".join(map(str, flat_img))

# Encryption
msg = input("Enter secret message:")
password = input("Enter a passcode:")

d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

encrypted_pixels = []

for i in range(len(msg)):
    encrypted_pixels.append(d[msg[i]])

# Replace the pixel values in the flattened image
for i in range(len(encrypted_pixels)):
    flat_img[i] = encrypted_pixels[i]

# Reshape the array back to the original image shape
encrypted_img = flat_img.reshape(height, width, channels)

# Save the encrypted image
cv2.imwrite("encryptedImage.jpg", encrypted_img)
os.system("start encryptedImage.jpg")  # Use 'start' to open the image on Windows

# Decryption
message = ""
n = 0
m = 0
z = 0

pas = input("Enter passcode for Decryption:")
if password == pas:
    decrypted_pixels = []

    # Replace the pixel values in the flattened image
    for i in range(len(msg)):
        decrypted_pixels.append(c[flat_img[i]])

    # Reshape the array back to the original image shape
    decrypted_img = flat_img.reshape(height, width, channels)

    # Save the decrypted image
    cv2.imwrite("decryptedImage.jpg", decrypted_img)
    os.system("start decryptedImage.jpg")  # Use 'start' to open the image on Windows

    for i in range(len(msg)):
        message = message + c[flat_img[i]]
else:
    print("YOU ARE NOT authorized")

print("Decryption message:", message)

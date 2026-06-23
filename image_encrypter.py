from PIL import Image

def encrypt_image(image_path):
    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            pixels[x, y] = (255-r, 255-g, 255-b)

    img.save("encrypted_image.png")
    print("Image encrypted successfully!")
    print("Saved as: encrypted_image.png")


def decrypt_image(image_path):
    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            pixels[x, y] = (255-r, 255-g, 255-b)

    img.save("decrypted_image.png")
    print("Image decrypted successfully!")
    print("Saved as: decrypted_image.png")


while True:
    print("\n===== Image Encryption Tool =====")
    print("1. Encrypt Image")
    print("2. Decrypt Image")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        filename = input("Enter image filename: ")
        encrypt_image(filename)

    elif choice == "2":
        filename = input("Enter image filename: ")
        decrypt_image(filename)

    elif choice == "3":
        print("Thank you for using Image Encryption Tool.")
        break

    else:
        print("Invalid choice!")
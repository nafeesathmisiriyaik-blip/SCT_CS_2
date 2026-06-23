# Image Encryption Tool

## Description
A Python-based image encryption and decryption tool that uses pixel manipulation to secure images.

## Features
- Encrypts images by modifying pixel values
- Decrypts encrypted images
- User-friendly menu system
- Supports PNG and JPG images

## How It Works
The program inverts RGB pixel values using:

255 - pixel_value

Applying the same operation again restores the original image.

## How to Run

1. Install Pillow:

pip install pillow

2. Run the program:

python image_encryptor.py

3. Choose:
- Encrypt Image
- Decrypt Image

## Technology Used
- Python 3
- Pillow (PIL)

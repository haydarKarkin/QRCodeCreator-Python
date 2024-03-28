# QR Code Generation and Conversion Script

This Python script generates QR codes from a list of serial numbers and saves them as PPM files. It then converts the PPM files to PNG format. Follow these steps to use the script:

## Prerequisites

- Python installed on your system.
- Pillow library installed. You can install it using `pip`:
  ```bash
  pip install Pillow
  pip install qrcode

## Usage

1. **Download the Python Script**

   - Download the Python script provided in this repository (`script.py`).

2. **Prepare Serial Numbers**

   - Create a text file (e.g., `serial_numbers.txt`) containing a list of serial numbers, with one serial number per line.

     Example (serial_numbers.txt):
     ```
     ABC123
     XYZ456
     ...
     ```

3. **Run the Script**

   - Open a terminal or command prompt and navigate to the directory where the Python script is located.

   - Run the script with the following command:
     ```bash
     python script.py serial_numbers.txt output_folder
     ```

     - Replace `script.py` with the name of the Python script.
     - Replace `serial_numbers.txt` with the path to your input file containing serial numbers.
     - Replace `output_folder` with the name of the folder where you want to save the generated QR code images.

     Example:
     ```bash
     python script.py serial_numbers.txt QRCodeImages
     ```

4. **View QR Code Images**

   - The script will generate QR code images as PPM files in the specified output folder and then convert them to PNG format. You can find the converted PNG files in the same output folder.

     Example (QRCodeImages folder):
     ```
     ABC123.png
     XYZ456.png
     ...
     ```

5. **Finished**

   - You've successfully generated and converted QR code images using the Python script. You can now use these PNG files as needed.

Please note that you can customize the script further to meet your specific requirements or integrate it into your own projects.

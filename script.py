import os
import qrcode
from PIL import Image

def generate_qr_code(data, output_folder):
    qr = qrcode.QRCode(
        version=5,  # Version 5 corresponds to a 500x500 QR code
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=25,  # Increase box size for a larger QR code
        border=4,  # Add a border
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    ppm_file_path = os.path.join(output_folder, f"{os.path.basename(data)}.ppm")
    try:
        img.save(ppm_file_path)
    except Exception as e:
        print(f"Error saving PPM file for {data}: {e}")
        return

    # Convert PPM to PNG
    png_file_path = os.path.join(output_folder, f"{os.path.basename(data)}.png")
    try:
        Image.open(ppm_file_path).convert("RGB").save(png_file_path, "PNG")
    except Exception as e:
        print(f"Error converting PPM to PNG for {data}: {e}")
        return

    # Remove the PPM file
    try:
        os.remove(ppm_file_path)
    except Exception as e:
        print(f"Error removing PPM file for {data}: {e}")

def read_serial_numbers_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            rows = file.read().splitlines()
            return list(set(rows))  # Remove duplicates
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def generate_qr_codes_for_serial_numbers(serial_numbers, output_folder):
    total_count = len(serial_numbers)
    for index, serial in enumerate(serial_numbers, start=1):
        generate_qr_code(serial, output_folder)
        print(f"Generated QR code {index}/{total_count}: {serial}")

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <file-path> <output-folder>")
        sys.exit(1)

    input_file_path = sys.argv[1]
    output_folder = sys.argv[2]

    if not os.path.exists(output_folder):
        try:
            os.makedirs(output_folder)
        except Exception as e:
            print(f"Error creating output folder: {e}")
            sys.exit(1)

    serial_numbers = read_serial_numbers_from_file(input_file_path)
    if serial_numbers:
        print(f"TOTAL COUNT: {len(serial_numbers)}")
        generate_qr_codes_for_serial_numbers(serial_numbers, output_folder)

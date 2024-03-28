import os

# Get the directory path of the script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Define the starting and ending numbers for the URLs
start_number = 2501
end_number = 5000

# Specify the file path for the output file
output_file = os.path.join(script_dir, "urls.txt")

# Open the output file to write the URLs
with open(output_file, "w") as file:
    # Loop through the range of numbers and generate URLs
    for i in range(start_number, end_number + 1):
        url = f"https://SAMPLEURLHERE.com/{i}.pdf\n"
        file.write(url)

print(f"URLs generated and saved in: {output_file}")

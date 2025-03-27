import re

input_text = "+91 9580767236"
number = re.search(r"\d{10}$", input_text).group()
print(number)

f=open("one.txt","w")


import re

# Read the input from a file
with open("one.txt", "r") as file:
    input_text = file.read()

# Extract the phone number
number = re.search(r"\d{10}$", input_text)

# Print the extracted number if found
if number:
    print(number.group())
else:
    print("No valid phone number found.")
import re

# Read the input from the file
with open("one.txt", "r") as file:
    input_text = file.read()

# Extract the phone number
number = re.search(r"\d{10}$", input_text)

# Overwrite the file accordingly
with open("one.txt", "w") as file:
    if number:
        file.write(number.group())
        print("File updated with extracted number.")
    else:
        file.write(input_text)  # Retain original content if no valid number is found
        print("No valid phone number found. File remains unchanged.")


# output as a different file
import re

# Read the input from a file
with open("input.txt", "r") as file:
    input_text = file.read()

# Extract the phone number
number = re.search(r"\d{10}$", input_text)

# Write the extracted number to a new file
if number:
    with open("output.txt", "w") as file:
        file.write(number.group())
    print("Extracted number saved in output.txt")
else:
    print("No valid phone number found.")



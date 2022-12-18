import sys

# Prompt the user for input
text_to_remove = input("Enter the text to remove: ")

# Initialize a list to store the additional text strings
additional_texts = []

# Ask the user if they want to enter additional text to remove
additional_text = input("Would you like to enter additional text to remove? (y/n) ")

# Keep prompting the user for additional text until they answer "no"
while additional_text.lower() == "y":
  additional_text = input("Enter the additional text to remove: ")
  additional_texts.append(additional_text)
  additional_text = input("Would you like to enter additional text to remove? (y/n) ")

# Open the input file and output file
with open("input.txt", "r") as input_file, open("output.txt", "w") as output_file:
  # Get the number of lines in the input file
  num_lines = sum(1 for _ in input_file)
  input_file.seek(0)  # Reset the file cursor to the beginning of the file

  # Initialize a counter and a progress bar
  counter = 0
  progress_bar = "Progress: ["
  progress_bar += "-" * 50
  progress_bar += "]"

  # Iterate over the lines in the input file
  for line in input_file:
    # If the line does not contain any of the text strings, write it to the output file
    if all(text not in line for text in [text_to_remove] + additional_texts):
      output_file.write(line)

    # Update the progress bar
    counter += 1
    progress = int(counter / num_lines * 50)
    progress_bar = progress_bar[:10] + "=" * progress + "-" * (50 - progress) + progress_bar[60:]
    sys.stdout.write("\r" + progress_bar)
    sys.stdout.flush()

print("\nDone!")
import os
import GPTTextModel
import Utils

# Read config file:
config = Utils.load_config('config.json')

# Declaring variables:
file_path = config['file_path']
prompt_text = config['prompt_text']
buffer = config['buffer']

# Create file:
if not os.path.exists(file_path):
    Utils.create_file(file_path)

# Read file:
inputText = Utils.read_file(file_path)

# Initialize prompt file:
if (len(inputText) == 0):
    Utils.write_file(file_path, prompt_text)
    inputText = prompt_text

# Generate text:
content_to_append = GPTTextModel.generate_text(inputText, buffer)

# Append new text to file:
Utils.write_file(file_path, content_to_append)
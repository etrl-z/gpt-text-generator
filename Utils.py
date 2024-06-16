import json

# Load configuration from JSON file
def load_config(config_file):
    with open(config_file, 'r') as f:
        config = json.load(f)
    return config

def read_file(file_path):
    with open(file_path, 'r') as file:
        # Read the entire file content into a string
        file_content = file.read()
        return file_content
    
def write_file(file_path, content_to_append):
    # Open the file in append mode ('a')
    with open(file_path, 'a') as file:
        # Write content to the file
        file.write(content_to_append + "\n")
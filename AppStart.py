import GPTTextModel
import Utils

# Read config file:
config = Utils.load_config('config.json')
file_path = config['file_path']

# Read file:
inputText = Utils.read_file(file_path)
# Generate text:
content_to_append = GPTTextModel.generate_text(inputText)
# Append text to file:
Utils.write_file(file_path, content_to_append)
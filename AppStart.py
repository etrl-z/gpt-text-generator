import GPTTextModel
import Utils

# Read config file:
config = Utils.load_config('config.json')
file_path = config['file_path']
prompt_text = config['prompt_text']
force_prompt = config['force_prompt']
buffer = config['buffer']

# Read file:
inputText = Utils.read_file(file_path)

if (len(inputText) == 0 or force_prompt):
    Utils.write_file(file_path, prompt_text)
    inputText = prompt_text

# Generate text:
content_to_append = GPTTextModel.generate_text(inputText, buffer)
# Append text to file:
Utils.write_file(file_path, content_to_append)
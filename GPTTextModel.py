from transformers import GPT2LMHeadModel, GPT2Tokenizer

def generate_text(input_text, buffer):
    # Load pre-trained model and tokenizer
    model_name = 'gpt2'
    model = GPT2LMHeadModel.from_pretrained(model_name)
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)

    # Define input text length
    text_length = len(input_text)
    maxLength = text_length + buffer

    # Encode input text
    input_ids = tokenizer.encode(input_text, return_tensors='pt')

    # Generate text based on input
    output = model.generate(input_ids, max_length=maxLength, num_return_sequences=1, no_repeat_ngram_size=2, top_k=50)

    # Decode and print generated text
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

    text_to_append = generated_text.replace(input_text, "")

    return text_to_append

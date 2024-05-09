from transformers import MarianMTModel, MarianTokenizer

# Specify the model name
model_name = 'Helsinki-NLP/opus-mt-en-mul'

# Load the tokenizer
tokenizer = MarianTokenizer.from_pretrained(model_name)

# Load the model
model = MarianMTModel.from_pretrained(model_name)
model.save_pretrained("model")
tokenizer.save_pretrained("tokenizer")
# Define the text to translate
text = '>>ara<< Hello, how are you?'

# Tokenize the text
input_ids = tokenizer.encode(text, return_tensors='pt')

# Generate the translation
outputs = model.generate(input_ids)
translation = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(translation)
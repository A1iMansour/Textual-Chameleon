from transformers import T5Tokenizer, T5ForConditionalGeneration

def translate(lang ,input):

    model_name = "t5-base"
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name)
    text = f"translate English to {lang} and keep placeholder:( "
    # Define the text to translate
    for n in input:
       text+="|||" +n 
    

    # Tokenize the text
    input_ids = tokenizer.encode(text, return_tensors="pt")

    # Generate the translation
    outputs = model.generate(input_ids,max_length=50)
    translation = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return translation

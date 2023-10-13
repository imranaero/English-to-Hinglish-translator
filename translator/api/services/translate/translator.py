from loguru import logger
from transformers import MarianMTModel, MarianTokenizer

model_name = "Helsinki-NLP/opus-mt-en-hi"
model = MarianMTModel.from_pretrained(model_name)
tokenizer = MarianTokenizer.from_pretrained(model_name)


async def translator(text: str):
    logger.info("Inside translate function")
    words = text.split()
    translated_words = []
    for i, word in enumerate(words):
        if i % 2 == 0:
            input_ids = tokenizer.encode(word, return_tensors="pt")
            translated_output = model.generate(input_ids, max_length=50,
                                               num_beams=5,
                                               no_repeat_ngram_size=2)
            translated_word = tokenizer.decode(translated_output[0],
                                               skip_special_tokens=True)
        else:
            translated_word = word
        translated_words.append(translated_word)
    translated_text = " ".join(translated_words)
    logger.info("output generated")
    return translated_text

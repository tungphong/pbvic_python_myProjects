import translators as ts

# Correct universal function call
text_to_translate = "Hello world"
translated = ts.translate_text(text_to_translate, translator='google', from_language='en', to_language='es')

print(translated)
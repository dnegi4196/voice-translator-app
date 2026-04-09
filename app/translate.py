from googletrans import Translator

translator = Translator()

def translate_text(text):
    result = translator.translate(text, src="ja", dest="en")
    return result.text

from googletrans import Translator
import asyncio

translator = Translator()

def distance(x, y):
    return (x**2 + y**2) ** 0.5

def language(code):
    from googletrans import LANGUAGES
    code = code.lower()
    name = LANGUAGES.get(code)
    if name is None:   # якщо мова некоректна
        return "Українська"
    return name.capitalize()

def translate_text(text, lang):
    try:
        result = translator.translate(text, dest=lang)

        if asyncio.iscoroutine(result):
            result = asyncio.run(result)

        return result.text
    except:
        return text
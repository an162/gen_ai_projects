from flask import Flask, render_template, request
from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer

app = Flask(__name__)

# Load the M2M100 model and tokenizer
model_name = "facebook/m2m100_418M"
tokenizer = M2M100Tokenizer.from_pretrained(model_name)
model = M2M100ForConditionalGeneration.from_pretrained(model_name)

language_codes = {
    "af": "af",    # Afrikaans
    "am": "am",    # Amharic
    "ar": "ar",    # Arabic
    "as": "as",    # Assamese
    "az": "az",    # Azerbaijani
    "be": "be",    # Belarusian
    "bg": "bg",    # Bulgarian
    "bn": "bn",    # Bengali
    "bs": "bs",    # Bosnian
    "ca": "ca",    # Catalan
    "ceb": "ceb",  # Cebuano
    "cs": "cs",    # Czech
    "cy": "cy",    # Welsh
    "da": "da",    # Danish
    "de": "de",    # German
    "el": "el",    # Greek
    "en": "en",    # English
    "es": "es",    # Spanish
    "et": "et",    # Estonian
    "eu": "eu",    # Basque
    "fa": "fa",    # Persian
    "fi": "fi",    # Finnish
    "fr": "fr",    # French
    "gl": "gl",    # Galician
    "gu": "gu",    # Gujarati
    "ha": "ha",    # Hausa
    "he": "he",    # Hebrew
    "hi": "hi",    # Hindi
    "hr": "hr",    # Croatian
    "hu": "hu",    # Hungarian
    "hy": "hy",    # Armenian
    "id": "id",    # Indonesian
    "ig": "ig",    # Igbo
    "is": "is",    # Icelandic
    "it": "it",    # Italian
    "ja": "ja",    # Japanese
    "jv": "jv",    # Javanese
    "ka": "ka",    # Georgian
    "kk": "kk",    # Kazakh
    "km": "km",    # Khmer
    "kn": "kn",    # Kannada
    "ko": "ko",    # Korean
    "lo": "lo",    # Lao
    "lt": "lt",    # Lithuanian
    "lv": "lv",    # Latvian
    "mg": "mg",    # Malagasy
    "mk": "mk",    # Macedonian
    "ml": "ml",    # Malayalam
    "mn": "mn",    # Mongolian
    "mr": "mr",    # Marathi
    "ms": "ms",    # Malay
    "my": "my",    # Burmese
    "ne": "ne",    # Nepali
    "nl": "nl",    # Dutch
    "no": "no",    # Norwegian
    "om": "om",    # Oromo
    "or": "or",    # Odia (Oriya)
    "pa": "pa",    # Punjabi
    "pl": "pl",    # Polish
    "ps": "ps",    # Pashto
    "pt": "pt",    # Portuguese
    "ro": "ro",    # Romanian
    "ru": "ru",    # Russian
    "sd": "sd",    # Sindhi
    "si": "si",    # Sinhala
    "sk": "sk",    # Slovak
    "sl": "sl",    # Slovenian
    "so": "so",    # Somali
    "sq": "sq",    # Albanian
    "sr": "sr",    # Serbian
    "su": "su",    # Sundanese
    "sv": "sv",    # Swedish
    "sw": "sw",    # Swahili
    "ta": "ta",    # Tamil
    "te": "te",    # Telugu
    "tg": "tg",    # Tajik
    "th": "th",    # Thai
    "tr": "tr",    # Turkish
    "uk": "uk",    # Ukrainian
    "ur": "ur",    # Urdu
    "uz": "uz",    # Uzbek
    "vi": "vi",    # Vietnamese
    "xh": "xh",    # Xhosa
    "yi": "yi",    # Yiddish
    "yo": "yo",    # Yoruba
    "zh": "zh",    # Chinese (Simplified)
    "zu": "zu",    # Zulu
}

def translate(text, src_lang, tgt_lang):
    tokenizer.src_lang = src_lang
    encoded_text = tokenizer(text, return_tensors="pt")
    generated_tokens = model.generate(**encoded_text, forced_bos_token_id=tokenizer.get_lang_id(tgt_lang))
    translated_text = tokenizer.decode(generated_tokens[0], skip_special_tokens=True)
    return translated_text

@app.route("/", methods=["GET", "POST"])
def index():
    translated_text = ""
    if request.method == "POST":
        source_text = request.form["source_text"]
        src_lang = request.form["src_lang"]
        tgt_lang = request.form["tgt_lang"]
        translated_text = translate(source_text, src_lang, tgt_lang)

    return render_template("index.html", languages=language_codes, translated_text=translated_text)

if __name__ == "__main__":
    app.run(debug=True)

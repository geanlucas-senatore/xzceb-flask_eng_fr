from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    text_translated_fr = translator.english_to_french(textToTranslate)
    # Write your code here
    return f"Translated text to French is: {text_translated_fr}"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    text_translated_en = translator.french_to_english(textToTranslate) 
    # Write your code here
    return f"Translated text to English is: {text_translated_en}"

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

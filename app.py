from flask import Flask, render_template, request, redirect, jsonify
from googletrans import Translator
from gtts import gTTS
import fitz
import os


app = Flask(__name__)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


app.config['UPLOAD_FOLDER'] = 'static'

LANGUAGES = {
    'en': 'English',
    'id': 'Indonesian',
    'af': 'Afrikaans',
    'sq': 'Albanian',
    'ar': 'Arabic',
    'be': 'Belarusian',
    'bg': 'Bulgarian',
    'ca': 'Catalan',
    'zh-CN': 'Chinese_simplified',
    'zh-TW': 'Chinese_traditional',
    'hr': 'Croatian',
    'cs': 'Czech',
    'da': 'Danish',
    'nl': 'Dutch',
    'eo': 'Esperanto',
    'et': 'Estonian',
    'tl': 'Filipino',
    'fi': 'Finnish',
    'fr': 'French',
    'gl': 'Galician',
    'de': 'German',
    'el': 'Greek',
    'iw': 'Hebrew',
    'hi': 'Hindi',
    'hu': 'Hungarian',
    'is': 'Icelandic',
    'ga': 'Irish',
    'it': 'Italian',
    'ja': 'Japanese',
    'ko': 'Korean',
    'la': 'Latin',
    'lv': 'Latvian',
    'lt': 'Lithuanian',
    'mk': 'Macedonian',
    'ms': 'Malay',
    'mt': 'Maltese',
    'no': 'Norwegian',
    'fa': 'Persian',
    'pl': 'Polish',
    'pt': 'Portuguese',
    'ro': 'Romanian',
    'ru': 'Russian',
    'sr': 'Serbian',
    'sk': 'Slovak',
    'sl': 'Slovenian',
    'es': 'Spanish',
    'sw': 'Swahili',
    'sv': 'Swedish',
    'th': 'Thai',
    'tr': 'Turkish',
    'uk': 'Ukrainian',
    'vi': 'Vietnamese',
    'cy': 'Welsh',
    'yi': 'Yiddish',
  }

@app.route("/", methods=['GET','POST'])
def index():

    if request.method == "POST":

        pdf_file = request.files['pdf_file']
        new_filename = "pdf-file-upload.pdf"

        pdf_file.save(os.path.join(app.config['UPLOAD_FOLDER'], new_filename))

        doc = fitz.open('static/pdf-file-upload.pdf')

        # Konversi file PDF menjadi HTML
        for page in doc:
            html = page.get_text("html")
            with open('static/html-file-upload.html', 'a', encoding='utf-8') as f:
                f.write(html)

        return redirect('/upload')
    else:
        file_path_pdf = os.path.join(app.config['UPLOAD_FOLDER'], 'pdf-file-upload.pdf' )
        file_path_html = os.path.join(app.config['UPLOAD_FOLDER'], 'html-file-upload.html' )

        if os.path.exists(file_path_pdf):
            os.remove(file_path_pdf)

        if os.path.exists(file_path_html):
            os.remove(file_path_html)

        return render_template("index.html")


@app.route("/upload", methods=['GET','POST'])
def upload():

    if request.method == "POST":

        data = request.get_json()
        text_input = data.get('text_input')
        lang = data.get('lang')
        count = data.get('count')

        # merubah bahasa teks
        translator = Translator()
        text = text_input
        translated = translator.translate(text, dest=lang).text
        print(translated)

        # convert text-input menjadi audio
        text = translated
        tts = gTTS(text=text, lang=lang)
        tts.save(f'static/{count}-mp3-file-upload.mp3')

        # Contoh: Kirim balik tanggapan sebagai confermation
        response = {'message': 'Data berhasil diterima dan diproses di server'}
        print(jsonify(response))

        location_audio = "static"
        name_audio = "-mp3-file-upload.mp3"

        response = {'translated': translated, 'location_audio': location_audio, 'name_audio': name_audio}
        return jsonify(response)
    else:

        return render_template("upload.html", code_language=LANGUAGES)
from flask import Flask, render_template, jsonify
from wonderwords import RandomWord
from words import app  # Import the Flask app instance from the package

rw = RandomWord()

header = {
    'Authorization': "kiwel11dvz8vz90zygypvmxpnbdhjykzvsevxunx4wa45cliletrjt6mlyfx3xf8"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_words', methods=['POST'])
def generate_words():
    word1 = rw.word()
    word2 = rw.word()
    return jsonify({'word1': word1, 'word2': word2})

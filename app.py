from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# OpenAI API anahtarınızı buraya ekleyin
openai.api_key = 'sk-50a7amgbPuVC5b0UGfiNsnk1NVZZceYMp916RY4vcyT3BlbkFJSkO41AYB_33CTNrysmOKysnYLfAtYZ5pkYCewvFpYA'

# Ana Sayfa Rotası
@app.route('/')
def index():
    return render_template('index.html')

# Rüya Yorumlama Rotası
@app.route('/ruya_yorumu', methods=['POST'])
def ruya_yorumu():
    data = request.get_json()
    dream = data['dream']

    # OpenAI API ile rüya yorumu oluşturma (Türkçe)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Sen, psikoloji ve mitoloji bilgisi olan bir rüya yorumcususun."},
            {"role": "user", "content": f"Şu rüyayı yorumla: {dream}"}
        ],
        max_tokens=500
    )

    dream_interpretation = response['choices'][0]['message']['content'].strip()

    return jsonify({"interpretation": dream_interpretation})

if __name__ == '__main__':
    app.run(debug=True)

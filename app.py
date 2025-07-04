from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form.get('url')
    if "instagram.com" not in url:
        return "❌ Invalid Instagram URL"
    
    # 👉 यहाँ आप इंस्टा डाउनलोड स्क्रिप्ट जोड़ सकते हो
    return f"✅ प्रोसेस किया गया: {url}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

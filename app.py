from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form.get('url')
    if "instagram.com" not in url:
        return "❌ Invalid URL"
    return f"✅ प्रोसेस किया गया: {url}"

if __name__ == '__main__':
    app.run()

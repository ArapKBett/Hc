from flask import Flask, request, render_template
import requests
import json

app = Flask(__name__)

# hCaptcha secret key
HCAPTCHA_SECRET = 'YOUR_SECRET_KEY'  # Replace with your hCaptcha secret key

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')
    email = request.form.get('email')
    hcaptcha_response = request.form.get('h-captcha-response')

    # Verify hCaptcha token
    verify_url = 'https://api.hcaptcha.com/siteverify'
    payload = {
        'secret': HCAPTCHA_SECRET,
        'response': hcaptcha_response,
        'remoteip': request.remote_addr
    }
    response = requests.post(verify_url, data=payload)
    result = response.json()

    if result.get('success'):
        return render_template('success.html', username=username, email=email)
    else:
        return render_template('error.html'), 400

@app.route('/log-fingerprint', methods=['POST'])
def log_fingerprint():
    fingerprint = request.json
    print('Received Fingerprint:', fingerprint)
    return {'status': 'Fingerprint logged'}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

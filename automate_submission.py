import requests
import random
from fingerprint import generate_fingerprint, log_fingerprint
'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def get_real_hcaptcha_token():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('http://localhost:5000')
    time.sleep(10)  # Wait for manual hCaptcha solving
    token = driver.execute_script("return hcaptcha.getResponse();")
    driver.quit()
    return token
'''

def get_mock_hcaptcha_token():
    # For demo purposes, return a placeholder token
    return 'mock-hcaptcha-token-' + str(random.randint(1000, 9999))

def automate_submission(num_attempts=3):
    url = 'http://localhost:5000/submit'
    for i in range(num_attempts):
        # Generate dynamic fingerprint
        fingerprint = generate_fingerprint()
        log_fingerprint(fingerprint)

        # Prepare form data
        form_data = {
            'username': f'user_{i}_{random.randint(100, 999)}',
            'email': f'user{i}@example.com',
            'h-captcha-response': get_mock_hcaptcha_token()  # Replace with get_real_hcaptcha_token() for Selenium
        }

        # Set headers with dynamic User-Agent
        headers = {
            'User-Agent': fingerprint['userAgent'],
            'Accept-Language': fingerprint['language']
        }

        # Send POST request
        try:
            response = requests.post(url, data=form_data, headers=headers)
            print(f'Attempt {i+1}: Status {response.status_code}')
            if response.status_code == 200:
                print('Success:', response.text[:100], '...')
            else:
                print('Error:', response.text[:100], '...')
        except requests.RequestException as e:
            print(f'Attempt {i+1}: Failed with error {e}')

if __name__ == '__main__':
    automate_submission(num_attempts=3)

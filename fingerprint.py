import random
import json

def generate_fingerprint():
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15',
    ]
    fingerprint = {
        'userAgent': random.choice(user_agents),
        'screen': {
            'width': random.choice([1920, 1366, 1440]),
            'height': random.choice([1080, 768, 900]),
            'colorDepth': 24
        },
        'timezone': random.choice(['America/New_York', 'Europe/London']),
        'language': random.choice(['en-US', 'en-GB'])
    }
    return fingerprint

def log_fingerprint():
    fingerprint = generate_fingerprint()
    with open('fingerprint_log.json', 'a') as f:
        json.dump(fingerprint, f)
        f.write('\n')
    print('Generated Fingerprint:', fingerprint)

if __name__ == '__main__':
    log_fingerprint()

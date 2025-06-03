import random
import json

def generate_fingerprint():
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    ]
    screen_resolutions = [(1920, 1080), (1366, 768), (1440, 900), (1280, 720)]
    timezones = ['America/New_York', 'Europe/London', 'Asia/Tokyo']
    languages = ['en-US', 'en-GB', 'fr-FR']
    
    width, height = random.choice(screen_resolutions)
    fingerprint = {
        'userAgent': random.choice(user_agents),
        'screen': {
            'width': width,
            'height': height,
            'colorDepth': random.choice([16, 24, 32])
        },
        'timezone': random.choice(timezones),
        'language': random.choice(languages),
        'webgl': random.choice(['WebKit', 'ANGLE', 'Not supported'])
    }
    return fingerprint

def log_fingerprint(fingerprint):
    with open('fingerprint_log.json', 'a') as f:
        json.dump(fingerprint, f)
        f.write('\n')
    print('Generated Fingerprint:', fingerprint)

if __name__ == '__main__':
    fingerprint = generate_fingerprint()
    log_fingerprint(fingerprint)

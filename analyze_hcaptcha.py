import requests
import re

def fetch_hcaptcha_script():
    url = 'https://newassets.hcaptcha.com/captcha/v1/123456/static/hcaptcha.html'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/91.0.4472.124'}
    response = requests.get(url, headers=headers)
    
    wasm_refs = re.findall(r'https://newassets\.hcaptcha\.com/[^"]+\.wasm', response.text)
    js_refs = re.findall(r'https://newassets\.hcaptcha\.com/[^"]+\.js', response.text)
    
    print('WebAssembly References:', wasm_refs)
    print('JavaScript References:', js_refs)
    
    if wasm_refs:
        wasm_url = wasm_refs[0]
        wasm_response = requests.get(wasm_url, headers=headers)
        with open('hcaptcha.wasm', 'wb') as f:
            f.write(wasm_response.content)
        print('Downloaded WebAssembly file for analysis.')

if __name__ == '__main__':
    fetch_hcaptcha_script()

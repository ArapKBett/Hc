document.addEventListener('DOMContentLoaded', function() {
    const fingerprint = {
        userAgent: navigator.userAgent,
        screen: {
            width: window.screen.width,
            height: window.screen.height,
            colorDepth: window.screen.colorDepth
        },
        timezone: Intl.DateTimeFormat().resolvedOptions().timeZone,
        language: navigator.language,
        webgl: (function() {
            try {
                const canvas = document.createElement('canvas');
                const gl = canvas.getContext('webgl');
                return gl ? gl.getParameter(gl.VENDOR) : 'Not supported';
            } catch (e) {
                return 'Error: ' + e.message;
            }
        })()
    };
    console.log('Browser Fingerprint:', fingerprint);

    fetch('/log-fingerprint', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(fingerprint)
    }).then(response => response.json())
      .then(data => console.log('Fingerprint logged:', data))
      .catch(error => console.error('Error logging fingerprint:', error));
});

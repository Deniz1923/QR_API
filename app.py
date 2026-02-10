from flask import Flask, request, send_file
import qrcode
import io

app = Flask(__name__)

# --- NEW: Route for the Homepage ---
@app.route('/')
def home():
    # When user visits root URL, send them the HTML file
    return send_file('index.html')

# --- EXISTING: Route for the API ---
@app.route('/api/qr', methods=['GET'])
def generate_qr():
    url = request.args.get('url')
    
    if not url:
        return {"error": "Missing URL parameter"}, 400

    img = qrcode.make(url)
    
    buf = io.BytesIO()
    img.save(buf)
    buf.seek(0)
    
    return send_file(buf, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
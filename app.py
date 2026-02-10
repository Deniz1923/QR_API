from flask import Flask, request, send_file
import qrcode
import io

app = Flask(__name__)

@app.route('/api/qr', methods=['GET'])
def generate_qr():
    # 1. Get the data from the URL (e.g. ?url=google.com)
    data = request.args.get('url')

    # Check if the user forgot to send a URL
    if not data:
        return {"error": "Please provide a url! Example: /api/qr?url=google.com"}, 400

    # 2. Generate the QR Code
    img = qrcode.make(data)

    # 3. Save the image to "memory" (RAM) instead of a file
    # Think of this as a virtual file that only exists for a second
    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0) # Reset the file pointer to the beginning

    # 4. Send the image back to the user
    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
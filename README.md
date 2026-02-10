# QR Code Generator API

A simple, serverless QR code generator built with Python (Flask) and deployed on Vercel.

You can try at https://simple-qr-gen-api-67.vercel.app/
## 🚀 Features
- **Web Interface:** A clean, user-friendly frontend to generate QR codes instantly.
- **API Endpoint:** A direct API (`/api/qr`) for developers to integrate QR generation into their own apps.
- **Serverless:** Designed to run on Vercel or any standard Python environment.
- **Fast:** Powered by `uv` for dependency management.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Framework:** Flask
- **Libraries:** `qrcode`, `Pillow`
- **Package Manager:** `uv`
- **Hosting:** Vercel

## 📂 Project Structure
```text
.
├── app.py              # Main application logic (API + Frontend serving)
├── index.html          # The frontend user interface
├── pyproject.toml      # Dependency definitions (managed by uv)
├── requirements.txt    # Exported dependencies for Vercel
└── vercel.json         # Configuration for Vercel deployment
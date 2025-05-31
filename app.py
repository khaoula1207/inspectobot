from flask import Flask, render_template_string
import os

app = Flask(__name__)

@app.route('/')
def home():
    iframe_url = "https://copilotstudio.microsoft.com/environments/Default-37921931-3dbf-4176-ba5b-bd16c6a70568/bots/crc0f_assistant_QTHcos/canvas?__version__=2&enableFileAttachment=true"
    html = f"""
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Inspectobot – BH Bank</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            background: #f6f6f6;
            font-family: 'Segoe UI', Arial, sans-serif;
        }}
        .header {{
            background: #0a2043;
            color: #d90429; /* red instead of gold */
            padding: 24px 0 12px 0;
            text-align: center;
            font-size: 2.7rem;
            font-weight: bold;
            letter-spacing: 1px;
            box-shadow: 0 4px 24px rgba(10,32,67,0.11);
        }}
        .subtitle {{
            color: #fff;
            font-size: 1.2rem;
            margin-top: 6px;
            margin-bottom: 18px;
        }}
        .container {{
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: flex-start;
            min-height: 80vh;
            padding: 4vw 1vw 2vw 1vw;
        }}
        .card {{
            background: #fff;
            border: 2px solid #d90429; /* red border instead of gold */
            border-radius: 20px;
            box-shadow: 0 8px 32px rgba(10,32,67,0.12);
            padding: 24px 24px 18px 24px;
            max-width: 480px;
            width: 100%;
            margin-top: 32px;
        }}
        .chatbot-iframe {{
            width: 100%;
            height: 68vh;
            min-height: 420px;
            border: none;
            border-radius: 12px;
            box-shadow: 0 2px 20px #d9042925; /* subtle red shadow */
            margin-top: 8px;
            background: #fff;
            transition: box-shadow 0.2s;
        }}
        .footer {{
            text-align: center;
            color: #222;
            margin-top: 34px;
            font-size: 1rem;
        }}
        @media (max-width: 600px) {{
            .card {{
                padding: 10px 2vw 8px 2vw;
                border-radius: 0;
                max-width: 99vw;
            }}
            .chatbot-iframe {{
                min-height: 330px;
                border-radius: 0;
            }}
            .header {{
                font-size: 1.5rem;
                padding: 12px 0 8px 0;
            }}
        }}
    </style>
</head>
<body>
    <div class="header">
        BH Bank Inspectobot
        <div class="subtitle">Assistant conversationnel pour les missions d’inspection</div>
    </div>
    <div class="container">
        <div class="card">
            <iframe
                class="chatbot-iframe"
                src="{iframe_url}"
                allow="clipboard-write; clipboard-read; encrypted-media;">
            </iframe>
        </div>
        <div class="footer">
            &copy; 2025 BH Bank Tunisie. Tous droits réservés.
        </div>
    </div>
</body>
</html>
"""

    return render_template_string(html)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)

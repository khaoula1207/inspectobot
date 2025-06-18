from flask import Flask, render_template_string
import os

app = Flask(__name__)

@app.route('/')
def home():
    iframe_url = "https://copilotstudio.microsoft.com/environments/Default-37921931-3dbf-4176-ba5b-bd16c6a70568/bots/crc0f_assistant/canvas?__version__=2&enableFileAttachment=true"
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
            background: linear-gradient(135deg, #f6f6f6 70%, #eaf0f6 100%);
            font-family: 'Segoe UI', Arial, sans-serif;
        }}
        .header {{
            background: #0a2043;
            color: #d90429;
            padding: 36px 0 12px 0;
            text-align: center;
            font-size: 2.8rem;
            font-weight: 800;
            letter-spacing: 1px;
            box-shadow: 0 4px 32px rgba(10,32,67,0.08);
            border-bottom-left-radius: 24px;
            border-bottom-right-radius: 24px;
        }}
        .subtitle {{
            color: #fff;
            font-size: 1.18rem;
            margin-top: 8px;
            margin-bottom: 18px;
            font-weight: 400;
            letter-spacing: .5px;
        }}
        .container {{
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: flex-start;
            min-height: 80vh;
            padding: 5vw 1vw 2vw 1vw;
        }}
        .card {{
            background: #fff;
            border: 2.5px solid #d90429;
            border-radius: 24px;
            box-shadow: 0 8px 36px 0 rgba(10,32,67,0.10), 0 1.5px 6px #d904291a;
            padding: 28px 32px 22px 32px;
            max-width: 520px;
            width: 100%;
            margin-top: 40px;
            display: flex;
            flex-direction: column;
            align-items: stretch;
            transition: box-shadow 0.3s;
        }}
        .card:hover {{
            box-shadow: 0 10px 50px 0 rgba(217,4,41,0.11), 0 4px 20px #0a204350;
        }}
        .chatbot-iframe {{
            width: 100%;
            height: 67vh;
            min-height: 370px;
            border: none;
            border-radius: 14px;
            box-shadow: 0 3px 28px #d9042924;
            margin-top: 8px;
            background: #fff;
            transition: box-shadow 0.18s;
        }}
        .footer {{
            text-align: center;
            color: #222;
            margin-top: 40px;
            margin-bottom: 24px;
            font-size: 1.05rem;
            opacity: 0.82;
        }}
        @media (max-width: 700px) {{
            .header {{
                font-size: 2rem;
                padding: 14px 0 7px 0;
                border-radius: 0;
            }}
            .subtitle {{
                font-size: 1rem;
            }}
            .card {{
                padding: 12px 3vw 9px 3vw;
                border-radius: 0;
                max-width: 100vw;
                margin-top: 14px;
            }}
            .chatbot-iframe {{
                min-height: 210px;
                border-radius: 0;
            }}
        }}
        @media (max-width: 400px) {{
            .header {{
                font-size: 1.1rem;
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

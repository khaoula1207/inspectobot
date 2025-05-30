from flask import Flask, render_template_string, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import datetime
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL',
    'postgresql://inspectobot_db_user:9QAeLY5zrTmRwOKuc0OX5b2MeYiH8Mi8@dpg-d0sf8249c44c73f4fr00-a/inspectobot_db'  
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class ChatLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(80))
    question = db.Column(db.Text)
    answer = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def home():
    iframe_url = "https://copilotstudio.microsoft.com/environments/Default-37921931-3dbf-4176-ba5b-bd16c6a70568/bots/crc0f_assistant_QTHcos/canvas?__version__=2&enableFileAttachment=true"
    html = f"""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Inspectobot</title>
        <style>
            body {{
                background: #eaf6fb;
                font-family: 'Segoe UI', Arial, sans-serif;
                margin: 0;
                padding: 0;
            }}
            .container {{
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: flex-start;
                min-height: 100vh;
                padding: 5vw 2vw 2vw 2vw;
            }}
            h1 {{
                margin-top: 2vw;
                text-align: center;
                font-size: 6vw;
                color: #222;
                letter-spacing: 1px;
            }}
            .chatbot-iframe {{
                width: 100%;
                max-width: 430px;
                height: 70vh;
                min-height: 420px;
                border: none;
                border-radius: 14px;
                box-shadow: 0 6px 32px #a2b5c6;
                background: white;
                margin-top: 6vw;
                transition: box-shadow 0.2s;
            }}
            .chatbot-iframe:focus {{
                box-shadow: 0 6px 38px #3476a4;
            }}
            @media (max-width: 600px) {{
                .container {{
                    padding: 2vw 0 0 0;
                }}
                .chatbot-iframe {{
                    width: 98vw;
                    min-width: 0;
                    height: 80vh;
                    min-height: 330px;
                    border-radius: 0;
                    margin-top: 3vw;
                }}
                h1 {{
                    font-size: 8vw;
                    margin-top: 4vw;
                }}
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <iframe
                class="chatbot-iframe"
                src="{iframe_url}"
                allow="clipboard-write; clipboard-read; encrypted-media;"
            ></iframe>
        </div>
    </body>
    </html>
    """
    return render_template_string(html)

@app.route('/api/log_conversation', methods=['POST'])
def log_conversation():
    data = request.json
    chat = ChatLog(
        user_id=data.get('user_id'),
        question=data.get('question'),
        answer=data.get('answer')
    )
    db.session.add(chat)
    db.session.commit()
    return jsonify({'status': 'logged'}), 201

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)

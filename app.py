#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install flask')


# In[2]:


from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    # Your Inspectobot Power Virtual Agent iframe URL
    iframe_url = "https://copilotstudio.microsoft.com/environments/Default-37921931-3dbf-4176-ba5b-bd16c6a70568/bots/crc0f_assistant_QTHcos/canvas?__version__=2&enableFileAttachment=true"
    html = f"""
    <html>
    <head>
        <title>Inspectobot</title>
        <style>
            body {{ background: #eaf6fb; font-family: Arial, sans-serif; }}
            h1 {{ text-align: center; color: #222; margin-top: 30px; }}
            .iframe-container {{
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 70vh;
            }}
            iframe {{
                border: none;
                border-radius: 10px;
                box-shadow: 0 4px 24px #aaa;
            }}
        </style>
    </head>
    <body>
        <h1>Bienvenue sur Inspectobot !</h1>
        <div class="iframe-container">
            <iframe src="{iframe_url}" width="400" height="600"></iframe>
        </div>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    # use_reloader=False is IMPORTANT if you are running in Jupyter
    app.run(port=8050, debug=True, use_reloader=False)


# In[ ]:





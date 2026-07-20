from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>FF ASH Tournament</title>
    </head>
    <body style="background:#111;color:#FFD700;text-align:center;font-family:Arial;">
        <h1>🎮 FF ASH Tournament</h1>
        <h2>به سایت رسمی تورنومنت خوش آمدید</h2>

        <h3>ثبت نام مسابقات</h3>

        <form>
            <input type="text" placeholder="نام بازیکن"><br><br>
            <input type="text" placeholder="UID فری فایر"><br><br>
            <button>ثبت نام</button>
        </form>

        <br>

        <h3>پشتیبانی</h3>
        <p>@IM_SHAH__1</p>
        <p>@MY_SHAYAN_1</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

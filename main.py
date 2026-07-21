from flask import Flask, request
import sqlite3

app = Flask(__name__)

# ساخت دیتابیس
def create_db():
    conn = sqlite3.connect("players.db")
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS players(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        uid TEXT,
        phone TEXT
    )
    """)
    conn.commit()
    conn.close()

create_db()


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":
        name = request.form["name"]
        uid = request.form["uid"]
        phone = request.form["phone"]

        conn = sqlite3.connect("players.db")
        c = conn.cursor()
        c.execute(
            "INSERT INTO players (name, uid, phone) VALUES (?,?,?)",
            (name, uid, phone)
        )
        conn.commit()
        conn.close()

        message = "✅ ثبت نام با موفقیت انجام شد"

    else:
        message = ""


    return f"""
<!DOCTYPE html>
<html>
<head>
<title>FF ASH Tournament</title>
<meta name="viewport" content="width=device-width, initial-scale=1">

<style>
body{{
background:#111;
color:white;
font-family:Arial;
text-align:center;
}}

.box{{
background:#1a1a1a;
margin:20px;
padding:20px;
border:2px solid #FFD700;
border-radius:15px;
}}

input{{
padding:12px;
margin:8px;
width:80%;
border-radius:8px;
}}

button{{
background:#FFD700;
padding:12px 25px;
border-radius:10px;
font-weight:bold;
}}
</style>

</head>

<body>

<h1 style="color:#FFD700">
🏆 FF ASH TOURNAMENT 🏆
</h1>


<div class="box">

<h2>📝 ثبت نام بازیکن</h2>

<form method="POST">

<input name="name" placeholder="نام بازیکن" required><br>

<input name="uid" placeholder="UID فری فایر" required><br>

<input name="phone" placeholder="شماره تماس" required><br>

<button>
ثبت نام
</button>

</form>

<p style="color:#FFD700">
{message}
</p>

</div>


<div class="box">
<h2>👑 FF ASH ADMIN</h2>
<p>Players Database Active</p>
</div>


</body>
</html>
"""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

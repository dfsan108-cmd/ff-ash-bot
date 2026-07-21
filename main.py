from flask import Flask, request, redirect, session
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "FF_ASH_SECRET_2026_KEY"

ADMIN_PASSWORD = "ASH_ADMIN_2026"


def db():
    conn = sqlite3.connect("players.db")
    return conn


def create_db():
    conn = db()
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS players(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        uid TEXT,
        phone TEXT,
        team TEXT,
        mode TEXT,
        receipt TEXT
    )
    """)

    conn.commit()
    conn.close()


create_db()



@app.route("/", methods=["GET","POST"])
def home():

    message=""

    if request.method=="POST":

        name=request.form["name"]
        uid=request.form["uid"]
        phone=request.form["phone"]
        team=request.form["team"]
        mode=request.form["mode"]
        receipt=request.form["receipt"]


        conn=db()
        c=conn.cursor()

        c.execute("""
        INSERT INTO players
        (name,uid,phone,team,mode,receipt)
        VALUES(?,?,?,?,?,?)
        """,
        (name,uid,phone,team,mode,receipt))


        conn.commit()
        conn.close()

        message="✅ ثبت نام موفق بود"



    return f"""

<html>
<head>
<title>FF ASH Tournament</title>
<meta name="viewport" content="width=device-width">

<style>

body{{
background:#111;
color:white;
font-family:Arial;
text-align:center;
}}

.box{{
background:#1b1b1b;
margin:20px;
padding:20px;
border:2px solid #FFD700;
border-radius:15px;
}}

input,select{{
width:80%;
padding:12px;
margin:8px;
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
🏆 FF ASH TOURNAMENT
</h1>


<div class="box">

<h2>📝 ثبت نام مسابقه</h2>


<form method="POST">


<input name="name" placeholder="نام بازیکن" required><br>

<input name="uid" placeholder="UID فری فایر" required><br>

<input name="phone" placeholder="شماره تماس" required><br>

<input name="team" placeholder="نام تیم"><br>


<select name="mode">

<option>Solo</option>
<option>Duo</option>
<option>Squad</option>

</select><br>


<input name="receipt" placeholder="لینک رسید پرداخت">


<br>

<button>
ثبت نام
</button>


</form>


<h3 style="color:#FFD700">
{message}
</h3>


</div>


</body>
</html>

"""





@app.route("/admin", methods=["GET","POST"])
def admin():


    if "admin" not in session:


        if request.method=="POST":

            if request.form["password"]==ADMIN_PASSWORD:

                session["admin"]=True

                return redirect("/admin")


        return """

<html>

<body style="background:#111;color:white;text-align:center">


<h2>👑 ASH ADMIN LOGIN</h2>


<form method="POST">

<input type="password" name="password" placeholder="رمز مدیریت">

<br><br>

<button>
ورود
</button>

</form>


</body>

</html>

"""



    conn=db()

    players=conn.cursor().execute(
    "SELECT * FROM players"
    ).fetchall()

    conn.close()



    html="""

<html>

<body style="background:#111;color:white;text-align:center">


<h1 style="color:#FFD700">
👑 ASH ADMIN PANEL
</h1>


<h3>
تعداد بازیکنان:
"""


    html+=str(len(players))


    html+="""

</h3>

"""


    for p in players:


        html+=f"""

<div style="
background:#1b1b1b;
border:2px solid #FFD700;
margin:15px;
padding:15px;
border-radius:15px;
">


نام: {p[1]} <br>
UID: {p[2]} <br>
شماره: {p[3]} <br>
تیم: {p

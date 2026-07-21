from flask import Flask, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "FFASH2026"

PASSWORD = "ASH2026"


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


@app.route("/", methods=["GET","POST"])
def home():

    msg=""

    if request.method=="POST":

        name=request.form["name"]
        uid=request.form["uid"]
        phone=request.form["phone"]

        conn=sqlite3.connect("players.db")
        c=conn.cursor()

        c.execute(
        "INSERT INTO players(name,uid,phone) VALUES(?,?,?)",
        (name,uid,phone)
        )

        conn.commit()
        conn.close()

        msg="✅ ثبت نام شد"


    return f"""

<html>

<body style="background:#111;color:white;text-align:center;font-family:Arial">

<h1 style="color:#FFD700">
🏆 FF ASH TOURNAMENT
</h1>


<form method="POST">

<input name="name" placeholder="نام بازیکن"><br><br>

<input name="uid" placeholder="UID"><br><br>

<input name="phone" placeholder="شماره تماس"><br><br>

<button>
ثبت نام
</button>

</form>


<h3 style="color:#FFD700">
{msg}
</h3>


</body>

</html>

"""



@app.route("/admin", methods=["GET","POST"])
def admin():

    if "admin" not in session:

        if request.method=="POST":

            if request.form["password"]==PASSWORD:
                session["admin"]=True
                return redirect("/admin")


        return """

<html>
<body style="background:#111;color:white;text-align:center">

<h2>👑 ADMIN LOGIN</h2>

<form method="POST">

<input type="password" name="password" placeholder="رمز">

<button>
ورود
</button>

</form>

</body>
</html>

"""


    conn=sqlite3.connect("players.db")
    players=conn.cursor().execute(
    "SELECT * FROM players"
    ).fetchall()

    conn.close()


    text=""


    for p in players:

        text+=f"""

<div

from flask import Flask, request, session, redirect
import sqlite3

app = Flask(__name__)
app.secret_key = "FFASH2026"

PASSWORD = "ASH2026"


def db():
    conn = sqlite3.connect("players.db")
    conn.execute("""
    CREATE TABLE IF NOT EXISTS players(
        id INTEGER PRIMARY KEY,
        name TEXT,
        uid TEXT,
        phone TEXT
    )
    """)
    return conn


@app.route("/", methods=["GET","POST"])
def home():

    msg = ""

    if request.method == "POST":
        conn = db()
        conn.execute(
            "INSERT INTO players(name,uid,phone) VALUES(?,?,?)",
            (
                request.form["name"],
                request.form["uid"],
                request.form["phone"]
            )
        )
        conn.commit()
        conn.close()
        msg = "ثبت نام شد ✅"


    return """
    <html>
    <body style="background:#111;color:white;text-align:center">

    <h1 style="color:#FFD700">
    🏆 FF ASH TOURNAMENT
    </h1>

    <form method="POST">

    <input name="name" placeholder="نام"><br>
    <input name="uid" placeholder="UID"><br>
    <input name="phone" placeholder="شماره"><br>

    <button>ثبت نام</button>

    </form>

    <h3 style="color:#FFD700">""" + msg + """

    </h3>

    </body>
    </html>
    """


@app.route("/admin", methods=["GET","POST"])
def admin():

    if "admin" not in session:

        if request.method=="POST":
            if request.form["password"] == PASSWORD:
                session["admin"] = True
                return redirect("/admin")

        return """
        <form method="POST">
        <input name="password" type="password">
        <button>ورود</button>
        </form>
        """


    conn=db()
    players=conn.execute(
        "SELECT * FROM players"
    ).fetchall()

    text="<h1>👑 ASH PANEL</h1>"

    for p in players:
        text += f"""
        <p>
        نام: {p[1]}<br>
        UID: {p[2]}<br>
        شماره: {p[3]}
        </p>
        <hr>
        """

    return text


if __name__=="__main__":
    app.run(host="0.0.0.0",port=10000)

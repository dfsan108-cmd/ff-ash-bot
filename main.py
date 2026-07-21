from flask import Flask, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "FFASH_SECRET_KEY"


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

    message = ""

    if request.method == "POST":
        name = request.form["name"]
        uid = request.form["uid"]
        phone = request.form["phone"]

        conn = sqlite3.connect("players.db")
        c = conn.cursor()
        c.execute(
            "INSERT INTO players(name,uid,phone) VALUES(?,?,?)",
            (name,uid,phone)
        )
        conn.commit()
        conn.close()

        message="✅ ثبت نام انجام شد"


    return f"""
    <html>
    <body style="background:#111;color:white;text-align:center;font-family:Arial">

    <h1 style="color:#FFD700">
    🏆 FF ASH TOURNAMENT
    </h1>

    <form method="POST">

    <input name="name" placeholder="نام بازیکن"><br><br>
    <input name="uid" placeholder="UID فری فایر"><br><br>
    <input name="phone" placeholder="شماره تماس"><br><br>

    <button style="background:#FFD700;padding:10px">
    ثبت نام
    </button>

    </form>

    <h3 style="color:#FFD700">{message}</h3>

    </body>
    </html>
    """


@app.route("/admin", methods=["GET","POST"])
def admin():

    if "admin" not in session:

        if request.method=="POST":

            if request.form["password"]=="ASH2026":
                session["admin"]=True
                return redirect("/admin")


        return """
        <html>
        <body style="background:#111;color:white;text-align:center">

        <h2>👑 ASH ADMIN LOGIN</h2>

        <form method="POST">
        <input name="password" type="password" placeholder="رمز">
        <button>ورود</button>
        </form>

        </body>
        </html>
        """


    conn=sqlite3.connect("players.db")
    c=conn.cursor()

    players=c.execute(
        "SELECT * FROM players"
    ).fetchall()

    conn.close()


    html="""
    <html>
    <body style="background:#111;color:white;text-align:center">

    <h1 style="color:#FFD700">
    👑 بازیکنان ثبت نام شده
    </h1>
    """


    for p in players:
        html += f"""
        <div style="border:2px solid #FFD700;margin:10px;padding:10px">
        نام: {p[1]}<br>
        UID: {p[2]}<br>
        شماره: {p[3]}
        </div>
        """


    html += "</body></html>"

    return html



if __name__=="__main__":
    app.run(host="0.0.0.0",port=10000)

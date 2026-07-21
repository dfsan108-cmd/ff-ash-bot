from flask import Flask, request, session, redirect
import sqlite3

app = Flask(__name__)
app.secret_key = "FFASH2026"
TOURNAMENT = {
    "time": "20:00",
    "price": "15,000 تومان",
    "first": ",110 جم",
    "second": ",30 هزار تومان",
    "third": "20 هزار تومان"
}
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

    conn.execute("""
    CREATE TABLE IF NOT EXISTS custom_players(
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
<head>
<title>FF ASH Tournament</title>

<meta name="viewport" content="width=device-width, initial-scale=1">

<meta name="google-site-verification" content="cbDP_66Gwq0JZuGfspUi8gMrnlVE0ubnS4UXj1st6p8" />

<style>

body{
background:#090909;
color:white;
font-family:Arial;
text-align:center;
margin:0;
}


.header{
padding:35px;
background:linear-gradient(90deg,#FFD700,#111);
color:black;
font-size:35px;
font-weight:bold;
}


.box{
background:#151515;
margin:20px;
padding:25px;
border-radius:20px;
border:2px solid #FFD700;
box-shadow:0 0 15px #FFD700;
}


h2{
color:#FFD700;
}


input,select{

width:80%;
padding:14px;
margin:8px;
border-radius:10px;
border:none;

}


button{

background:#FFD700;
color:black;
padding:15px 35px;
border-radius:15px;
border:none;
font-weight:bold;
font-size:16px;

}


button:hover{

background:white;

}


.card{

display:inline-block;
background:#222;
padding:20px;
margin:10px;
border-radius:15px;
border:1px solid #FFD700;

}


.gold{

color:#FFD700;

}


</style>

</head>


<body>


<div class="header">

🏆 FF ASH TOURNAMENT 🏆

</div>



<div class="box">

<h2>
🔥 بزرگترین تورنومنت فری فایر
</h2>

<p>
به مسابقات رسمی FF ASH خوش آمدید
</p>

<p class="gold">
جوایز ویژه برای برندگان 🥇
</p>

</div>



<div class="box">

<h2>
📊 آمار مسابقات
</h2>


<div class="card">
50+
<br>
بازیکن
</div>


<div class="card">
10+
<br>
مسابقه
</div>


<div class="card">
1000+
<br>
بازدید
</div>


</div>


<div class="box">


<h2>🏆 اطلاعات تورنومنت</h2>

<p>
⏰ ساعت برگزاری:
<br>
""" + TOURNAMENT["time"] + """
</p>

<p>
💰 هزینه ورود:
<br>
""" + TOURNAMENT["price"] + """
</p>

<p>
👥 ظرفیت مسابقه:
<br>
48 بازیکن
</p>

<p>
🥇 نفر اول:
<br>
""" + TOURNAMENT["first"] + """
</p>

<p>
🥈 نفر دوم:
<br>
""" + TOURNAMENT["second"] + """
</p>

<p>
🥉 نفر سوم:
<br>
""" + TOURNAMENT["third"] + """
</p>

</div>

<div class="box">


<h2>
📝 ثبت نام مسابقه
</h2>


<form method="POST">


<input name="name" placeholder="نام بازیکن" required>

<br>


<input name="uid" placeholder="UID فری فایر" required>

<br>


<input name="phone" placeholder="شماره تماس" required>

<br>


<button>
ثبت نام 🏆
</button>


</form>


</div>




<div class="box">


<h2>
📜 قوانین مسابقه
</h2>


<p>
✔ ورود با UID واقعی
</p>

<p>
✔ رعایت قوانین بازی
</p>

<p>
✔ تصمیم نهایی با مدیریت FF ASH
</p>


</div>




<div class="box">


<h2>
📞 پشتیبانی
</h2>


<p>
@IM_SHAH__1
</p>

<p>
@MY_SHAYAN_1
</p>


</div>




<div class="box">

<h2>
👑 مدیریت
</h2>

<p>
ASH ADMIN PANEL
</p>

</div>



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
    conn=db()

    players=conn.execute(
        "SELECT * FROM players"
    ).fetchall()

    custom_players=conn.execute(
        "SELECT * FROM custom_players"
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

    text += "<h2>🎮 شرکت کنندگان کاستوم</h2>"

    for c in custom_players:
        text += f"""
        <p>
        نام: {c[1]}<br>
        UID: {c[2]}<br>
        شماره: {c[3]}
        </p>
        <hr>
        """

    conn.close()

    return text

@app.route("/customs")
def customs():

    return """
    <html>
    <body style="background:#111;color:white;text-align:center;font-family:Arial">

    <h1 style="color:#FFD700">
    🎮 FF ASH CUSTOM ROOMS
    </h1>

    <div style="
    background:#1a1a1a;
    margin:20px;
    padding:20px;
    border:2px solid #FFD700;
    border-radius:15px;
    ">

    <h2>🏆 کاستوم شماره 1</h2>

    <p>👥 ظرفیت: 48 نفر</p>

    <p>💰 ورودی: 50,000 تومان</p>

    <p>⏰ ساعت: 20:00</p>

    <a href="/join">
    <button>
    شرکت در کاستوم 🎮
    </button>
    </a>

    </div>

    </body>
    </html>
        """

@app.route("/join", methods=["GET","POST"])
def join():
    msg = ""
    if request.method=="POST":

        conn=db()

        conn.execute(
            "INSERT INTO custom_players(name,uid,phone) VALUES(?,?,?)",
(
    request.form["name"],
    request.form["uid"],
    request.form["phone"]
)
        )

        conn.commit()
        conn.close()
        msg = "ثبت شرکت انجام شد ✅"
        return """
<h2 style="color:#FFD700">
ثبت شرکت انجام شد ✅
</h2>
<a href="/customs">بازگشت</a>
"""
    return """
    <html>
    <body style="background:#111;color:white;text-align:center">

    <h1 style="color:#FFD700">
    🎮 شرکت در کاستوم
    </h1>
<p>
""" + msg + """
</p>
    <form method="POST">

<input name="name" placeholder="نام بازیکن"><br><br>

<input name="uid" placeholder="UID فری فایر"><br><br>

<input name="phone" placeholder="شماره تماس"><br><br>



    <button>
    ثبت شرکت
    </button>

    </form>

    </body>
    </html>
    """
if __name__=="__main__":
    app.run(host="0.0.0.0",port=10000)

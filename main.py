from flask import Flask, request, session, redirect
import sqlite3

app = Flask(__name__)
app.secret_key = "FFASH2026"
TOURNAMENT = {
    "time": "20:00",
    "price": "50,000 تومان",
    "first": "5,000,000 تومان",
    "second": "2,000,000 تومان",
    "third": "1,000,000 تومان"
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

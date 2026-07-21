from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<title>FF ASH Tournament</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
body{
background:#111;
color:white;
font-family:Arial;
margin:0;
padding:0;
text-align:center;
}

.header{
background:linear-gradient(90deg,#FFD700,#222);
padding:25px;
font-size:35px;
font-weight:bold;
color:black;
}

.box{
background:#1a1a1a;
margin:15px;
padding:20px;
border-radius:15px;
border:2px solid #FFD700;
}

input{
width:80%;
padding:12px;
margin:8px;
border:none;
border-radius:8px;
}

button{
background:#FFD700;
color:black;
padding:12px 25px;
border:none;
border-radius:10px;
font-weight:bold;
}

.stats{
font-size:20px;
color:#FFD700;
}
</style>

</head>

<body>

<div class="header">
🏆 FF ASH TOURNAMENT 🏆
</div>


<div class="box">
<h2>🎮 به تورنومنت فری فایر خوش آمدید</h2>
<p>ثبت نام مسابقات رسمی FF ASH</p>
</div>


<div class="box">
<h2>📝 ثبت نام</h2>

<input type="text" placeholder="نام بازیکن"><br>
<input type="text" placeholder="UID فری فایر"><br>
<input type="text" placeholder="شماره تماس"><br>

<button>ثبت نام</button>

</div>


<div class="box">
<h2>📊 آمار</h2>

<div class="stats">
50+ بازیکن<br>
10+ تورنومنت<br>
1000+ بازدید
</div>

</div>


<div class="box">
<h2>📞 پشتیبانی</h2>

<p>@IM_SHAH__1</p>
<p>@MY_SHAYAN_1</p>

</div>


<div class="box">
<h2>👑 مدیریت</h2>

<p>ASH ADMIN PANEL</p>

</div>


</body>
</html>
"""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

print("FF ASH BOT")
from rubpy import Client

bot = Client("BJJAIF0STZGBTRLGEVWBIMBUBJRTNUCIPYBJVSWMNDOMFJISTZUCCINREVFXDVSI")

@bot.on_message()
async def messages(update):
    text = update.text

    if text == "/start":
        await update.reply(
            "سلام!\n"
            "برای ثبت نام کلمه register را ارسال کنید."
        )

    elif text == "register":
        await update.reply(
            "ثبت نام شما با موفقیت انجام شد ✅"
        )

bot.run()

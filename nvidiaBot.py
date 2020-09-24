from mail_to_sms import MailToSMS
import check_stock

phone_number = 1234567890                   # enter your phone number here
password = "yourpassword"               # enter your password to the email you will be using to send the message
email = "your-bot-email@gmail.com"          # email youll be using to send the message
provider = "att"                            # your cell phone provider


def send_sms():
    stock_bot = MailToSMS(phone_number, provider, email, password, subject="RTX3080 IS NOW IN STOCK")
    stock_bot.send("https://rb.gy/r577ju")


check_stock.check_stock()
send_sms()

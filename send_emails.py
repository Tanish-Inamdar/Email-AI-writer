from simplegmail import Gmail

gmail = Gmail() # will open a browser window to ask you to log in and authenticate

sample = """Tanish,



    The summer between your junior and senior years is an exciting and important time to set yourself up for a successful college search (and less stress your senior year!). We put together a simple guide of the top 7 things you can do this summer <https://admissions.xavier.edu/www/documents/summer-college-search.pdf> to help you get started. I think these small steps can make a big difference as you go into your senior year. 



    We are truly here to support you at Xavier, so please let me know how we can help with your college search. I'm looking forward to getting to know you more, Tanish!



    Julie Nelson

    Assistant Dean, Undergraduate Admission"""

sample = sample.replace("\n", "<br>")

def send_email(to, subject, message):
    params = {
    "to": to,
    "sender": "tanishdinamdar@gmail.com",
    "subject": subject,
    "msg_html": message,
    }
    message = gmail.send_message(**params)  # equivalent to send_message(to="you@youremail.com", sender=...)

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email.mime.image as img

# me == my email address
# you == recipient's email address
me = "isarkhan95@gmail.com"
you = "isarkhan95@gmail.com"
# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Link"
msg['From'] = me
msg['To'] = you
# Create the body of the message (a plain-text and an HTML version).
text = "Hi! Isaar"
html = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Here is the <a href="http://www.python.org">link</a> you wanted.
    </p>
    <div>
       <img src="https://drive.google.com/file/d/1Y84K599cR5b1cJsWak7AEwDjSVayJXKe/view?usp=sharing" alt="Smiley face" height="300" width="900">
    </div>
    <div>
       <img src="D:/text.png" alt="Smiley face" height="300" width="900">
    </div>
  </body>
</html>
"""

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')
# img_data = open('D:/chart.png', 'rb').read()
# img1=img.MIMEImage(img_data,'png')
# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)
# msg.attach(img1)
# Send the message via local SMTP server.
mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
mail.login('isarkhan95@gmail.com', 'N@ureenaslam786')
mail.sendmail(me, you, msg.as_string())
mail.quit()
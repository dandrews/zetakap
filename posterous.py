import smtplib

class Posterous:
    def __init__(self, subject, text, link):    
        self.from_addr = 'zetakap.media@gmail.com'
        self.to_addr = ['zetakap@posterous.com']
        self.subject = subject
        self.link = link
        self.text = text
    
    def send_post(self):

        self.message = """\
From: %s
To: %s
Subject: %s

<html>
  <head></head>
  <body>
    <p>
       %s ... <a href='%s'>Read the rest at SeekingAlpha.com</a>
    </p>
  </body>
</html>
""" % (self.from_addr, ", ".join(self.to_addr), self.subject, self.text, self.link )
        
#         self.text = """
# %s 
# <markdown>
# [Read the rest at SeekingAlpha.com](%s)
# </markdown>
# """ % (text,link)
    
#     def send_post(self):

#         self.message = """\
# From: %s
# To: %s
# Subject: %s

# %s

# """ % (self.from_addr, ", ".join(self.to_addr), self.subject, self.text )

        username = 'zetakap.media@gmail.com'  
        password = 'skippable'  
        server = smtplib.SMTP('smtp.gmail.com:587')  
        server.starttls()  
        server.login(username,password)  
        server.sendmail(self.from_addr, self.to_addr, self.message)
        server.quit()

# post = Posterous( "My Subject/Title", "AADKFJDLKFJDKLFJDLFJDJFLJLFD\nYIOUIOUOUO\nLJJLJL ", 'http://google.com' )
# print post.text
# print
# post.send_post()

"""
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Here is the <a href='http://www.python.org'>link</a> you wanted.
    </p>
  </body>
</html>
"""

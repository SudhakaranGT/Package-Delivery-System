import smtplib
fromMy = 'courierservices6@yahoo.com' # fun-fact: "from" is a keyword in python, you can't use it as variable.. did anyone check if this code even works?
to  = '23sujay23@gmail@Example.com'
subj='TheSubject'
date='2/1/2010'
message_text='Hello Or any thing you want to send'

msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % ( fromMy, to, subj, date, message_text )
  
username = str('courierservices6@yahoo.com')  
password = str('1qaz_2wsx')  
  

server = smtplib.SMTP("smtp.mail.yahoo.com",587)
server.login(username,password)
server.sendmail(fromMy, to,msg)
server.quit()    
print ('ok the email has sent ')
# from flask import Flask, jsonify
# from flask_mail import Mail, Message
# import os


# mail_settings = {
#     "MAIL_SERVER": 'smtp.gmail.com',
#     "MAIL_PORT": 465,
#     "MAIL_USE_TLS": False,
#     "MAIL_USE_SSL": True,
#     "MAIL_USERNAME": 'dervidme@gmail.com',
#     "MAIL_PASSWORD": 'fervour133'
# }
# app = Flask(__name__)

# mail = Mail(app)

# app.config.update(mail_settings)


# import smtplib
# import mimetypes

# from app import app
# from werkzeug.utils import secure_filename
# from flask import flash, render_template, request

# from email.message import EmailMessage
# from email.utils import make_msgid
		
	
# @app.route('/donations/send_news_later', methods=['POST'])
# def send_email():
# 	subject = request.form['email-subject']
# 	body = request.form['email-body']
# 	emails = request.form['emails']
	
# 	if subject and body and emails:
	
# 		msg = EmailMessage()

# 		asparagus_cid = make_msgid()
		
# 		msg['Subject'] = subject
# 		msg['From'] = 'email@gmail.com'
# 		msg['To'] = (emails)
		
# 		msg.add_alternative(body.format(asparagus_cid=asparagus_cid[1:-1]), subtype='html')
		
# 		if 'email-attachments[]' in request.files:
# 			files = request.files.getlist('email-attachments[]')

# 			for file in files:
# 				filename = secure_filename(file.filename)
				
# 				ctype = mimetypes.MimeTypes().guess_type(filename)[0]
				
# 				if ctype is None:
# 					ctype = 'application/octet-stream'
					
# 				maintype, subtype = ctype.split('/', 1)
# 				f_data = file.read()
				
# 				msg.add_attachment(f_data, maintype=maintype, filename=filename, subtype=subtype)
				
# 		s = smtplib.SMTP('smtp.gmail.com', 587)

# 		s.starttls()

# 		s.login('email@gmail.com', 'gmail password')
# 		s.send_message(msg)
# 		s.quit()
		
# 		flash('Email successfully sent to recepients')
		
# 		return render_template('emails.html', color='green')
# 	else:
# 		flash('Email subject, body and list of emails are required field')
		
# 		return render_template('emails.html', color='red')
		
# if __name__ == "__main__":
#     app.run()



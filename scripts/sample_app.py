from flask import Flask, request, render_template
import smtplib

app = Flask(__name__,template_folder=".")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    sender_email = request.form['sender_email']
    recipient_email = request.form['recipient_email']
    subject = request.form['subject']
    message = request.form['message']
    
    # connect to SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        
        # log in to SMTP server
        smtp.login('walterbrnrd@gmail.com', 'dndyshwmjuqpcylm')

        
        # create email message
        email_message = f'Subject: {subject}\n\n{message}'
        
        # send email
        smtp.sendmail(sender_email, recipient_email, email_message)
    
    return 'Email sent successfully!'

if __name__ == '__main__':
    app.run(debug=True)

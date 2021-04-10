import smtplib
import ssl


smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "sidharthsoumya2nd@gmail.com"
password = input("Type your password and press enter: ")

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()  # Can be omitted
    server.starttls(context=context)  # Secure the connection
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    message = """\
    Subject: Greetings

    Hi, Have a nice day."""
    # TODO: Send email here
    server.sendmail(sender_email, 'sidharthsoumya@gmail.com', message)
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit()

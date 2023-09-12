import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from src.utils import get_ticker_data
from src.utils import get_date
from src.utils import get_receivers
from src.logger import logging

def send_email(sender_email, sender_password, subject):


    with open(f"dags//src//news_letters//{get_date()}//news_letter_final.txt", "r") as file:
            body = file.read()
    
    smtp_server = "smtp.gmail.com"  # Replace with your SMTP server address
    smtp_port = 587  # Replace with the appropriate port for your SMTP server
    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        logging.info("Server Started")
        # Login to the sender email account
        server.login("aazarjan15003@gmail.com", sender_password)

        receivers = get_receivers("dags//src//subscriber_list.txt")
        logging.info("Receivers List Created")
        receivers_string = ", ".join(receivers)

        # Create a MIMEMultipart message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receivers_string
        msg['Subject'] = subject

        msg.attach(MIMEText("<img src='cid:logo'>", 'html'))

        # Attach the body of the email from the file
        msg.attach(MIMEText(body, 'plain'))
        ticker_data = get_ticker_data()
        ticker_data_text = f"""<br><br><b>Here is the day's performace for QQQ and SPY:</b>
        
            <table border="1">
        <tr>
            <th>Ticker</th>
            <th>Open</th>
            <th>Close</th>
            <th>High</th>
            <th>Low</th>
        </tr>
        <tr>
            <td>QQQ</td>
            <td>{ticker_data["QQQ Open"]}</td>
            <td>{ticker_data["QQQ Close"]}</td>
            <td>{ticker_data["QQQ Highest"]}</td>
            <td>{ticker_data["QQQ Lowest"]}</td>
        </tr>
        <tr>
            <td>SPY</td>
            <td>{ticker_data["SPY Open"]}</td>
            <td>{ticker_data["SPY Close"]}</td>
            <td>{ticker_data["SPY Highest"]}</td>
            <td>{ticker_data["SPY Lowest"]}</td>
        </tr>
    </table>
        """

        msg.attach(MIMEText(ticker_data_text, 'html'))

        heatmap_text = "<br><br><b>Check out today's Heatmap!</b>"
        msg.attach(MIMEText(heatmap_text, 'html'))
        msg.attach(MIMEText("<img src='cid:heatmap'>", 'html'))

        # Open the file to be sent
        with open(f"dags//src//heatmaps//heatmap-{get_date()}.png","rb") as image:
        # with open(r"C:\Users\azark\Desktop\News Letter Project\heatmaps\heatmap-2023-07-28.png","rb") as image:
            # Attach the image to the email
            image = MIMEImage(image.read())
            image.add_header('Content-ID', '<heatmap>')
            msg.attach(image)
        logging.info("Heatmap Attached")

        with open(f"dags//src//logo.png", "rb") as logo:
            logo = MIMEImage(logo.read())
            logo.add_header('Content-ID', '<logo>')
            msg.attach(logo)
        logging.info("Logo Attached")
        # Send the email
        # server.sendmail(sender_email, get_receivers(f"subscriber_list.txt"), msg.as_string())
        server.sendmail(sender_email,"azarkhowaja111@gmail.com", msg.as_string())    
        # Close the connection to the SMTP server
        server.quit()
        logging.info("Email Sent Successfully")
    except Exception as e:
        logging.info("Email Failed to Send")  
        logging.info(e)  


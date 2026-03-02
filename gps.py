import requests
import pywhatkit
import smtplib
from email.mime.text import MIMEText
import pyttsx3

def get_location():
    try:
        res = requests.get('https://ipinfo.io/json')
        data = res.json()
        loc = data['loc']  # "latitude,longitude"
        lat, lng = map(float, loc.split(','))
        print(f"Fetched location: {lat}, {lng}")
        return [lat, lng]
    except Exception as e:
        print(f"❌ Error fetching location: {e}")
        return None
    
engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def get_location_link():
    coords = get_location()
    if coords:
        lat, lng = coords
        return f"https://www.google.com/maps?q={lat},{lng}"
    else:
        return None

def send_location(mode="whatsapp"):
    # n = int(input("Enter the number: "))
    print("Starting send_location function...")
    location_link = get_location_link()
    print(f"Location link: {location_link}")
    
    if not location_link:
        print("❌ Location not available.")
        return

    message = f"📍 My current location: {location_link}"

    if mode.lower() == "whatsapp":
        try:
            print("Trying to send WhatsApp message...")
            phone_number = f"+91{8864038401}"
            pywhatkit.sendwhatmsg_instantly(phone_number, message)
            print("✅ Location sent via WhatsApp!")
        except Exception as e:
            print(f"❌ Failed to send WhatsApp message: {e}")

    elif mode.lower() == "email":
        try:
            print("Trying to send Email...")
            sender_email = "your_email@gmail.com"
            sender_password = "your_password"
            receiver_email = "receiver_email@gmail.com"

            msg = MIMEText(message)
            msg['Subject'] = "My Current Location"
            msg['From'] = sender_email
            msg['To'] = receiver_email

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            server.quit()

            print("✅ Location sent via Email!")
        except Exception as e:
            print(f"❌ Failed to send Email: {e}")

    else:
        print("❌ Invalid mode selected.")

def send_msz():
    n = input("Enter the number: ")
    a = input("Type your message: ")
    print("Sending your message, please wait!")
    pywhatkit.sendwhatmsg_instantly(f"+91{n}", f"{a}")
    print("Your message has been sent.")

# def choose_sos_msz():
#     c = input("Choose 'Zero' for general message and 'One' for SOS: ")
#     if c == 1:
#         send_location("whatsapp")
#     elif c == 0:
#         send_msz()
# choose_sos_msz()

# if __name__ == '__main__':
#     c = int(input("Choose 'Zero' for general message and 'One' for SOS: "))
#     if c == 1:
#         send_location("whatsapp")
#     elif c == 0:
#         send_msz()
#     else:
#         print("❌ Invalid choice! Please enter 0 or 1.")

# if __name__ == '__main__':
def main_function():
    while True:
        try:
            c = input("Choose '0' for general message, '1' for SOS and '2' for exit: ")

            if c == "1":
                send_location("whatsapp")
                speak(f"your location has been sent")
                break  # Exit loop after successful SOS
            elif c == "0":
                send_msz()
                speak(f"your message has been sent")
                break  # Exit loop after successful message
            elif c == "2":
                break
            else:
                print("❌ Invalid input. Please enter '0', '1' or '2'. Try again.")

        except Exception as e:
            print(f"❌ An unexpected error occurred: {e}")
            break  # Exit loop on unexpected error

main_function()
# send_location("whatsapp")
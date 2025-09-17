import smtplib
import ssl
from utils.speech import speak, takeCommand
from config.settings import EMAIL_ADDRESS, EMAIL_PASSWORD, SMTP_SERVER, SMTP_PORT
from data.contacts import CONTACTS

def sendmail(to, content):
    """Send email using SMTP"""
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            
            # Create proper email format
            message = f"Subject: Message from Jarvis\n\n{content}"
            server.sendmail(EMAIL_ADDRESS, to, message)
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

def handle_email():
    """Handle email sending process"""
    while True:
        speak(f"Your email is {EMAIL_ADDRESS}")
        speak("Who do you want to email?")
        name = takeCommand().lower().strip()

        if "exit" in name or "cancel" in name:
            speak("Exiting email flow.")
            break

        to = CONTACTS.get(name)
        if not to:
            speak(f"I couldn't find a contact named {name}. Available contacts are: {', '.join(CONTACTS.keys())}")
            continue

        speak(f"Sending email to {name} at {to}. Is that correct?")
        confirmation = takeCommand().lower()
        if "no" in confirmation:
            speak("Okay, let's try again.")
            continue

        speak("What should I say in the email?")
        content = takeCommand()
        
        if not content or content == "none":
            speak("I didn't catch the message. Please try again.")
            continue

        speak(f"You said: {content}. Should I send it?")
        final_confirmation = takeCommand().lower()
        if "no" in final_confirmation:
            speak("Okay, starting over.")
            continue

        success = sendmail(to, content)
        if success:
            speak("Email sent successfully.")
        else:
            speak("Failed to send the email. Please check your email settings.")
        break

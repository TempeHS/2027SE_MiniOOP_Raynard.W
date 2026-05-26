# Driver to test Audio_Notification
from audio_notification import Audio_Notification

def test_audio():
    audio = Audio_Notification(27)
    audio.warning_on()
    print("Audio Notifcation")

test_audio()

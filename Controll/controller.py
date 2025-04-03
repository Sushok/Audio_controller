import pyautogui
import subprocess

class Controller:
    @staticmethod
    def play_pause():
        pyautogui.press("playpause")

    @staticmethod
    def next_track():
        pyautogui.press("nexttrack")

    @staticmethod
    def prev_track():
        pyautogui.press("prevtrack")

    @staticmethod
    def volume_up():
        pyautogui.press("volumeup")

    @staticmethod
    def volume_down():
        pyautogui.press("volumedown")

    @staticmethod
    def mute():
        pyautogui.press("volumemute")
    
    @staticmethod
    def set_volume(volume):
        # Для Windows можно использовать nircmd для установки громкости
        # Если у вас установлен nircmd, можно использовать команду для установки громкости
        subprocess.run(["nircmd", "setsysvolume", str(volume * 65535 // 100)])

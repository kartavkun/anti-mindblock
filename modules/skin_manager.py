import os
import getpass
import subprocess
from PIL import Image, UnidentifiedImageError

username = getpass.getuser()

class Skins:
    @staticmethod
    def backup_skin(skin_name, osu_directory):
        skin_directory = f"{osu_directory}/Skins"
        subprocess.run(['cp', '-r', f"{skin_directory}/{skin_name}", f"{skin_directory}/{skin_name}.bak"])
        return skin_directory

    @staticmethod
    def check_skin(config_data):
        config_file = f"{config_data}/osu!.{username}.cfg"
        
        if not os.path.isfile(config_file):
            print(f"Файл конфигурации {config_file} не найден.")
            return None
        
        with open(config_file, "r", encoding="utf-8") as file:
            for line in file:
                if line.startswith("Skin = "):
                    skin_name = line.strip().replace("Skin = ", "")
                    Skins.backup_skin(skin_name, config_data)
                    return skin_name

        print("Настройка скина не найдена в файле конфигурации.")
        return None   

    @staticmethod
    def find_osu_exe_directory(start_directory):
        for root, dirs, files in os.walk(start_directory):
            if 'osu!.exe' in files:
                return root
        return None

    osu_wine_path = os.path.expanduser("~/.local/share/osu-wine/osu!/osu!.exe")

    @staticmethod
    def osu_directory():
        if os.path.isfile(Skins.osu_wine_path):
            print(f"Ты используешь osu-wine: /home/{username}/.local/share/osu-wine/osu!")
            return os.path.dirname(Skins.osu_wine_path)
        
        start_directory = os.path.expanduser('~')
        osu_directory = Skins.find_osu_exe_directory(start_directory)

        if osu_directory:
            return osu_directory
        
        print("sosal?")
        return None

class SkinRotater:
    def rotate_images():
        osu_directory = Skins.osu_directory()
        if not osu_directory:
            print("Не удалось найти osu! директорию.")
            return

        current_skin = Skins.check_skin(osu_directory)
        if not current_skin:
            print("Не удалось определить текущий скин.")
            return

        skins_directory = os.path.join(osu_directory, 'Skins')
        skin_path = os.path.join(skins_directory, current_skin)

        if not os.path.exists(skin_path):
            print("No skin path provided.")
            return

        rotate_prefixes = ["default-", "cursor", "spinner", "slider", "play-skip", "hit", "ranking", "section"]
        transparency_prefixes = ["score", "scorebar"]

        skin_ini_path = os.path.join(skin_path, "skin.ini")
        if os.path.exists(skin_ini_path):
            with open(skin_ini_path, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()
                    if line.startswith('HitCirclePrefix:'):
                        rotate_prefixes.append(line.split(':')[1].strip() + '-')
                    if line.startswith('ScorePrefix:'):
                        transparency_prefixes.append(line.split(':')[1].strip())

        temp_folder_path = os.path.join(skin_path, "temp_australia_mode")
        if not os.path.exists(temp_folder_path):
            os.makedirs(temp_folder_path)

        for root, dirs, files in os.walk(skin_path):
            if root.endswith("temp_australia_mode"):
                continue
            for file in files:
                if file.endswith(".png"):
                    image_path = os.path.join(root, file)
                    temp_image_path = os.path.join(temp_folder_path, file)
                    if any(file.startswith(prefix) for prefix in rotate_prefixes) and not any(file.startswith(prefix) for prefix in transparency_prefixes):
                        process_image(image_path, temp_image_path, rotate=True)
                    elif any(file.startswith(prefix) for prefix in transparency_prefixes):
                        process_image(image_path, temp_image_path, transparency=True, rotate=True)


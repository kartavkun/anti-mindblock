import os
import getpass
import subprocess
# from PIL import Image, UnidentifiedImageError
# import shutil

username = getpass.getuser()

# Я ТАК ЗАЕБАЛСЯ ПРИДУМЫВАТЬ НАЗВАНИЯ ПЕРЕМЕННЫХ И ФУНКЦИИ В КЛАССЕ
# Я НЕ УВЕРЕН, ЧТО ЭТО ПРАВИЛЬНО РАБОТАЕТ
# Я НЕ УВЕРЕН, ЧТО ЭТО ПРАВИЛЬНО РАБОТАЕТ
# ПОЧЕМУ Я НЕ УВЕРЕН, ЧТО ЭТО ПРАВИЛЬНО РАБОТАЕТ?
# Я НЕ УВЕРЕН, ЧТО ЭТО ПРАВИЛЬНО РАБОТАЕТ
# КАК Я НЕ УВЕРЕН, ЧТО ЭТО ПРАВИЛЬНО РАБОТАЕТ
# Я НЕ УВЕРЕН, ЧТО ЭТО ПРАВИЛЬНО РАБОТАЕТ
# НЕ УВЕРЕН, ЧТО ЭТО ПРАВИЛЬНО РАБОТАЕТ
# Я НЕ УВЕРЕН, ЧТО ЭТО ПРАВИЛЬНО РАБОТАЕТ
# ЕБИТЕ МЕНЯ В РОТ

# Я буду в ахуе, если это заработает xD

class Skins:
    australia_skin_path = None

    @staticmethod
    def backup_skin(skin_name, osu_directory):
        skin_directory = f"{osu_directory}/Skins"
        subprocess.run(['cp', '-r', f"{skin_name}", f"{skin_name}.bak"])
        skin_path = f"{skin_directory}/{skin_name}"
        return skin_path

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
                    Skins.australia_skin_path = Skins.backup_skin(skin_name, config_data)
                    # Skins.australia_skin_path = Skins.backup_skin(current_skin_path, config_data)
                    print(f"Текущий скин: {Skins.australia_skin_path}")
                    return Skins.australia_skin_path

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
            osu_directory = os.path.dirname(Skins.osu_wine_path)
            return osu_directory
        
        start_directory = os.path.expanduser('~')
        osu_directory = Skins.find_osu_exe_directory(start_directory)

        if osu_directory:
            print(f"Файл osu!.exe найден в директории: {osu_directory}")
            check_skin = Skins.check_skin(osu_directory)
            # if check_skin:
                # print(f"Текущий скин: {check_skin}")

            backup = Skins.backup_skin(check_skin, osu_directory)
            if backup:
                print(f"Скин был сохранен в директории {backup}")
        else:
            print("sosal?")
        # return None
#
# if __name__ == "__main__":
#     skin_manager = Skins()
#     skin_manager.osu_directory()

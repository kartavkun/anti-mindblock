from modules.wayland_checker import SessionChecker
from modules.xrandr_manager import XrandrManager
from modules.otd_invert import TabletRotator
from modules.skin_manager import Skins
# from modules.skin_inverter import Skin

if __name__ == "__main__":
    session = SessionChecker()
    
    if session.is_valid():
        # Инициализация менеджера для экрана
        xrandr_manager = XrandrManager()
        xrandr_manager.rotate_screen()

        print("✅ Session check passed. Rotating tablet...")
        
        # Инициализация менеджера для планшета
        tablet = TabletRotator()
        
        if tablet.rotate(180):  # Меняем ротацию
            tablet.restart_driver()

        skin_backuper = Skins()
        skin_backuper.osu_directory()

        # skin = Skin()
        # skin_inverter.osu_directory()

        print("✅ Australia mode activated.")

    else:
        print("❌ Session check failed. Exiting.")

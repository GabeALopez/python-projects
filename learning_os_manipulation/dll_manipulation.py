import winreg

def get_current_wallpaper():
    key = r"HKEY_CURRENT_USER\Control Panel\Desktop"
    value_name = "Wallpaper"

    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key) as reg_key:
            wallpaper_path, _ = winreg.QueryValueEx(reg_key, value_name)
            return wallpaper_path
    except FileNotFoundError:
        return None

# Example usage
if __name__ == "__main__":
    current_wallpaper = get_current_wallpaper()
    if current_wallpaper:
        print("Current wallpaper:", current_wallpaper)
    else:
        print("Unable to retrieve current wallpaper.")
import os
import sys
import subprocess
import shutil
import time
import tempfile

from colorama import Fore, Style, init

init(autoreset=True)
def print_logo():
    print(Fore.CYAN + r"""

 _____          _        _       _             
|_   _|        | |      | |     | |            
  | | _ __  ___| |_ __ _| | __ _| |_ ___  _ __ 
  | || '_ \/ __| __/ _` | |/ _` | __/ _ \| '__|
 _| || | | \__ \ || (_| | | (_| | || (_) | |   
 \___/_| |_|___/\__\__,_|_|\__,_|\__\___/|_|   
                                               
                                                
        """)
    print(Fore.CYAN + "              Made with ❤️ by mOntey")
    print(Style.RESET_ALL)

def loading_bar(task, total_time=2):
    print(Fore.YELLOW + f"-> {task}")
    for i in range(0, 21):
        time.sleep(total_time / 20)
        bar = ('#' * i).ljust(20)
        percent = int((i/20)*100)
        sys.stdout.write(f"\r[{bar}] {percent}%")
        sys.stdout.flush()
    print()

def create_shortcut(name, target_path):
    try:
        import winshell
        from win32com.client import Dispatch

        desktop = winshell.desktop()
        path = os.path.join(desktop, f"{name}.lnk")
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(path)
        shortcut.Targetpath = target_path
        shortcut.WorkingDirectory = os.path.dirname(target_path)
        shortcut.save()
        print(Fore.GREEN + f"skrót {name} utworzony!")
    except Exception as e:
        print(Fore.RED + f"error skrótu: {e}")

def install_program(file_name, display_name):
    try:
        installer_dir = os.path.join(os.getcwd(), "installers")
        installer_path = os.path.join(installer_dir, file_name)

        if not os.path.exists(installer_path):
            print(Fore.RED + f"install {file_name} nie znaleziony w {installer_dir}..")
            return

        loading_bar(f"Instalacja {display_name}...")
        subprocess.run([installer_path, '/S'], check=True)
        print(Fore.GREEN + f"! {display_name} zainstalowano!")
        create_shortcut(display_name, find_executable(display_name))

    except subprocess.CalledProcessError:
        print(Fore.RED + f"error instalacji {display_name}!")
    except Exception as e:
        print(Fore.RED + f"error przy instalacji {display_name}: {e}")


def find_executable(program_name):
    program_paths = {
        "Visual Studio Code": r"C:\Program Files\Microsoft VS Code\Code.exe",
        "Python": r"C:\Python\python.exe",
        "XAMPP": r"C:\xampp\xampp-control.exe",
        "PyCharm": r"C:\Program Files\JetBrains\PyCharm Community Edition\bin\pycharm64.exe",
        "Notepad++": r"C:\Program Files\Notepad++\notepad++.exe",
        "Git": r"C:\Program Files\Git\git-bash.exe",
        "IntelliJ IDEA": r"C:\Program Files\JetBrains\IntelliJ IDEA Community Edition\bin\idea64.exe"
    }
    return program_paths.get(program_name, "")

def main_menu():
    while True:
        print_logo()
        print(Fore.GREEN + """
Wybierz tryb instalacji:

[1] Matura (VSCode, Python, XAMPP, PyCharm, Notepad++)
[2] Matura v2 (VSCode, Python, PyCharm, Notepad++)
[3] Dev (PyCharm, Python, IntelliJ IDEA, Git)
[4] Własny wybór programów
[0] Wyjście
""")
        wybor = input(Fore.CYAN + "Wybierz opcję: ")

        if wybor == '1':
            install_program("vscode.exe", "Visual Studio Code")
            install_program("python.exe", "Python")
            install_program("xampp.exe", "XAMPP")
            install_program("pycharm.exe", "PyCharm")
            install_program("notepadpp.exe", "Notepad++")
            break

        elif wybor == '2':
            install_program("vscode.exe", "Visual Studio Code")
            install_program("python.exe", "Python")
            install_program("pycharm.exe", "PyCharm")
            install_program("notepadpp.exe", "Notepad++")
            break

        elif wybor == '3':
            install_program("pycharm.exe", "PyCharm")
            install_program("python.exe", "Python")
            install_program("intellij.exe", "IntelliJ IDEA")
            install_program("git.exe", "Git")
            break

        elif wybor == '4':
            custom_install()
            break

        elif wybor == '0':
            print(Fore.YELLOW + "naura")
            sys.exit()
        else:
            print(Fore.RED + "zly wybor nr!")

def custom_install():
    programs = [
        ("Visual Studio Code", "vscode.exe"),
        ("Python", "python.exe"),
        ("XAMPP", "xampp.exe"),
        ("PyCharm", "pycharm.exe"),
        ("Notepad++", "notepadpp.exe"),
        ("Git", "git.exe"),
        ("IntelliJ IDEA", "intellij.exe")
    ]
    selected = []

    print(Fore.MAGENTA + "\nWybierz programy do install:")
    for idx, (name, _) in enumerate(programs, start=1):
        print(f"[{idx}] {name}")
    print("[0] Rozpocznij instalacje")

    while True:
        try:
            option = int(input(Fore.CYAN + "twój wybór: "))
            if option == 0:
                break
            if 1 <= option <= len(programs):
                selected.append(programs[option-1])
                print(Fore.GREEN + f"Dodano {programs[option-1][0]}")
            else:
                print(Fore.RED + "Zly wybór!")
        except ValueError:
            print(Fore.RED + "podaj liczbe!")

    for program_name, exe_file in selected:
        install_program(exe_file, program_name)

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    main_menu()
    print(Fore.GREEN + "\nInstalacja zakończona pomyślnie!!!")
    input(Fore.CYAN + "\nNaciśnij Enter, aby wyjsc...")

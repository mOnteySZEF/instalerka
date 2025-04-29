# Instalerka

![Icon](icon.ico)

## Opis

Ten skrypt Pythona automatyzuje proces instalacji popularnych programów, takich jak Visual Studio Code, Python, XAMPP, PyCharm i inne. Umożliwia użytkownikom wyboru programów do zainstalowania oraz tworzy skróty na pulpicie dla zainstalowanych aplikacji.

## Wymagania

- Python 3.x
- Moduł `colorama`
- W systemie Windows, ponieważ korzysta z `winshell` i `win32com.client`

## Użycie

1. Skopiuj instalatory programów do folderu `installers` w tym samym katalogu, co skrypt.
2. Uruchom skrypt:
```bash
   python main.py
```

3. Wybierz tryb instalacji z wyświetlonego menu:

   - [1] Matura (VSCode, Python, XAMPP, PyCharm, Notepad++)
   - [2] Matura v2 (VSCode, Python, PyCharm, Notepad++)
   - [3] Dev (PyCharm, Python, IntelliJ IDEA, Git)
   - [4] Własny wybór programów
   - [0] Wyjście

4. Postępuj zgodnie z instrukcjami na ekranie, aby zainstalować wybrane programy.

## Funkcjonalności

- Instalacja wielu programów na raz
- Tworzenie skrótów na pulpicie do zainstalowanych programów
- Możliwość wyboru programów do instalacji przez użytkownika
- Prosty interfejs w konsoli z kolorowym wyświetlaniem informacji

## Licencja

Ten projekt jest objęty licencją MIT. Zobacz plik [LICENSE](LICENSE) po więcej informacji.

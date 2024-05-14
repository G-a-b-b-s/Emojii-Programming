Interpreter Języka Emoji
Celem tego projektu jest stworzenie interpretera emotikonowego, który służyłby dzieciom do łatwej nauki programowania.

Język Implementacji
Python 3
Użyte Narzędzia i Biblioteki
ANTLR4: Oficjalna strona ANTLR4
Instalacja i Uruchomienie
Sklonuj Repozytorium:

sh
Skopiuj kod
git clone <repository-url>
cd <repository-directory>
Zainstaluj Wymagane Biblioteki:
Zainstaluj środowisko uruchomieniowe ANTLR4 dla Pythona używając pip:

sh
Skopiuj kod
pip install antlr4-python3-runtime==4.13.1
Uruchom Interpreter:
Uruchom główny skrypt:

sh
Skopiuj kod
python main.py
Użycie
Identyfikacja Tokenów:

Zidentyfikowane tokeny zostaną zapisane do pliku tokens.txt.
Drzewo Parsowania:

Wynik analizy składniowej (drzewo parsowania) zostanie zapisany do pliku parsing_tree.txt.
Edytowanie Pliku Testowego:

Możesz dostosować plik testowy do swoich potrzeb, aby przetestować różne aspekty interpretera.
Autorzy
Martyna Baran
Gabriela Czapska
Kontakt
Martyna Baran: martynab@student.agh.edu.pl
Gabriela Czapska: czapska@student.agh.edu.pl
Projekt wykonany na potrzeby przedmiotu "Teoria kompilacji i kompilatory" w ramach kierunku Informatyka i Systemy Inteligentne na Akademii Górniczo-Hutniczej w Krakowie.

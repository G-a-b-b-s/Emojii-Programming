# Interpreter Języka Emotikonów

Celem tego projektu jest stworzenie interpretera języka emotikonowego, który służyłby dzieciom do łatwej nauki programowania w prosty i angażujący sposób.

## Język Implementacji
- Python 3

## Narzędzia i Biblioteki
- ANTLR4: [Oficjalna strona ANTLR4](https://www.antlr.org/)
  
- GraphViz https://graphviz.org/



## Instalacja i Uruchomienie

1. **Klonowanie Repozytorium**:
   ```sh
   git clone <adres-repozytorium>
   cd <katalog-repozytorium>
   ```
2.**Instalacja Zależności**:
  Zainstaluj środowisko wykonawcze ANTLR4 dla Pythona używając pip:
  ```sh
  pip install antlr4-python3-runtime==4.13.1
  ```
3.**Uruchomienie Interpretera**:
  Uruchom główny skrypt:
  ```sh
  python main.py
```
## Użytkowanie
-**Identyfikacja Tokenów**:

Zidentyfikowane tokeny zostaną zapisane do pliku tokens.txt.

-**Drzewo Parsowania**:

Wynik analizy składniowej (drzewo parsowania) zostanie zapisany w diretory Results, a dokładniej do pliku parsing_tree.txt, natomiast wersja png - w pliku 'dot parsing tree'.

-**Edycja Pliku Testowego**:

Możesz dostosować plik testowy do swoich potrzeb, aby przetestować różne aspekty interpretera.


## Autorzy i Kontakt

**Martyna Baran**: martynab@student.agh.edu.pl

**Gabriela Czapska**: czapska@student.agh.edu.pl


Projekt wykonany na potrzeby przedmiotu "Teoria kompilacji i kompilatory" na kierunku Informatyka i Systemy Inteligentne w Akademii Górniczo-Hutniczej w Krakowie.

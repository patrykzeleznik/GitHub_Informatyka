Krótki opis działania i posługiwania się aplikacją:

Mój program posiada możliwość manualnego dodawania cieczy do każdego ze zbiorników oraz przelewania się jej. Oprócz tego, jesteśmy w stanie
także zwiększyć, lub zminiejszyć temperature Zbiornika nr.1, co po otworzeniu się zaworów wpływa na temperaturę wody w zbiornikach znajdujących się niżej.
Użyłem w tym celu wzoru związanego z mieszniem się substancji o różnych objętościach oraz temperaturach. Istotnym jest, że Zbiornik nr.1 posiada
taką samą pojemność co pozostałe, a jest większy tylko ze względów wizualnych. Każdy ze zbiorników posiada własny licznik poziomu oraz temperatury co pozwala, co manualne ustawienie 
odpowiedniej wartości, która nas interesuje. Pomóc w tym może nam także opcja "Odpompuj", która usuwa wodę ze zborników dolnch. Metodą, ściśle związaną z automatyzacją może być
funkcja regulacji poziomu cieczy jak i temperatury w zbiornikach znajdujących się na dole. Polega na tym, że jeżeli poziom cieczy jest wiekszy w Zbiorniku nr.4
to usuwamy z niego ciecz poprzez metodę odpompuj, a w Zbiorniku nr.5 dodajemy poprzez funkcję popmpuj do momentu uzyskania tego samego poziomu cieczy w Zbiornikach dolnych.
Analogicznie działa metoda regulacji temperatury.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

LOGIKA PROGRAMU

Metody:

--> Przelewanie się wody ze zbiorników:
odpowiada za to funkcja - logika_przepływu, która jest bardzo zbliżona do tej użytej podczas zajęć labolatoryjnych, ale posiada jeden element dodany przeze mnie w celu urozmaicenia 
animacji. Jest nim zmiana temperatury, która jest określona przez wzór na zmianę tej wartości. Uruchomić możemy tę metodę dzięki przyciskowi Otwórz zawory.

--> Pompowanie cieczy do zbiorników:
Kazdy ze Zbiorników może być uzupełniony dodatkową wodą. Można tego dokonać dzięki funkcji pompowanie_cieczy. Użyłem opcji z if'ami, aby nie rozdzielać funkcji na pełno niepotrzebnych,
tylko mieć wszytsko w jednym miejscu a przy wywoływaniu funkcji w nawiasach wpisać interesujący nas numer pompy. Istotne jest że T wody z pompy to 0, więc wlewając ją do 
Zbiornika z T > 0, zmniejszamy jej T.

--> Odpompowanie cieczy:
Polega na tej samej zasadzie co metoda wyżej, różni się jedynie tym, że ciecz usuwamy ze zbiornika. Odgrywa fundamentalną rolę przy regulacji.

--> Zwiększanie T:
Bardzo prosta funkcja, która polega na tym że jeżeli poziom cieczy jest > 0, to po kliknięciu odpowiedniego przycisku T cieczy w Zbiorniku nr.1 zwiększa się do max wartości 100,
określonej w min(100, app.z1.aktualna_ilosc + 4). Istotne to jest, że dzięki funkcji w pliku zbiornik.py - pobierz_kolor() woda w zbiorniku zmienia się w zależności od
funkcji związanej z kolorami RGB. Zmiana tych kolorów to nie jest moja autorska metoda, a bardziej inspiracja, by kolor cieczy zmieniał się w bardziej korzystny sposób,
nie przechodząc przez kolor fioletowy(Wizualne ulepszenie).

--> Zmniejszamy T:
To samo co metoda wyżej, T zmniejszamy aż do min wartości 0, określonej w max(0, app.z1.aktualna_wartość - 4)

--> Regulacja Poziomu:
Metoda bardzo prosta, jednak obarczona pewnym błędem. Jest tak ponieważ program wykonuje bardzo dużo operacji w jednej chwili i nie byłem w stanie wymysleć funkcji, która zawsze 
ustawiała by poziom wody idealnie na tym samym poziomie. Polega ona na policzeniu róznicy poziomu wody w Zbiornikach nr.4 oraz nr.5, porównaniu z tolerancją(Naszym błędem) oraz 
w zależności od nich regulacji aż do momentu uzyskania odpowiedniej wartości. Do tego odpalają się odpowiednie pompy i wykonują operacje na tych Zbiornikach. Nawet jeżeli zawory rur
będą otwarte, to po kliknięciu przycisku regulacji wszystkie się zamkną, aby nie wpłynąć negatywnie na proces.

--> Regulacja T:
Metoda dosłownie polega na tym samym co regulacja Poziomu. Także potrzebujemy tolerancję, także istotna jest różnica oraz wyłączane są wszytskie procesy, aby nie generować 
dodatkowych zakłóceń(Układ sterowania nie jest na nie odporny).

Przyciski:

Każdy z przycisków podłączony jest do odpowiedniej metody oraz przełącza się w stan działania dzięki funkcji przełącz_symulacje(). To samo co wyżej, używam if'ów
w celu ujednolicenia kodu.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

ELEMENTY GRAFICZNE

Do utworzenia elementów graficznych, użyłem biblioteki PyQt. Metody przepływu cieczy w rurach, zbiornikach są praktycznie takie same jak te, które były wykonywane na zajęciach.
Jedyna różnica to metoda pobierz_kolor() klasy Zbiornik, którą opisałem wyżej. Podzieliłem ten program na 5 plików z czego 3, są związane z elemenatmi graficznymi - zbiornik.py,
rura.py, elementy_graficzne_py.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

SKRÓCENIE KODU

Do skrócenia kodu podzieliłem mój kod na 5 części, ale w rzeczywistości dzielą się na 3 segmenty - logika gry, elementy graficzne i to w czym łączy się całość, czyli program główny.
Niestety, logika_gry.py posiada prawie 500 linijek kodu, jednak nie byłem w stanie już zmniejszyć tej ilości. Reszta plików mieści się w zakresie do 80 linijek.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

PODSUMOWANIE:

Wydaje mi się, że program posiada praktyczne wykorzystanie - realizuje procesy wlewania cieczy przez pompy, otwierania zaworów, zmiany koloru oraz temperatury, a nawet regulacji
dwóch wartości. Myślałem także o dodaniu opcji nastawy odpowiedniego poziomu cieczy, bądź temperatury, ale wiązało by się to z dużym skomplikowaniem interfejsu w postaci zbyt dużej
ilości przycisków. Same funckje polegałyby na tym samym co regulacja poziomu, po prostu rożnica poziomu potrzebna do porównania z tolernacją wyglądałaby następująco:

--> roznica = app.z1.aktualna_ilosc - app.wartosc_zadana

Reszta metody nie różniłaby się znacząco. To samo z temperaturą.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




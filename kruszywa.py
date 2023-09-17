
while 1:
    try:

        powierzchnia = input("Podaj powierzchnię do zasypania w m2: ")
    
        if "," in powierzchnia:
            powierzchnia = powierzchnia.replace(",", ".")

        powierzchnia_input = float(powierzchnia)
        break
    except ValueError:
        print("Musisz wpisać liczbę.")
        
while 2:
    try:
        grubosc = input("Podaj grubość warstwy w cm: ")
        if "," in grubosc:
            grubosc = grubosc.replace(",", ".")
        grubosc_input = float(grubosc)
        break
    except ValueError:
        print("Musisz wpisać liczbę.")
grubosc_wlasciwa = grubosc_input / 100

wynik = (powierzchnia_input * grubosc_wlasciwa * 1.7) *1000

print("Ilość potrzebnego kruszywa to: ", round(wynik),"kg.")




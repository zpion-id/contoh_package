from mypackage import modul1, modul2, modul3
from mypackage.subpackage1 import modul11
from mypackage.subpackage1.subpackage11 import modul111
from mypackage.subpackage1.subpackage12 import modul121
from mypackage.subpackage2 import modul21
#from mypackage import subpackage1 # error

def main():
    print(f'{__file__} : main')
    modul1.metode11()
    modul1.metode12()
    modul2.metode21()
    modul2.metode22()
    modul3.metode31()
    modul3.metode32()
    modul11.metode21()
    modul111.metode111()
    modul111.metode112()
    modul121.metode21()
    modul21.metode21()
    modul21.metode22()
    #subpackage1.modul11.metode() # error

print(f'{__file__} : ')
if(__name__ == '__main__'):
    main()

"""
modul ini tidak bisa di akses secara langsung misal
-----------------------
python mypackage/app.py
-----------------------
muncul error :
ModuleNotFoundError: No module named 'mypackage'
"""
## Project Structure of Python
Structure direktori untuk project Python


### Directory Tree
Berikut directory-tree :
```
Project
├─doc
├─mypackage
│   ├─subpackage1
│   │  ├─subpackage11
│   │  │  ├──__init__.py
│   │  │  └──modul111.py
│   │  ├─subpackage12
│   │  │  ├──__init__.py
│   │  │  └──modul121.py
|   │  ├──__init__.py
│   |  ├──modul11.py
│   │  └──modul12.py     
│   ├─subpackage2
│   │  ├──__init__.py
│   │  ├──modul21.py
│   │  └──modul22.py
│   ├─__init__.py
│   ├─__main__.py
|   ├─main.py
│   ├─modul1.py
|   ├─modul2.py
│   └─modul3.py
├─README.md
└─app.py
```




### Cara import
misal kita ingin import `mypackage/subpackage1/modul11.py` in `mypackage/subpackage2/modul21.py`, bisa ditulis sbb:
```python
from mypackage.subpackage1 import modul11
```

Begitu juga jika kita ingin import `mypackage/subpackage1/modul11.py` dalam `test.py`), bisa ditulis sbb:
```python
from mypackage.subpackage1 import modul11
```


### Cara Eksekusi
Cara eksesukusi package:

```shell
python -m 'mypackage'
```
Jika ingin eksekusi `mypackage` dengan modul luar misal file `app.py`, berikut cara eksekusinya:

```shell
ptyhon -m app
```

Eksekusi dari shell di luar direktori `mypackage` jika tidak ada file `__main__.py` maka akan error :

```shell
$ python -m mypackage
/mypackage/__init__.py
/home/ubuntu/miniconda3/envs/pandas/bin/python: No module named mypackage.__main__; 'mypackage' is a package and cannot be directly executed
```

Eksekusi dari file `app.py` diluar direktori `mypackage` dengan kondisi file `__init__.py` kosong :
```shell
$ python -m app
/mypackage/__init__.py
```
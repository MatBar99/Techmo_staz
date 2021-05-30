# Techmo_staz
Rozwiązanie zadań na staż 

# [Zadanie projektowe ASR]
Celem programu jest wykorzystanie istniejącego repozytorium DeepSpeech:
https://github.com/mozilla/DeepSpeech 
 
W celu transkrypcji mowy z dziesięciu przygotowanych nagrań. 
Wykorzystano pre-trenowany model dostępny dzięki twórcom użyte repozytorium, dodatkowo rozpoznawanie mowy zostało wzmocnione modelem językowym również dostarczonym przez twórców DeepSpeech.

Po uruchomienu ``task_project.py`` transkrypcje zostają zapisane do pliku ``results.csv``.

# [Zadanie Python]
Wszystko zawarte w pliku ``staz.ipynb``

## Przebieg instalacji zadania projektowego - Windows 

### 0. Pobrać repozytorium w wybrane miejsce

Należy mieć zainstalowany git.

Włączyć ``cmd`` i za pomocą komendy ``cd`` wybrać miejsce, w którym repozytorium ma zostać pobrane.

Następnie, pobrać repozytorium za pomocą komendy: 

`` git clone https://github.com/MatBar99/Techmo_staz.git `` 




### 1. Przygotować w Python wirtualne środowisko:

Włączyć ``cmd`` i jeśli to potrzebne zainstalować ``pip`` oraz pakiet ``virtualenv``


 - Stworzyć wirtualne środowisko w miejscu gdzie zostało pobrane repozytorium o nazwie ``task_one``:

``virtualenv task_one``

 - Uruchomić wirtualne środowisko: 

``task_one\Scripts\activate``



### 2. Zainstalować biblioteki zgodnie z plikiem ``requirements.txt``:

```
 pip install -r requirements.txt
```

### 3. Pobrać model rozpoznawania mowy wraz z modelem językowym korzystając z terminala:

```
 python -m wget https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.pbmm
 
 python -m wget https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.scorer
```
### 4. Uruchomić plik ``task_project.py`` 
```
python -m task_project.py
```

Badane pliki powinny znajdować się w folderze ``test_wavs`` - cały ten folder zostanie przebadany. 



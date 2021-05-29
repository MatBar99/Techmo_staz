# Techmo_staz
Rozwiązanie zadań na staż 

# [Zadanie projektowe ASR]
Celem programu jest wykorzystanie istniejącego repozytorium DeepSpeech:
https://github.com/mozilla/DeepSpeech 
 
W celu transkrypcji mowy z dziesięciu przygotowanych nagrań. 
Wykorzystano pre-trenowany model dostępny dzięki twórcom użyte repozytorium, dodatkowo rozpoznawanie mowy zostało wzmocnione modelem językowym również dostarczonym przez twórców DeepSpeech.

Po uruchomienu ``task_project.py`` transkrypcje zostają zapisane do pliku ``results.csv``.

#Przebieg instalacji 
1. Zainstalować biblioteki zgodnie z plikiem ``requirements.txt``:

```
 pip install -r requirements.txt
```

2. Pobrać model rozpoznawania mowy wraz z modelem językowym korzystając z terminala:

```
 python -m wget https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.pbmm
 
 python -m wget https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.scorer
```
3. Uruchomić plik ``task_project.py`` 
Badane pliki powinny znajdować się w folderze ``test_wavs`` - cały ten folder powinnien zostać przebadany. 

# [Zadanie Python]
Wszystko zawarte w pliku ``staz.ipynb``

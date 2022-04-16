# Django

## Spuštění serveru
    cd website
    py manage.py runserver

## Údaje superuživatele

>name: admin
>
>password: admin

## Bugy a chyby

- obrázky .png se nestahují
    - Řešení: připsat podmínku do etesty.py ```def download_image``` a spustit celý skript znovu
- nestahují se videa
# Django

## Spuštění serveru
    cd website
    py manage.py runserver

## Údaje superuživatele

>name: admin
>
>password: admin

## Bugy a chyby

- scrapers/etesty.py nepřiřazuje obrázky
    - Řešení: přidat nový sloupec do etesty.csv a případně do něj zapsat cestu obrázku
- pokud jsou všechny odpovědi . , scraper pokaždé přiřadí správnou odpověď a
- index.html zobrazuje C none
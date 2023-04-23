## Запуск джанги

`source ./venv/Scripts/activate` - для запуска venv

`set -a; source .env; set +a;` - чтобы подгрузить переменные окружения
 -a  Mark variables which are modified or created for export.
Using + rather than - causes these flags to be turned off.

`./manage.py shell` - запустить шел

## Запуск сайта

`python manage.py runserver`

Добавляем партнера Frigate

Добавляем платежное средство FreeKassa

Запускаем шел

```python
from proxylab import di

di.partner.update_partners_data()
di.partner.update_availability()
```

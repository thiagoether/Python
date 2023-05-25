import datetime import date

# METODO 1
currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
year = date.strftime("%Y")
print(f"Current Year -> {year}")
# METODO 2
date = datetime.date.today()
year = date.strftime("%Y")
print(f"Current Year -> {year}")

# METODO 3
currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
print(f"Current Year -> {date.year}")

# METODO 4
from datetime import date

ano_atual = date.today().year
print(ano_atual)

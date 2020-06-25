# Instagram bot basico
Creamos un bot para Instagram basado en Python 3.6+ y Selenium.

## Instalacion
Este proyecto usa pipenv para manejar las librerias en las que depende el bot. Lo primero que debes hacer es descargar pipenv y luego correr una instalacion en la carpeta madre del proyecto.
`pip3 install pipenv` #linux (Recuerda agregarlo al $PATH)
`pip install pipenv` #windows

`pipenv install`

Tambien debes descargarte Geckodriver(Firefox)


## Uso
Hemos implementado un menu basico en la linea de comando que va a intanciar el bot. Para correrlo usa:
`pipenv shell`
`python app.py`

##Uso avanzado
Nuestro menu solo incorpora un par de usos. Tenemos unas cuantas funcionalidades adicionales para esto puedes correr una sesion interactiva e importar la clase Bot.
`python -i`

```
from Engine import bots
mi_bot = bots.Bot("","") #aca usuario y contrasena
mi_bot.enter()

#de aca queda a tu discrecion

mi_bot.go_to("google") #esto envia al bot a https://www.instagram.com/google

```


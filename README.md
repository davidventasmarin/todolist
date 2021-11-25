# TODO-LIST🚀

## Descripción ✍️
_Este es el resultado de lo que voy aprendiendo del libro **Test-Driven Development with Python**_
_, desea ver el contenido del libro está [aquí](https://www.obeythetestinggoat.com/pages/book.html#toc)_
_si deseas comprarlo en físico está disponible [aquí](https://www.obeythetestinggoat.com/pages/book.html)_
_el contenido de esté libro te ayuda a desarrollar una aplicación útil mediante el TDD_

## Comenzando
---

### Pre-requisitos 📃
_Primero, debemos de comprobar que tenemos instalado Python versión 3 en adelante, para ello debemos de poner el comando de abajo en nuestra consola de comandos, para ver si tenemos instalado Python y que versión tenemos._
```
python --version
```
_Cumplido este requisito, ahora ya vamos a lo que tiene que ver con el proyecto en sí, para ello hacemos los pasos que tenemos en el apartado de Instalación_

## Warning ⚠️
Sí nos sale un error, difícil de leer, debemos de comprobar que la versión que tenemos de Django es la adecuada. Muchas veces cuando instalamos paquetes, lo hacemos para el sistema entero, lo que nosotros nos debemos acostumbrar cuando desarrollamos en Python es en usar los entornos virtuales.  
Para solucionar esto lo único que debemos hacer es comprobar primero que versión tenemos de Django, si es incorrecta la hemos de borrar, e instalar la versión adecuada. debemos de seguir los siguientes pasos en orden.

```
pip freeze 
pip uninstall django
pip install -r requeriments.txt
```

### Instalación 🧰
_Descargamos el proyecto_
```
git clone https://github.com/davidventasmarin/todolist.git
```
_Luego debemos de crear el entorno virtual_
```
python -m venv todolist-env
```
_Después para activar el entorno debemos de seguir los siguientes pasos en el caso de **Linux**._  
1. cd todolist-env
2. cd bin
3. source activate
4. Volvemos al directorio del proyecto    

_En el caso de **Windows** hacer los siguientes pasos_  
1. cd todolist-env
2. cd scripts
3. activate
   
_Esto hará que se active la variable de entorno de Python_  
_Instalamos el archivo requeriments.txt con todos los paquetes que vamos a necesitar._
```
pip install -r requeriments.txt
```
_Una ya tenemos hecho esto, para comprobar que todo está bien debemos de ejecutar los test unitarios, que es la forma en la que se puede comprobar rápidamente que nos está funcionando todo_
```
python manage.py test lists
```

Pruebas Unitarias 🧪

## Expresiones de Gratitud 🎁
* Habla a otras personas de este proyecto.📢
* Dá feedback al precioso ser de luz que está aprendiendo. Para animarle a mejorar. 👍
* Comentame lo que desees en cualquiera de las redes sociales. 🗨️
  





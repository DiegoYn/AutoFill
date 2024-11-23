
# AutoFill
Auto completar encuestas Docentes UTN frba

## Requisitos

python 3.8 o superior

[Python](https://www.python.org/downloads/windows/)

Instala las dependencias

request y beautifulsoup4
```bash
pip install requests beautifulsoup4
```
o

```bash
python3 -m pip install requests beautifulsoup4
```


Abrí una terminal donde hayas descargado el archivo encuesta.py y ejecuta
```bash
python encuesta.py
```
o
```bash
python3 encuesta.py
```

## Uso

Necesitas el link original a la encuesta , este lo encontras de la siguiente manera

Click derecho en la encuesta e inspeccionar elemento
![image](https://github.com/user-attachments/assets/04eb68fc-2e14-43f8-8496-011235d9fd85)


casi al principio se encuentra el iframe que contiene el link a la encuesta original
![image1](https://github.com/user-attachments/assets/91d2cbbf-8a88-456a-aad0-4caa32c7b3e5)



Ejecutas el script y pegas el link

ingresas un valor entre 0 y 10 , siendo 0 marcar los botones con la opcion No opina y siendo 10 marcando 100%.

Escriben si y se envia el formulario , luego solo basta recargar su pagina del siu para ver que la encuesta se respondió correctamente


Por defecto los text area de las ultimas 3 preguntas se rellenan con "No opina" si quieren personalizarlo pueden abrir el archivo con cualquier editor de texto y cambiar 
form_data[textarea["name"]] = "No opina" 
y cambiar el mensaje





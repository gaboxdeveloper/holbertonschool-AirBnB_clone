# Holbertonschool-AirBnB_clone

## HBNBCommand Console Module

Este módulo de consola, `HBNBCommand`, es una parte integral de nuestro proyecto. Proporciona una interfaz de línea de comandos para interactuar con nuestras clases y objetos.

### Características

- **Prompt personalizado**: Nuestra consola tiene un prompt personalizado `(hbnb) ` para mejorar la experiencia del usuario.
- **Clases soportadas**: Soporta varias clases, incluyendo `BaseModel`, `Amenity`, `City`, `Place`, `State`, `User` y `Review`.
- **Comandos disponibles**: Los comandos disponibles incluyen `quit`, `EOF`, `create`, `show`, `destroy`, `all` y `update`.

### Uso

Para usar este módulo, simplemente ejecuta el script de Python en tu terminal:
console.py

Para crear una nueva instancia de una clase:
```python
(hbnb) create BaseModel
```
Para mostrar información sobre una instancia específica:
```python
(hbnb) show BaseModel 1234-1234-1234
```
Para eliminar una instancia específica:
```python
(hbnb) destroy BaseModel 1234-1234-1234
```
Para mostrar todas las instancias de una clase:
```python
(hbnb) all BaseModel
```
Para actualizar un atributo en una instancia específica:
```python
(hbnb) update BaseModel 1234-1234-1234 first_name "John"
```

## BaseModel Class

Este es un módulo de Python que define una clase base para modelos. La clase `BaseModel` proporciona funcionalidades básicas para la creación y gestión de instancias de modelos.

### Características

- **Constructor**: El constructor de la clase acepta argumentos posicionales y de palabras clave. Si se proporcionan argumentos de palabras clave, se establecen como atributos del objeto. Si no se proporcionan argumentos, se generan valores predeterminados para `id`, `created_at`, `updated_at`, `my_number` y `name`.

- **Representación de cadena**: La clase tiene un método `__str__` que devuelve una representación de cadena del objeto.

- **Guardar**: El método `save` actualiza el atributo `updated_at` con la hora actual y guarda el objeto.

- **A diccionario**: El método `to_dict` convierte el objeto a un diccionario.

### Uso

Para utilizar esta clase, simplemente importa el módulo y crea una instancia del modelo:

```python
from base_model import BaseModel

model = BaseModel(name="Mi modelo", my_number=42)

print(model.name)  # Imprime: Mi modelo
model.save()  # Actualiza `updated_at` y guarda el modelo

dict_model = model.to_dict()
print(dict_model)
```

## Clase FileStorage

La clase `FileStorage` es una parte esencial de nuestro proyecto. Proporciona una forma de almacenar y recuperar objetos en un archivo JSON.

### Características

- **Almacenamiento de objetos**: Todos los objetos se almacenan en un diccionario privado `__objects`.
- **Archivo JSON**: Los objetos se almacenan en un archivo JSON, cuya ruta se guarda en la variable privada `__file_path`.

### Métodos

- **all()**: Este método devuelve el diccionario completo de objetos.
- **new(obj)**: Este método agrega un nuevo objeto al diccionario de objetos.
- **save()**: Este método guarda todos los objetos en el archivo JSON. Los objetos se convierten a un formato de diccionario antes de ser guardados.
- **classeneitor(class_name)**: Este método devuelve la clase correspondiente a un nombre de clase dado.
- **reload()**: Este método carga todos los objetos desde el archivo JSON al diccionario de objetos.

### Uso

Para usar esta clase, simplemente importa la clase `FileStorage` en tu script y crea una nueva instancia:

```python
from models.file_storage import FileStorage

storage = FileStorage()

# Crear un nuevo objeto
obj = BaseModel()
storage.new(obj)

# Guardar todos los objetos en el archivo JSON
storage.save()

# Recargar todos los objetos desde el archivo JSON
storage.reload()

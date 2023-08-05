# Laboratorio 1 

## Autores 

- Fredy Velasquez
- Jorge Caballeros

# Sistema de tipos

Para las especificaciones y contexto del laboratorio se construyó el siguiente sistema básico:

## Tipos básicos

### 1. int:
   - **Definición**: Números enteros
   - **Estructura**: `[0-9]`

### 2. string:
   - **Definición**: Cadena de caracteres
   - **Estructura**: `[a-zA-Z0-9]`

### 3. bool:
   - **Definición**: Valores booleanos. True or False.
   - **Valores**: `true`, `false`

## Reglas de ámbito

Se maneja un ámbito estático dado que se realiza el estudio de un programa fuente en forma estática y no en tiempo de ejecución.

## Reglas de tipos

Donde:
- A: Variable
- B: Variable

### 1. Operaciones entre int:

   a. Si A es int y B es int, entonces la suma de esas dos variables es int  
   b. Si A es int y B es int, entonces la resta de esas dos variables es int  
   c. Si A es int y B es int, entonces la multiplicación de esas dos variables es int  
   d. Si A es int y B es int, entonces la división de esas dos variables es int (dado que no hay float en YAPL)

### 2. Operaciones entre string:

   a. Si A es string y B es string, la suma de esas dos variables es string (operación también llamada “concatenación”)  
   b. Si A es string y B es string, la resta de esas dos variables es ERROR  
   c. Si A es string y B es string, la multiplicación de esas dos variables es ERROR  
   d. Si A es string y B es string, la división de esas dos variables es ERROR  

### 3. Operaciones entre int y string:

   a. Si A es string y B es int, la suma de esas dos variables es ERROR  
   b. Si A es string y B es int, la resta de esas dos variables es ERROR  
   c. Si A es string y B es int, la multiplicación de esas dos variables es string pero multiplicado por la cantidad estipulada por B  
   d. Si A es string y B es int, la división de esas dos variables es ERROR  

### 4. Operaciones entre bool:

   a. Si A es bool y B es bool, la suma de esas dos variables es ERROR  
   b. Si A es bool y B es bool, la resta de esas dos variables es ERROR  
   c. Si A es bool y B es bool, la multiplicación de esas dos variables es ERROR  
   d. Si A es bool y B es bool, la división de esas dos variables es ERROR  
   e. Si A es bool y B es bool, la operación AND da como resultado bool  
   f. Si A es bool y B es bool, la operación OR da como resultado bool  

### 5. Tabla de símbolos

   - **Definición**: La tabla de símbolos es una estructura de datos utilizada para tener un control sobre métodos, variables y clases en el programa. Si la implementación es en python se puede utilizar un formato de clave-valor, tal como lo es un diccionario, en Javascript, por ejemplo, podría utilizarse un objeto.

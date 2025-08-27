# Máquina de Turing Aritmética

Creado por:
Juan Joya
, Santiago Diaz
, Johan Garcia

Una implementación en Python de una máquina de Turing que puede realizar operaciones aritméticas básicas: suma, resta, multiplicación y división.

## Descripción

Este programa simula el funcionamiento de una máquina de Turing para procesar operaciones matemáticas. La máquina utiliza una cinta infinita, un cabezal de lectura/escritura y un conjunto de estados para procesar las operaciones de forma similar a como lo haría una máquina de Turing real.

## Características

- **Operaciones soportadas**: Suma (+), Resta (-), Multiplicación (*), División (/)
- **Números enteros**: Positivos y negativos
- **Simulación completa**: Incluye cinta, cabezal, estados y transiciones
- **Representación unaria**: Convierte resultados a formato unario como referencia
- **Manejo de errores**: División por cero y formato inválido
- **Interfaz de consola**: Entrada interactiva por línea de comandos

## Requisitos

- Python 3.x
- No requiere librerías externas

## Instalación

1. Descarga el archivo `maquina_turing_aritmetica.py`
2. Asegúrate de tener Python 3 instalado en tu sistema

## Uso

### Ejecutar el programa

```bash
python maquina_turing_aritmetica.py
```

### Formato de entrada

```
numero operador numero
```

### Ejemplos válidos

```
5+3
10-7
4*6
15/3
8+(-2)
(-5)*3
```

### Comandos especiales

- `salir`: Termina el programa

## Funcionamiento

### Componentes de la Máquina de Turing

1. **Cinta**: Almacena la operación de entrada y procesa los datos
2. **Cabezal**: Lee y escribe símbolos en la cinta
3. **Estados**: Controla el flujo de procesamiento
4. **Transiciones**: Define cómo la máquina cambia de estado

### Estados principales

- `inicio`: Estado inicial
- `suma`: Procesando suma
- `resta`: Procesando resta
- `multiplicacion`: Procesando multiplicación
- `division`: Procesando división
- `suma_final`, `resta_final`, `mult_final`, `div_final`: Estados finales exitosos
- `error`: Estado de error

### Algoritmos implementados

- **Suma y resta**: Operación directa con manejo de signos
- **Multiplicación**: Mediante sumas repetidas (simulando comportamiento real de MT)
- **División**: Mediante restas repetidas (simulando comportamiento real de MT)

## Ejemplo de ejecución

```
CALCULADORA CON MAQUINA DE TURING
Operadores: + - * /
Formato: numero operador numero
Ejemplos: 5+3, 10-7, 4*6, 15/3
Escribe 'salir' para terminar
----------------------------------------

Operacion: 5+3
Ejecutando: 5+3
Cinta inicial: 5+3#
Operandos: 5 + 3
Estado de procesamiento: suma_final
Representación unaria del resultado: 11111111
Resultado: 8

Operacion: 12/4
Ejecutando: 12/4
Cinta inicial: 12/4#
Operandos: 12 / 4
Estado de procesamiento: div_final
Representación unaria del resultado: 111
Resultado: 3

Operacion: salir
Programa terminado.
```

## Estructura del código

### Clase principal: `MaquinaTuringAritmetica`

- `inicializar_cinta(operacion)`: Prepara la cinta con la operación
- `leer_simbolo()`: Lee el símbolo actual del cabezal
- `escribir_simbolo(simbolo)`: Escribe un símbolo en la posición actual
- `mover_cabezal(direccion)`: Mueve el cabezal izquierda o derecha
- `parsear_entrada()`: Extrae números y operador de la entrada
- `convertir_a_unario(numero)`: Convierte número a representación unaria
- `sumar(num1, num2)`: Ejecuta operación de suma
- `restar(num1, num2)`: Ejecuta operación de resta
- `multiplicar(num1, num2)`: Ejecuta multiplicación mediante sumas
- `dividir(num1, num2)`: Ejecuta división mediante restas
- `ejecutar(operacion)`: Función principal que procesa la operación completa

### Función principal: `calculadora_interactiva()`

Maneja la interfaz de usuario y el bucle principal del programa.

## Limitaciones

- Solo procesa números enteros
- La división devuelve solo la parte entera (sin decimales)
- Los números muy grandes pueden afectar el rendimiento en multiplicación y división

## Manejo de errores

- **División por cero**: Retorna mensaje de error
- **Formato inválido**: Detecta entrada mal formateada
- **Operadores no válidos**: Rechaza operadores no soportados
- **Interrupciones**: Maneja Ctrl+C de forma elegante


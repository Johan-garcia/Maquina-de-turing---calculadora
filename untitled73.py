

class MaquinaTuringAritmetica:
    def __init__(self):
        self.cinta = []
        self.cabezal = 0
        self.estado = 'inicio'
        self.estados_finales = {'suma_final', 'resta_final', 'mult_final', 'div_final', 'error'}

    def inicializar_cinta(self, operacion):
        """Inicializa la cinta con la operación en formato: num1 op num2"""
        self.cinta = list(operacion.replace(' ', '')) + ['#']  # # marca el final
        self.cabezal = 0
        self.estado = 'inicio'

    def leer_simbolo(self):
        """Lee el símbolo actual en la posición del cabezal"""
        if self.cabezal >= len(self.cinta):
            return '#'
        return self.cinta[self.cabezal]

    def escribir_simbolo(self, simbolo):
        """Escribe un símbolo en la posición actual del cabezal"""
        if self.cabezal >= len(self.cinta):
            self.cinta.extend(['#'] * (self.cabezal - len(self.cinta) + 1))
        self.cinta[self.cabezal] = simbolo

    def mover_cabezal(self, direccion):
        """Mueve el cabezal: 'D' (derecha), 'I' (izquierda)"""
        if direccion == 'D':
            self.cabezal += 1
        elif direccion == 'I' and self.cabezal > 0:
            self.cabezal -= 1

    def parsear_entrada(self):
        """Parsea la entrada para extraer números y operación"""
        entrada = ''.join(self.cinta).replace('#', '')

        # Buscar el operador
        operadores = ['+', '-', '*', '/']
        operador = None
        pos_op = -1

        # Buscar operador (excluyendo el primer carácter que puede ser signo negativo)
        for i, char in enumerate(entrada[1:], 1):
            if char in operadores:
                operador = char
                pos_op = i
                break

        if operador is None:
            return None, None, None

        try:
            num1 = int(entrada[:pos_op])
            num2 = int(entrada[pos_op + 1:])
            return num1, operador, num2
        except ValueError:
            return None, None, None

    def convertir_a_unario(self, numero):
        """Convierte un número decimal a representación unaria usando '1'"""
        if numero == 0:
            return '0'
        elif numero > 0:
            return '1' * numero
        else:
            return '-' + '1' * abs(numero)

    def convertir_de_unario(self, unario):
        """Convierte de unario a decimal"""
        if unario == '0':
            return 0
        elif unario.startswith('-'):
            return -len(unario[1:])
        else:
            return len(unario)

    def sumar(self, num1, num2):
        """Simula suma en máquina de Turing"""
        if num1 >= 0 and num2 >= 0:
            resultado = num1 + num2
        elif num1 < 0 and num2 < 0:
            resultado = num1 + num2
        else:
            resultado = num1 + num2

        return resultado

    def restar(self, num1, num2):
        """Simula resta en máquina de Turing"""
        return num1 - num2

    def multiplicar(self, num1, num2):
        """Simula multiplicación mediante sumas repetidas"""
        if num2 == 0 or num1 == 0:
            return 0

        resultado = 0
        multiplicando = abs(num1)
        multiplicador = abs(num2)

        # Simulamos la multiplicación como sumas repetidas
        for _ in range(multiplicador):
            resultado += multiplicando

        # Determinar el signo del resultado
        if (num1 < 0 and num2 > 0) or (num1 > 0 and num2 < 0):
            resultado = -resultado

        return resultado

    def dividir(self, num1, num2):
        """Simula división mediante restas repetidas"""
        if num2 == 0:
            return "Error: División por cero"

        if num1 == 0:
            return 0

        dividendo = abs(num1)
        divisor = abs(num2)
        cociente = 0

        # Simulamos la división como restas repetidas
        while dividendo >= divisor:
            dividendo -= divisor
            cociente += 1

        # Determinar el signo del resultado
        if (num1 < 0 and num2 > 0) or (num1 > 0 and num2 < 0):
            cociente = -cociente

        return cociente

    def ejecutar(self, operacion):
        """Ejecuta la operación completa"""
        print(f"Ejecutando: {operacion}")

        # Inicializar la cinta
        self.inicializar_cinta(operacion)
        print(f"Cinta inicial: {''.join(self.cinta)}")

        # Parsear la entrada
        num1, operador, num2 = self.parsear_entrada()

        if num1 is None:
            return "Error: Formato de entrada inválido"

        print(f"Operandos: {num1} {operador} {num2}")

        # Ejecutar la operación correspondiente
        if operador == '+':
            self.estado = 'suma'
            resultado = self.sumar(num1, num2)
            self.estado = 'suma_final'
        elif operador == '-':
            self.estado = 'resta'
            resultado = self.restar(num1, num2)
            self.estado = 'resta_final'
        elif operador == '*':
            self.estado = 'multiplicacion'
            resultado = self.multiplicar(num1, num2)
            self.estado = 'mult_final'
        elif operador == '/':
            self.estado = 'division'
            resultado = self.dividir(num1, num2)
            if isinstance(resultado, str):  # Error
                self.estado = 'error'
                return resultado
            self.estado = 'div_final'
        else:
            self.estado = 'error'
            return "Error: Operador no reconocido"

        # Mostrar el proceso de la máquina de Turing
        print(f"Estado de procesamiento: {self.estado}")
        print(f"Representación unaria del resultado: {self.convertir_a_unario(resultado)}")

        return resultado

    def mostrar_estado(self):
        """Muestra el estado actual de la máquina"""
        print(f"Estado: {self.estado}")
        print(f"Cinta: {''.join(self.cinta)}")
        print(f"Cabezal en posición: {self.cabezal}")
        if self.cabezal < len(self.cinta):
            print(f"Símbolo actual: {self.cinta[self.cabezal]}")


# Función para demostrar el uso de la máquina de Turing
def demostrar_maquina_turing():
    mt = MaquinaTuringAritmetica()

    operaciones = [
        "5+3",
        "10-4",
        "6*7",
        "15/3",
        "8+(-2)",
        "(-5)*3",
        "12/4"
    ]

    print("=== DEMOSTRACIÓN DE MÁQUINA DE TURING ARITMÉTICA ===\n")

    for op in operaciones:
        print(f"{'='*50}")
        resultado = mt.ejecutar(op)
        print(f"Resultado: {resultado}")
        print(f"Estado final: {mt.estado}")
        print()

# Función interactiva principal
def calculadora_interactiva():
    mt = MaquinaTuringAritmetica()

    print("CALCULADORA CON MAQUINA DE TURING")
    print("Operadores: + - * /")
    print("Formato: numero operador numero")
    print("Ejemplos: 5+3, 10-7, 4*6, 15/3")
    print("Escribe 'salir' para terminar")
    print("-" * 40)

    while True:
        try:
            operacion = input("\nOperacion: ").strip()

            if operacion.lower() == 'salir':
                print("Programa terminado.")
                break

            if not operacion:
                print("Error: Ingresa una operacion valida.")
                continue

            resultado = mt.ejecutar(operacion)
            print(f"Resultado: {resultado}")

        except KeyboardInterrupt:
            print("\nPrograma interrumpido.")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    # Solo ejecutar calculadora interactiva
    calculadora_interactiva()

import random
import statistics

def analizar_numeros_aleatorios():
    print("==================================================")
    print("   PROGRAMA DE ANÁLISIS ESTADÍSTICO DE DATOS      ")
    print("==================================================\n")
    
    # 1. Generar 50 dígitos (números enteros) aleatorios entre 1 y 100
    # Usamos una lista de comprensión que se repite 50 veces
    numeros = [random.randint(1, 100) for _ in range(50)]
    
    # 2. Realizar los cálculos estadísticos usando la librería 'statistics'
    media = statistics.mean(numeros)
    mediana = statistics.median(numeros)
    
    # 'multimode' maneja correctamente situaciones donde hay más de una moda
    modas = statistics.multimode(numeros) 
    
    # Se calcula la varianza y desviación estándar muestral (dividido entre N-1)
    varianza = statistics.variance(numeros)
    desviacion_estandar = statistics.stdev(numeros)
    
    # 3. Mostrar los resultados en la consola con un formato limpio
    print("--- Datos Generados ---")
    print(f"Lista de números:\n{numeros}\n")
    
    print("--- Métricas Estadísticas ---")
    print(f"• Media (Promedio):      {media:.2f}")
    print(f"• Mediana (Valor medio):  {mediana:.2f}")
    print(f"• Moda(s) (Más repetido): {modas}")
    print(f"• Varianza Muestral:      {varianza:.2f}")
    print(f"• Desviación Estándar:    {desviacion_estandar:.2f}")
    print("==================================================")

# Ejecutar la función principal si el script se corre directamente
if __name__ == "__main__":
    analizar_numeros_aleatorios()
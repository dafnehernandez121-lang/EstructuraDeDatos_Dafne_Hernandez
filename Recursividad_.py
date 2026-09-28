import time

def intentar_tarea(tarea, nivel_estres):
    """
    Simula intentar hacer un quehacer en casa. 
    Retorna el nivel de estrés resultante (número entero).
    """
    inicio_tarea = time.perf_counter() 

    if nivel_estres <= 0:
        print(f"   ¡Haz completado la tarea en paz!: {tarea}")
        fin_tarea = time.perf_counter()
        print(f"   [Tiempo de ejecución - {tarea}: {fin_tarea - inicio_tarea:.4f}s]\n")
        return 0 
        
    print(f"-> Intento hacer: '{tarea}' (Estrés actual: {nivel_estres})")
    time.sleep(1) 
    
    nuevo_estres = 0

    if tarea == "Cambiar el foco fundido":
        print("    Ups, necesito la escalera, pero el garaje está hecho un desastre.")
        nuevo_estres = intentar_tarea(
            "Limpiar el garaje", 
            intentar_tarea("Buscar las llaves del garaje", nivel_estres - 1)
        )
        
    elif tarea == "Limpiar el garaje":
        print("    Ups, para limpiar el garaje necesito mover el auto, pero no tiene batería.")
        nuevo_estres = intentar_tarea(
            "Pasar corriente al auto",
            intentar_tarea("Pedir cables al vecino", nivel_estres - 1)
        )
        
    elif tarea == "Buscar las llaves del garaje":
        print("    Las llaves no están. Las dejé en el pantalón de ayer.")
        nuevo_estres = intentar_tarea(
            "Buscar en el cesto de ropa sucia",
            intentar_tarea("Distraerse viendo el celular", nivel_estres - 1)
        )
        
    else:
        print(f"    Logré resolver este obstáculo: {tarea}. (Me calmo un poco)")
        nuevo_estres = nivel_estres - 1 

    fin_tarea = time.perf_counter()
    print(f"   [Tiempo de ejecución - {tarea}: {fin_tarea - inicio_tarea:.4f}s]\n")
    
    return nuevo_estres 


print("ES SÁBADO POR LA MAÑANA")
print("Objetivo: Realizar el Cambio del foco fundido de la sala.\n")

tiempo_inicio_total = time.perf_counter()

estres_inicial = 2
estres_final = intentar_tarea("Cambiar el foco fundido", estres_inicial)

tiempo_fin_total = time.perf_counter()
tiempo_total = tiempo_fin_total - tiempo_inicio_total

print("==========================================")
if estres_final <= 0:
    print("Conclusión: Lograste hacer los quehaceres y te fuiste a descansar.")
else:
    print("Conclusión: Terminaste haciendo de todo, menos cambiar el foco.")

print(f"Tiempo total de la cadena de tareas: {tiempo_total:.4f} segundos")
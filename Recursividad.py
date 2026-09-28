import time

def intentar_tarea(tarea, nivel_estres):
    """
    Simula intentar hacer un quehacer en casa. 
    Retorna el nivel de estrés resultante (número entero).
    """
 
    if nivel_estres <= 0:
        print(f"   ¡Haz completado la tarea en paz!: {tarea}\n")
        return 0 
        
    print(f"-> Intento hacer: '{tarea}' (Estrés actual: {nivel_estres})")
    time.sleep(1) 
    

    if tarea == "Cambiar el foco fundido":
        print("    Ups, necesito la escalera, pero el garaje está hecho un desastre.")
        

        return intentar_tarea(
            "Limpiar el garaje", 
            intentar_tarea("Buscar las llaves del garaje", nivel_estres - 1)
        )
        
    elif tarea == "Limpiar el garaje":
        print("    Ups, para limpiar el garaje necesito mover el auto, pero no tiene batería.")
        

        return intentar_tarea(
            "Pasar corriente al auto",
            intentar_tarea("Pedir cables al vecino", nivel_estres - 1)
        )
        
    elif tarea == "Buscar las llaves del garaje":
        print("    Las llaves no están. Las dejé en el pantalón de ayer.")
        
        return intentar_tarea(
            "Buscar en el cesto de ropa sucia",
            intentar_tarea("Distraerse viendo el celular", nivel_estres - 1)
        )
        
    else:
        print(f" Logré resolver este obstáculo: {tarea}. (Me calmo un poco)")
        return nivel_estres - 1 


print("ES SÁBADO POR LA MAÑANA")
print("Objetivo: Realizar el Cambio del foco fundido de la sala.\n")

estres_inicial = 2
estres_final = intentar_tarea("Cambiar el foco fundido", estres_inicial)

print("==========================================")
if estres_final <= 0:
    print("Conclusión: Lograste hacer los quehaceres y te fuiste a descansar.")
else:
    print("Conclusión: Terminaste haciendo de todo, menos cambiar el foco.")
##################################################################################################################################################
#Alumno(a): HERNANDEZ CETZAL DAFNE MARIVY
#Correo: LE25081275@merida.tecnm.mx
#Fecha: 08-09-2026
##################################################################################################################################################
def Memoria_Estatica():    
    calificaciones=[0]*5
    for i in range(5):
        calificacion=int(input(f"Captura la calificacion {i+1}: "))
        calificaciones[i]=calificacion
    print("Calificaciones:", calificaciones) #EL CÓDIGO DEL VIDEO NO IMPRIME LAS CALIFICACIONES
if __name__ == "__main__":
    Memoria_Estatica()


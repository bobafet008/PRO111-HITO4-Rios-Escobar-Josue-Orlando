print("=" * 60)
print("  CONTROL DE ASISTENCIA Y RENDIMIENTO")
print("  Academia de Capacitacion")
print("=" * 60)
# Contadores
estudiantes= 0
aprobados= 0
reprobados_nota= 0
reprobados_asist= 0
contador_estudiante = 0
clases = 0
clases_asistidas = 0
# Permitir registrar varios hasta que decida irse
continuar = "s"
while continuar == "s":
    contador_estudiante = contador_estudiante + 1
    
    print("")
    print("-" * 60)
    print("ESTUDIANTE " + str(contador_estudiante))
    print("-" * 60)
    
    nombre = input("Nombre completo: ")
    # Cantidad de Clases
    clases = 0
    while clases == 0:
        clases_texto = input("Cantidad total de clases : ")
        clases = int(clases_texto)
        if clases > 0:
            clases = clases
        else:
            print("Error: debe ser mayor a 0")
    # Asistencias de esa clase
    clases_asistidas = 0
    while clases_asistidas == 0:
        clases_asistidas_texto = input("Cantidad de clases asistidas: ")
        clases_asistidas = int(clases_asistidas_texto)
        if clases_asistidas >= 0 and clases_asistidas <= clases:
            clases_asistidas = clases_asistidas
        else:
            print("Error: debe estar entre 0 y " + str(clases))
    # Notas
    Notas = 0
    while Notas == 0:
        nota_texto = input("Calificacion final (0-100): ")
        nota = float(nota_texto)
        if nota >= 0 and nota <= 100:
            Notas = 1
        else:
            print("Error: la calificacion debe estar entre 0 y 100")
    # porcentaje asistencia
    porcentaje_asistencia = (clases_asistidas / clases) * 100
    #Determinar si esta reprobado 
    if porcentaje_asistencia < 80:
        condicion = "Reprobado por asistencia"
        reprobados_asist= reprobados_asist + 1
    elif nota >= 51:
        condicion = "Aprobado"
        aprobados = aprobados + 1
    else:
        condicion = "Reprobado por nota"
        reprobados_nota = reprobados_nota + 1
    estudiantes = estudiantes + 1
    #mostrar datos
    print("\n")
    print("RESULTADO: " + nombre)
    print( "-" * 60)
    print("Asistencia: " + str(clases_asistidas) + "/" + str(clases) + " clases")
    print("Porcentaje de asistencia: " + str(porcentaje_asistencia) + "%")
    print("Calificacion: " + str(nota) + "/100")
    print("Condicion: " + condicion)
    print("\n")
    # bucle si desea meter a otro estudiante
    continuar = input("¿Desea registrar otro estudiante? (s/n): ")
    if continuar != "s":
        continuar = "n"
#mostrar datos si no desea meter a otro estudiante
print("\n")
print("=" * 60)
print("Registro final")
print("=" * 60)
print("Total de estudiantes procesados: " + str(estudiantes))
print("Estudiantes aprobados: " + str(aprobados))
print("Estudiantes reprobados por nota: " + str(reprobados_nota))
print("Estudiantes reprobados por asistencia: " + str(reprobados_asist))
# Calcular aprobados
if estudiantes > 0:
    porcentaje_aprobados = (aprobados / estudiantes) * 100
else:
    porcentaje_aprobados = 0
print("Porcentaje de aprobados: " + str(porcentaje_aprobados) + "%")
print("=" * 60)
print("\n")

print("=" * 60)
print("  CONTROL DE ASISTENCIA Y RENDIMIENTO")
print("  Academia de Capacitacion")
print("=" * 60)

# Contadores
estudiantes= 0
aprobados= 0
reprobados_nota= 0
reprobados_asist= 0

# Permitir registrar varios hasta que decida irse
continuar = "s"
contador_estudiante = 0
while continuar == "s":
    contador_estudiante = contador_estudiante + 1
    
    print("")
    print("-" * 60)
    print("ESTUDIANTE " + str(contador_estudiante))
    print("-" * 60)
    
    nombre = input("Nombre completo: ")
    
    # Cantidad de Clases
    clases_programadas_valida = 0
    while clases_programadas_valida == 0:
        clases_programadas_texto = input("Cantidad total de clases programadas: ")
        clases_programadas = int(clases_programadas_texto)
        if clases_programadas > 0:
            clases_programadas_valida = clases_programadas
        else:
            print("Error: debe ser mayor a 0")
    
    # Asistencias de esa clase
    clases_asistidas_valida = 0
    while clases_asistidas_valida == 0:
        clases_asistidas_texto = input("Cantidad de clases asistidas: ")
        clases_asistidas = int(clases_asistidas_texto)
        if clases_asistidas >= 0 and clases_asistidas <= clases_programadas_valida:
            clases_asistidas_valida = clases_asistidas
        else:
            print("Error: debe estar entre 0 y " + str(clases_programadas_valida))
    
    # Notas
    calificacion_valida = 0
    while calificacion_valida == 0:
        calificacion_texto = input("Calificacion final (0-100): ")
        calificacion = float(calificacion_texto)
        if calificacion >= 0 and calificacion <= 100:
            calificacion_valida = 1
        else:
            print("Error: la calificacion debe estar entre 0 y 100")
    
    # Porcentaje asistencia
    porcentaje_asistencia = (clases_asistidas / clases_programadas_valida) * 100
    
    # Determinar si esta reprobado 
    if porcentaje_asistencia < 80:
        condicion = "Reprobado por asistencia"
        reprobados_asist= reprobados_asist + 1
    elif calificacion >= 51:
        condicion = "Aprobado"
        aprobados = aprobados + 1
    else:
        condicion = "Reprobado por nota"
        reprobados_nota = reprobados_nota + 1
    
    estudiantes = estudiantes + 1
    
    # Mostrar datos
    print("\n")
    print("RESULTADO: " + nombre)
    print( "-" * 60)
    print("Asistencia: " + str(clases_asistidas) + "/" + str(clases_programadas_valida) + " clases")
    print("Porcentaje de asistencia: " + str(porcentaje_asistencia) + "%")
    print("Calificacion: " + str(calificacion) + "/100")
    print("Condicion: " + condicion)
    print("\n")
    # Bucle si desea meter a otro estudiante
    continuar = input("¿Desea registrar otro estudiante? (s/n): ")
    if continuar != "s":
        continuar = "n"

# Mostrar datos si no desea meter a otro estudiante
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

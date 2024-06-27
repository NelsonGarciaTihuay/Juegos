import datetime

fecha = input("Ingrese su fecha de nacimiento (AAA-MM-DD): ")

fech = datetime.datetime.strptime(fecha, "%Y-%m-%d")
dias_de_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Virnes", "Sabado", "Domingo"]
dia_semana = dias_de_semana[fech.weekday()]
print(f"Naciste un {dia_semana}.")

import random

f = open ('./crear_alumnos.sql','a')
data_base=input("nombre de la base de datos: ")
database = """create database {};
			use {};""".format(data_base,data_base)

create_table=input("nombre de la tabla: ")
creartable="""create table {}(
			id_{} int auto_increment primary key,
			nombre varchar(50)not null,
			apellido varchar(50)not null,
			dni int not null,
			fecha_nacimiento date);""".format(create_table,create_table)

f.write(database)
f.write(creartable)

apellidos=[]
nombres=[]
fechas=[]
dni=[]
while True:
	nom=input("ingrese nombre de {}: ".format(create_table))
	apel=input("ingrese apellido de {}: ".format(create_table))
	print("ingrese fecha de nacimiento: ")
	dia=int(input("ingrese dia: "))
	mes=int(input("ingrese mes: "))
	año=int(input("ingrese año: "))
	fecha = "{}/{}/{}".format(año, mes, dia)
	doc=int(input("ingrese dni sin puntos: "))
	nombres.append(nom)
	apellidos.append(apel)
	fechas.append(fecha)
	dni.append(doc)
	opcion=int(input("desea ingresar mas {}?: 1-s/2-n: ".format(create_table)))
	if opcion==1:
		True
	else:
		break		

for x in range(0,len(nombres)):
		
	table="""
			insert into {} (nombre,apellido,dni,fecha_nacimiento) VALUES ("{}","{}",{},"{}");
			""".format(create_table, nombres[x], apellidos[x], dni[x], fechas[x])	

	f.write(table)
f.close()


f = open ('./eliminar_columna.sql','a')
op=int(input("desea eliminar una columna?; 1-si| 2-no"))
if op==1:
	print("id_{}".format(create_table))
	print("nombre")
	print("apellido")
	print("dni")
	print("fecha_nacimiento")
	eliminar=input("escribe la columna que desea eliminar: ")
	eliminar_columna="""alter table {} drop column {};""".format(create_table, eliminar)
f.write(eliminar_columna)
f.close()
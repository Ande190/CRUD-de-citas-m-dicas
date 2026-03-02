
import mysql.connector
#Algoritmo Registro Citas Medicas
#Elabore una aplicacion python que realice que muestre, registre, elimine y actualice citas medicas
#Citas Medicas
#Limpieza de Pantalla
from os import system
reiniciar = "s";
while (reiniciar=="s"):
    #Cadena de Conexion
    conexion1=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="registros_citas")
    #Crear un menu con las operaciones del CRUD
    #Create = crear, Read = select, Update = Actualizar, Delete= Borrar
    # Otras Operaciones show (Mostrar BD existentes), I=Insertar
    print("*********************************************************************************************");
    print("                                          TECNALIA                                           ");
    print("                                         Talento Tech                                        ");
    print("*********************************************************************************************");
    print("                           Administracion y Visualizacion de Datos                           ");
    print("                                      Citas Medicas                                          ");
    print("                               Registro de Citas Medicas                                     ");
    print("*********************************************************************************************");
    print("                                 Administracion de Citas Medicas                             ");
    print("                             1. Mostrar Bases de Datos Disponibles                           ");
    print("                               2. Mostrar Citas Medicas (Select)                             ");
    print("                               3. Insertar Citas Medicas (Insert)                            ");
    print("                               4. Eliminar Citas Medicas (Delete)                            ");
    print("                             5. Actualizar Citas Medicas (Update)                            ");
    print("                             6. Salir del Catalogo de Citas Medicas (break)                  ");
    print("*********************************************************************************************");
    opcion = int(input("Seleccione una opcion del menu (numero de 1 a 6= )"));
    print("*********************************************************************************************");
    system("cls");
    if opcion==1:
        cursor1=conexion1.cursor()
        cursor1.execute("show databases")
        for base in cursor1:
            print(base)
    elif opcion==2:
        cursor1=conexion1.cursor()
        cursor1.execute("select * from registros_citas ")
        for fila in cursor1:
            print(fila);
    elif opcion==3:
        cursor1=conexion1.cursor()
        codigo_usuario = str(input("Digite el codigo del usuario a registrar:"));
        tipo_iden_usu = str(input("Digite el tipo de identificación del usuario a registrar:"));
        num_iden_usu = str(input("Digite el número de identificación del usuario a registrar:"));
        nacionalidad= input("Digite la nacionalidad del usuario a registrar:");
        p_nombre =  input("Digite el primer nombre del usuario a registrar:");
        s_nombre =  input("Digite el segundo nombre del usuario a registrar:");
        p_apellido =  input("Digite el primer apellido del usuario a registrar:");
        s_apellido =  input("Digite el segundo apellido del usuario a registrar:");
        genero =  input("Digite el Genero del usuario a registrar:");
        tipo_cita = input("Digite el tipo de cita que solicita el usuario:");
        codigo_cita = input("Digite el tipo de codigo de cita que solicita el usuario:");
        num_celular = input("Digite el número de celular del usuario a registrar:");
        direccion = input("Digite la dirección del usuario a registra:");
        edad_usuario = input("Digite la edad del usuario a registra:");
        peso_usu = input("Digite el peso del usuario a registra:");
        altura_usu = input("Digite la altura del usuario a registra:");
        fuma = input("Digite si o no, el usuario fuma:");
        bebe = input("Digite si o no, el usuario bebe:");
        consume_dro = input("Digite si o no, el usuario consume drogas:");
        patologias = input("Digite si o no, el usuario tiene patologías:");
        sql="insert into registros_citas values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        datos=(codigo_usuario, tipo_iden_usu, num_iden_usu, nacionalidad, p_nombre, s_nombre,
               p_apellido, s_apellido, genero, tipo_cita, codigo_cita, num_celular, direccion, edad_usuario, peso_usu, altura_usu,fuma,bebe,consume_dro,patologias)
        cursor1.execute(sql, datos)
        conexion1.commit()
    elif opcion==4:
        cursor1=conexion1.cursor()
        codigo1 = input("Digite el codigo del usuario a Borrar:"); 
        sentencia_sql = ''' DELETE FROM registros_citas WHERE codigo_usuario=%s '''
        cursor1.execute(sentencia_sql, (codigo1,))
        conexion1.commit()
        if(cursor1):
            print("Registro Borrado")
        else:
            print("Error en el borrado del Registro")
        conexion1.close()
    elif opcion==5:
        cursor1=conexion1.cursor()
        codigo_usuario = input("Digite el codigo del usuario a Actualizar:");
        codigo1 = input("Digite el nuevo de codigo del usuario:");
        tipo_iden_usu1 = (input("Digite el nuevo tipo de identificación del usuario:"));
        num_iden_usu1 = input("Digite el nuevo número de identificación del usuario:");
        nacionalidad1= input("Digite la nueva nacionalidad del usuario:");
        sentencia_sql = ''' UPDATE registros_citas set codigo_usuario = %s, tipo_iden_usu=%s, num_iden_usu=%s, nacionalidad=%s
                            where codigo_usuario=%s'''
        cursor1.execute(sentencia_sql, (codigo1,tipo_iden_usu1,num_iden_usu1,nacionalidad1, codigo_usuario,))
        conexion1.commit()
        if(cursor1):
            print("Registro Actualizado")
        else:
            print("Error en la actualizacion del Registro")
        conexion1.close()
    reiniciar=input("Desea volver a ejecutar el menu s / n :");

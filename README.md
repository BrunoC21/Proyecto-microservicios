1. Tecnologías: 
Python version 3.10-slim
Framework Flask con imports de:
  -Flask_SQLAlchemy
  -request, jsonify
  -psycopg2-binary
  -request
Docker Desktop
Docker compose
Base de datos PostgresSQL

2. Procesos de prueba Postman:
   2.1. Estudiantes:
     2.1.1 Insertar estudiantes:
       a. Para insertar un nuevo estudiante, primero acceda a Postman e inserte el siguiente link: "http://localhost:5000/estudiantes".
       b. Luego coloca el proceso a la izquierda del link, el metodo POST.
       c. Selecciona la opción BODY, dale click a "raw" y configuralo para texto en formato JSON.
       d. Inserta el código en el siguiente formato, llenalo con los datos que te gusten y haz click en SEND:
          {
            "nombre_completo": "Andrew Jackson",
            "rut": "11345678-9",
            "curso": "Ingenieria Informática",
            "edad": 24
          }
       e. Si el codigo se inserto exitosamente deberia entregar el mensaje: "{"mensaje": "Estudiante creado"}".
     2.1.2 Entregar todos los estudiantes:
       a. Primero acceda a Postman e inserte el siguiente link: "http://localhost:5000/estudiantes".
       b. Luego coloca el proceso a la izquierda del link, el metodo GET.
       c. Haga click en SEND, como resultado deberia entregar cada estudiante que haya insertado hasta el momento.
     2.1.3 Entregar un estudiante por RUT:
       a. Primero acceda a Postman e inserte el siguiente link: "http://localhost:5000/estudiantes/<rut>". En este caso el rut debe estar en el formato "11111111-1"
       b. Luego coloca el proceso a la izquierda del link, el metodo GET.
       c. Haga click en SEND, como resultado deberia entregar el estudiante que posea el rut.
       d. Si no existe el estudiante entregará el mensaje: "{"mensaje": "Estudiante no encontrado"}".
   2.2. Evaluaciones:
     2.2.1 Insertar evaluaciones:
       a. Para insertar un nuevo estudiante, primero acceda a Postman e inserte el siguiente link: "http://localhost:5001/evaluaciones".
       b. Luego coloca el proceso a la izquierda del link, el metodo POST.
       c. Selecciona la opción BODY, dale click a "raw" y configuralo para texto en formato JSON.
       d. Inserta el código en el siguiente formato, llenalo con los datos que te gusten y haz click en SEND:
          {
            "rut_estudiante": "11345678-9",
            "semestre": "2024-2",
            "asignatura": "Gestion de Software",
            "nota": 4.0
          }
       e. Si el codigo se inserto exitosamente deberia entregar el mensaje: "{"mensaje": "Evaluación creada"}".
       f. En el caso de que esta falle debido a que no existe el estudiante asociado al rut, el mensaje "{"mensaje": "No se puede crear evaluación: estudiante no encontrado."}" se presentará.
     2.2.2 Entregar todos los evaluaciones:
       a. Primero acceda a Postman e inserte el siguiente link: "http://localhost:5001/evaluaciones".
       b. Luego coloca el proceso a la izquierda del link, el metodo GET.
       c. Haga click en SEND, como resultado deberia entregar cada evaluación que haya insertado hasta el momento.
     2.2.3 Entregar un evaluación por RUT:
       a. Primero acceda a Postman e inserte el siguiente link: "http://localhost:5001/evaluaciones/<id>". En donde el id es solamente un número.
       b. Luego coloca el proceso a la izquierda del link, el metodo GET.
       c. Haga click en SEND, como resultado deberia entregar la evaluación asociada.
       d. Si no existe el estudiante entregará el mensaje: "{"mensaje": "Evaluación no encontrada"}".
3. Procesos de prueba Postman:
   Para realizar estas pruebas es necesario usar el comando "docker exec -it db psql -U user -d microservicios" en la consola de comandos,
   esto permite revisar la base de datos de manera directa
   3.1. Estudiantes:
     3.1.1 Insertar estudiantes:
       a. Para insertar un nuevo estudiante, utilice el comando de postgress con un formato similar a:
       "INSERT INTO student (rut, nombre_completo, edad, curso) VALUES ('12345678-9', 'Ana Pérez', 21, 'Ingeniería Civil');"
       b. Si esto es exitoso entregara el mensaje "INSERT 0 <numero>" donde el numero cambiará segun cuantos estudiantes sean insertados a la vez.
     3.1.2 Entregar todos los estudiantes:
       a. Para revisar los estudiantes solo inserte "SELECT * FROM student;"
       b. Este entregará una tabla con los estudiantes que esten presentes en el momento.
     3.1.3 Entregar un estudiante por RUT:
       a. Para esto solo inserte como ejemplo: "SELECT * FROM student WHERE rut='12345678-9';"
       b. Si esto es exitoso entregará una tabla con el estudiante que posean el rut, en caso de que no exista no mostrará nada en la tabla.
   3.2. Evaluaciones:
     3.2.1 Insertar evaluaciones:
       a. Para insertar una nueva evaluación, utilice el comando de postgress con un formato similar a:
       "INSERT INTO evaluacion (rut_estudiante, semestre, asignatura, nota) VALUES ('12345678-9', '2024-2', 'Matematica', 5.0);"
       b. Si esto es exitoso entregara el mensaje "INSERT 0 <numero>" donde el numero cambiará segun cuantas evaluaciones sean insertados a la vez.
       c. En el caso de que el rut no este dentro de la tabla de estudiantes, entregará el mensaje:
         "ERROR:  insert or update on table "evaluacion" violates foreign key constraint "evaluacion_rut_estudiante_fkey"
          DETAIL:  Key (rut_estudiante)=(22345678-9) is not present in table "student"."
     3.2.2 Entregar todos las evaluaciones:
       a. Para revisar las evaluaciones solo inserte "SELECT * FROM evaluacion;"
       b. Este entregará una tabla con las evaluaciones que esten presentes en el momento.
     3.2.3 Entregar un evaluación por RUT:
       a. Para esto solo inserte como ejemplo: "SELECT * FROM evaluacion WHERE id=2;"
       b. Si esto es exitoso entregará una tabla con la evaluacion que posea el id correspondiente, en caso de que no exista no mostrará nada en la tabla.

<b>DjangoProject es un programa realizado como práctica inicial con Django, un framework web para Python que permite crear aplicaciones web.</b>

En este caso, se ha creado un pequeño centro de aplicaciones en el que un usuario ha de crear una cuenta y loggearse para poder acceder. 
Una vez dentro, podrá utilizar las diferentes aplicaciones que se encuentran en la web. Dichas aplicaciones consisten en diferentes funcionalidades 
tales cómo agenda de contactos, sistema de alertas y tareas, mensajeria, gestión de archivos e incluso un bot de prueba que simula atención al usuario.

El proyecto sigue una arquitectura MTV (Model - Template - View) para cada aplicación, lo que permite generar cuantas aplicaciones se deseen de forma limpia y ordenada. Además, Django gestiona SQLite
que ya viene incluido en Python usando un ORM que traduce código python a consultas sql automáticamente.

<b>Aplicaciones actuales</b>

- Alertas. Sistema de alertas/tareas en el que el usuario puede crear una alerta con una descripción para que los demás usuarios estén informados y colaboren con la resolución de dichas incidencias.
  Cuando sean solucionadas, los usuarios pueden marcarlas y explicar su resolución. Las alertas se pueden conservar como solucionadas por si fuera útil la misma solución en el futuro. De no
  ser así, se puede eliminar dicha incidencia.

- Chatbot. Asistente robot que reesponde en un chat a las peticiones del usuario, con el fin de resolver pequeñas dudas de los usuarios respecto al programa y, en el futuro, poder automáticamente
  rastrear soluciones de una tabla de incidencias solucionadas y ofrecerlas al usuario. Se trata de un prototipo. Funciona con un diccionario en el que las claves son detectadas en la conversación
  por el bot y sus valores son las respuestas programadas para estas en cuanto las detecte. El sistema de detección por el momento es muy básico y solo reconoce palabras sueltas.

- Contactos. Una agenda que sirve para almacenar contactos usando su nombre, número de teléfono y correo electrónico. Valida dichos datos y los guarda en una lista para poder ser consultados si es necesario. Los usuarios cuentan con un token autogenerado y permanente desde que se crean que, cuando inician sesion desde otra aplicacion, lo reciben y les permite recibir información de otros dispositivos y aplicaciones mediante una API inegrada en la aplicación.

- Mensajes. Funciona como una colección de conversaciones chat entre usuarios dentro de la misma web. Los usuarios pueden iniciar conversaciones con otros usuarios registrados o borrarlas (solo se borra la
  conversación de la bandeja del que la borró).

- Datos. Permite subir archivos csv y excel y almacenarlos como tablas en la web, las cuales se pueden consultar y emplear para hacer estudios y analisis. De momento solo ocnsta con una por defecto para
  analizar el sistema de alertas. Para el manejo de las tablas se emplea la biblioteca de Pandas, la cual permite leer archivos excel o csv, operar con estos y traducirlos a tablas en la web.

- Cuentas. Esta aplicación permite gestionar las cuentas de los usuarios. Puede asignar rol(moderador o usuario) o eliminar a los usuarios. Esta aplicación solo puede ser visualizada y accedida
  por un usuario moderador. Los moderadores son usuarios cuyo rol les permite acceder a los métodos de eliminar o cambiar rol a otros usuarios. Solo pueden ser asignados por otro moderador o superusuario.

<b>Cómo emplear el programa</b>

En la consola del ide se activa el servidor con el comando -python manage.py runserver- lo que carga la web y ofrece el enlace de acceso a esta.

Una vez se entra a la página, lo primero de todo será logearse o registrarse en caso de que no se tenga cuenta. Para el registro, se emplea las funciones ya existentes en Django para formularios y
registro de usuarios.

A partir de aquí ya se pueden emplear las aplicaciones.

<b>Añadidos</b>

- Pandas para tablas
- Matplotlib para gráficas
- Seaborn para gráficas
- lxml para Pandas para tablas
- djangorestframework para APIs

<b>Procedimientos</b>

#Activar el venv si no está activado

- & .venv\Scripts\Activate.ps1

#En lugar de python global usar venv

- python manage.py runserver  ---> .venv\Scripts\python.exe manage.py runserver

#Crear entorno virtual y usar python12

- C:\Users\usuario\AppData\Local\Programs\Python\Python312\python.exe -m venv .venv  (Esto depende de si ya tienes la version de Python pero tu ide no la emplea)

- .\.venv\Scripts\Activate.ps1

#Instala todos los requerimientos

- pip install -r requeriments.txt 

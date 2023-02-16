PASOS INICIAL: CLONAR PROYECTO
1. Copiar el link del Repositorio
2. Crear una carpeta en el escritorio, que es donde clonaremos el Repositorio
3. Dentro de esta carpeta abrir GIT BASH (GIT BASH previamente instalado)
4. Ejecutamos el comando "git clone" + link del repositorio (.git)
SEGUNDO PASO: CREAR ENTORNO VIRTUAL
5. Con el repositorio clonado, y una carpeta creada dentro de la carpeta que se creó inicialmente, ingresamos a la carpeta, y ejecutamos el CMD (Command Prompt) dentro. 
a. AMBIENTE VIRTUAL - instalar el paquete "virtualenv" - pip3 install virtualenv - RESULTADO: da los comandos de "requirements satisfied"
b. CREAR AMBIENTE VIRTUAL - ejecuto el comando en la carpeta del Proyecto / comando "python -m venv env" - RESULTADO: se crea la carpeta "env" en la carpeta del Proyecto 
c. ACTIVAR AMBIENTE VIRTUAL ejecutando el comando "env\Scripts\activate" (CADA VEZ QUE ARRANCAMOS A TRABAJAR)
TERCER PASO: DEPENDENCIAS
Dentro del CMD, mediante el comando "pip install -r requirements.txt" instalamos las dependencias
CUARTO PASO: VSCODE
Dentro de la carpeta de nuestro proyecto, habiendo ya instalado el ambiente virtual y habiendolo activado, desde la carpeta con boton derecho ingresamos el Visual Studio Code
QUINTO PASO: 3 EJECUCIONES DESDE LA TERMINAL
a. Instalar django: pip install django
b. python manage.py migrate
c. python manage.py runserver. Corre el servidor y con el link provisto debajo ingresamos al servidor en el que se desarrolla nuestro programa

SEXTO PASO: DENTRO DEL SITIO WEB
a. Al ingresar al sitio WEB, verificamos que las secciones Estudiantes, Profesores y Cursos tienen sus formularios (1), verificamos que al ingresar los datos se ingresan a la Base de Datos (2). 
b. Luego, para Buscar el nombre de una camada y verificar que existe ingresamos el numero de la camada. Como resultado devolverá la camada si existe y su nombre.

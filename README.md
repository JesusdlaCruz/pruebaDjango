 ### Desarrollo de un microservicio que consulta datos de la API de Marvel
 
 **Instalación**
 
 Después de clonar el proyecto, ejecutar el archivo env_requirements.txt del proyecto principal, 
 para ello debemos tener activo un entorno virtual de python.
 
 Una vez activado el entorno virtual, ingresar a la carpeta del proyecto desde la terminal, 
 que en le caso de Linux o Mac es:
 
 cd pruebaDjango
 
 Y ejecutar el comando:
 pip install env_requirements.txt
 
 Después de ello, damos de alta el servidor local, para ello nos posicionamos a la altura del archivo manage.py e introducimos 
 el comando en la terminal:
 
 python manage.py runserver
 
 Finalmente para consultar la API, en la URL de nuestro navegador introucimos:

 localhost:8000/searchComics
 
 Lo cual hace la petición GET a la API de Marvel para posteriormente mostrar los datos en un template, sin embargo, el template al ser independiente
 de la solicitud, puede ser desarrollado de la manera en que se desee, o bien, únicamente hacer la llamada a la solicitud desde otra aplicación y 
 realizar los filtros correspondientes dependiendo de que información se quiere consutlar.
 

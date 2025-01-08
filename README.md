# Django REST Framework with MongoDB

Este proyecto es una prueba técnica que implementa un backend con **Django REST Framework** y **MongoDB** para realizar un CRUD de libros. A continuación, se detallan las instrucciones para desplegar, utilizar y probar el proyecto.

## Características del Proyecto

- **CRUD de Libros**:
  - Campos: Título, Autor, Género, Fecha de Publicación, Precio.
- **Autenticación JWT**:
  - Login y registro de usuarios.
  - Uso de token para acceder a las APIs.
- **Docker**:
  - Contenedores para el servidor de Django y la base de datos MongoDB.
  - Creación automática de datos iniciales: un usuario de prueba y cinco libros predefinidos.
- **Swagger y Redoc**:
  - Documentación interactiva de las APIs.
- **Postman Collection**:
  - Archivo Postman incluido para pruebas cómodas.
- **Pruebas Unitarias**:
  - Test para las funcionalidades de libros.

---

## Requisitos Previos

- **Docker** y **Docker Compose** instalados en el sistema.
- Conexión a Internet.

---

## Despliegue del Proyecto

1. Clona el repositorio desde el siguiente enlace:
   ```bash
   git clone https://github.com/vhjimenez15/book-seek.git
   cd book-seek
   ```

2. Ejecuta el siguiente comando para construir y levantar los contenedores:
   ```bash
   docker-compose up --build -d
   ```

   Esto creará las imágenes Docker necesarias y levantará:
   - Un contenedor con el servidor de Django.
   - Un contenedor con la base de datos MongoDB.

3. Datos iniciales generados:
   - **Usuario por defecto**:
     - Username: `vjimenez`
     - Contraseña: `123456789`
   - **Libros predefinidos**: 5 libros disponibles para listar y editar.

---

## Uso de las APIs

### Autenticación JWT

1. Para usar las APIs protegidas, primero realiza el login con el usuario por defecto o crea uno nuevo.

   **Endpoint de Login**:
   - URL: `/auth/login/`
   - Credenciales:
     - Username: `vjimenez`
     - Contraseña: `123456789`

2. Obtendrás un token que debes usar en el encabezado `Authorization` con el formato:
   ```
   Bearer <tu_token>
   ```

3. Si deseas registrar un nuevo usuario, usa el siguiente endpoint:
   - **Registro de Usuarios**:
     - URL: `/auth/register/`
     - También documentado en Swagger.

### Documentación de APIs

- **Swagger**: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
- **Redoc**: [http://localhost:8000/redoc/](http://localhost:8000/redoc/)

### Postman Collection

El proyecto incluye una colección de Postman para facilitar el uso de las APIs. Este archivo se encuentra dentro del repositorio o adjunto en el correo enviado.

---

## Pruebas Unitarias

El proyecto incluye pruebas unitarias para validar las funcionalidades del CRUD de libros.

### Ejecución de Pruebas

1. Accede al contenedor de Django:
   ```bash
   docker exec -it django bash
   ```

2. Ejecuta las pruebas:
   ```bash
   python manage.py test book.tests
   ```

---

## Tecnologías Utilizadas

- **Django**: Framework principal del backend.
- **Django REST Framework**: Para la creación de APIs.
- **MongoDB**: Base de datos NoSQL.
- **Docker**: Contenedores para la aplicación y la base de datos.
- **Swagger y Redoc**: Documentación interactiva.

---

## Notas

- Asegúrate de que los contenedores Docker estén corriendo antes de usar las APIs.
- Si no deseas usar el usuario por defecto, puedes registrar uno nuevo con el endpoint `/auth/register/`.
- Revisa el archivo `docker-compose.yml` para personalizar configuraciones si es necesario.

---

¡Gracias por revisar este proyecto! Si tienes alguna pregunta, no dudes en contactarme.


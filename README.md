# Stripe Project

// ...existing code...

## Crear un repositorio local

Para crear un nuevo repositorio local, sigue estos pasos:

1. Abre tu terminal.
2. Navega al directorio donde deseas crear el repositorio.
3. Usa el siguiente comando para inicializar un nuevo repositorio:

   ```sh
   git init
   ```

   Esto creará un nuevo repositorio Git en el directorio actual.

4. Añade los archivos al repositorio:

   ```sh
   git add .
   ```

5. Realiza el primer commit:

   ```sh
   git commit -m "Primer commit"
   ```

## Ver la rama actual en tu terminal

Para ver la rama actual en tu terminal, sigue estos pasos:

1. Abre tu terminal.
2. Navega al directorio de tu repositorio local.
3. Usa el siguiente comando para ver la rama actual:

   ```sh
   git branch
   ```

   El asterisco (\*) indicará la rama actual.

## Instalar `pip` y `python-dotenv`

Para instalar `pip` y el paquete `python-dotenv`, sigue estos pasos:

1. Si no tienes `pip` instalado, puedes instalarlo siguiendo las instrucciones en [este enlace](https://pip.pypa.io/en/stable/installation/).

   ### Instrucciones rápidas para instalar `pip`:

   - **En sistemas Unix/macOS**:

     ```sh
     curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
     python get-pip.py
     ```

   - **En Windows**:

     Descarga `get-pip.py` desde [este enlace](https://bootstrap.pypa.io/get-pip.py) y luego ejecuta:

     ```sh
     python get-pip.py
     ```

2. Una vez que tengas `pip` instalado, ejecuta el siguiente comando para instalar `python-dotenv`:

   ```sh
   pip install python-dotenv
   ```

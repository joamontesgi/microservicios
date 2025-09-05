# 📌 Proyecto de Microservicios

Este proyecto está compuesto por dos microservicios principales:

- 🔐 **Microservicio de Seguridad** → Laravel + Sanctum + MySQL  
- 💱 **Microservicio de Divisas** → Flask + MongoDB  

---

## 🔐 Microservicio de Seguridad

### 🛠️ Tecnologías
- **Framework:** Laravel  
- **Autenticación:** Sanctum  
- **Base de datos:** MySQL  

### 📦 Requisitos
- PHP >= 8.x  
- Composer  
- MySQL  

### ⚙️ Instalación
```bash
# Entrar al directorio del microservicio
cd microservicio_seguridad

# Instalar dependencias
composer install

# Copiar archivo de entorno y configurar la conexión a MySQL
cp .env.example .env

# Generar la key de la aplicación
php artisan key:generate

# Ejecutar migraciones
php artisan migrate
```

### 🚀 Ejecución
```bash
php artisan serve
```

---

## 💱 Microservicio de Divisas

### 🛠️ Tecnologías
- **Framework:** Flask (Python)  
- **Base de datos:** MongoDB  

### 📦 Requisitos
- Python 3.x  
- Flask  
- PyMongo  

### ⚙️ Instalación
```bash
# Entrar al directorio del microservicio
cd microservicio_divisas

# Crear y activar entorno virtual (opcional)
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

# Instalar dependencias necesarias
pip install flask pymongo
```

### 🚀 Ejecución
```bash
python app.py
```

---

## 🗄️ Bases de Datos
- **MySQL** → Usado por el microservicio de seguridad.  
- **MongoDB** → Usado por el microservicio de divisas.  

---

## ▶️ Levantamiento rápido
1. Configurar y levantar **MySQL** y **MongoDB**.  
2. Ejecutar el microservicio de seguridad:  
   ```bash
   cd microservicio_seguridad
   php artisan serve
   ```
3. Ejecutar el microservicio de divisas:  
   ```bash
   cd microservicio_divisas
   python app.py
   ```

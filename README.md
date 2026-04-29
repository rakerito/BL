# LobiFind — Backend

Backend de LobiFind, plataforma de asesorías universitarias en pares de la UTSJR.
Desarrollado con Python y desplegado en Vercel, expone las APIs que alimentan
la plataforma y gestiona la conexión con la base de datos en Supabase.

> 🏫 Proyecto en evaluación para pilotaje e implementación institucional en la UTSJR,
> con visión de expansión a otras universidades.

---

## ✨ Funcionalidades

- API REST para la gestión de asesorías entre estudiantes.
- Conexión y manejo de datos con Supabase.
- Lógica de negocio del sistema LobiFind.
- Desplegado en Vercel para acceso remoto.

---

## 🛠️ Tecnologías utilizadas

- **Lenguaje:** Python
- **Base de datos:** Supabase
- **Despliegue:** Vercel

---

## 📁 Estructura del proyecto

```
├── app/              → Lógica principal y rutas de la API
├── requirements.txt  → Dependencias del proyecto
└── vercel.json       → Configuración de despliegue en Vercel
```

---

## 🚀 Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/rakerito/BL.git
cd BL
```

### 2. Crear y activar un entorno virtual *(recomendado)*

```bash
python -m venv venv

# En Windows:
venv\Scripts\activate

# En macOS/Linux:
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

Crea un archivo `.env` en la raíz del proyecto y agrega tus credenciales de Supabase:

```
SUPABASE_URL=tu-url-de-supabase
SUPABASE_KEY=tu-clave-de-supabase
```

### 5. Ejecutar el servidor

```bash
python app/main.py
```

---

## 🌐 Demo

[bl-gold.vercel.app](https://bl-gold.vercel.app)

---

## 👥 Equipo de desarrollo

| Integrante | Rol |
|---|---|
| Eliel Priske Alanis | Desarrollo backend |
| Yael Meza Polo | Desarrollo backend |
| Raquel Pastor Gaytán | Diseño de interfaz de usuario y documentación técnica |
| Eimi Camila Cervantes Izquierdo | Desarrollo backend |

Materia: Aplicaciones Web Orientadas a Servicios — UTSJR.

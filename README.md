# QA API Framework – Pytest + Requests

## 📌 Descripción
Proyecto de **QA Automation** enfocado en pruebas de **APIs REST** mediante la construcción de un **framework de testing** utilizando **Pytest** y **Requests**.  
Se validan endpoints de una API pública aplicando buenas prácticas como **API Client reutilizable**, **contract testing con Pydantic**, **data-driven testing** y una **estructura escalable**, similar a la utilizada en entornos profesionales.

## ⭐ Características / Features Clave
- **API Client reutilizable** para centralizar llamadas HTTP
- **Separación clara de responsabilidades** (`clients`, `models`, `tests`, `utils`)
- **Contract testing** utilizando **Pydantic**
- **Data-driven testing** con parametrización en **Pytest**
- Tests organizados por **feature** (users / posts)
- Configuración centralizada y **estructura escalable**
- Documentación explícita de **limitaciones reales de la API**

## 🧪 Qué se está probando

### **Users**
- Obtención de usuario por ID (`GET /users/{id}`)
- **Validación de contrato** del usuario (estructura y tipos)
- **Pruebas data-driven** para múltiples usuarios
- Creación de usuario documentada como **no soportada por la API pública** (test marcado como *skipped*)

### **Posts**
- Obtención de listado de posts (`GET /posts`)
- Obtención de post por ID (`GET /posts/{id}`)
- Creación de post (`POST /posts`)
- **Validación de contrato** de posts
- **Pruebas data-driven** para múltiples posts

## 🛠 Stack Tecnológico
- **Python**
- **Pytest**
- **Requests**
- **Pydantic**
- **pytest-html**

## 📂 Estructura del Proyecto
```
qa-api-framework-pytest/
├─ src/
│ ├─ config/
│ │ ├─ settings.py
│ │ └─ env.example
│ ├─ clients/
│ │ ├─ base_client.py
│ │ └─ jsonplaceholder_client.py
│ ├─ models/
│ │ ├─ user.py
│ │ └─ post.py
│ ├─ utils/
│ │ ├─ data_loader.py
│ │ └─ logger.py
│ └─ init.py
├─ tests/
│ ├─ conftest.py
│ ├─ users/
│ │ ├─ test_get_user.py
│ │ └─ test_create_user.py
│ ├─ posts/
│ │ ├─ test_get_posts.py
│ │ └─ test_create_post.py
│ └─ contract/
│ ├─ test_contracts.py
│ └─ test_users_contract_data_driven.py
├─ testdata/
│ ├─ users.json
│ └─ posts.json
├─ pytest.ini
├─ requirements.txt
├─ .gitignore
└─ README.md
```
- `clients/`: clientes de API reutilizables para centralizar llamadas HTTP
- `models/`: modelos de datos para **contract testing** con Pydantic
- `utils/`: utilidades comunes (carga de datos, logging, etc.)
- `tests/`: tests organizados por feature y tipo (users, posts, contracts)
- `testdata/`: datos de prueba utilizados en **data-driven testing**
- `conftest.py`: fixtures globales de **Pytest**
- `pytest.ini`: configuración global del framework

## ▶️ Cómo ejecutar el proyecto
```powershell
# Clonar el repositorio e ingresar al proyecto
git clone <repo-url>
cd qa-api-framework-pytest

# Crear y activar entorno virtual
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar los tests
python -m pytest

# Ejecutar los tests con reporte HTML
python -m pytest --html=report.html --self-contained-html
```
## ✅ Escenarios automatizados
- Obtención de usuarios por ID
- **Validación de contratos** de usuarios
- **Pruebas data-driven** para múltiples usuarios
- Obtención de posts
- Creación de posts
- **Validación de contratos** de posts
- **Pruebas data-driven** para múltiples posts

## 🧠 Decisiones técnicas
- Se utiliza **JSONPlaceholder** como API pública para simular escenarios reales de testing.
- La creación de usuarios (`POST /users`) **no está soportada de forma real** por la API, por lo que el test correspondiente se deja marcado como skipped, documentando explícitamente la limitación.
- Se prioriza **claridad, reutilización de código y mantenibilidad** por sobre complejidad innecesaria.
- El framework está diseñado para ser **fácilmente extensible** a nuevos endpoints y features.

# 📊 Reportes / Evidencia (cuando aplique)
- **Reporte HTML** generado automáticamente mediante **pytest-html** como evidencia de ejecución de la suite de tests.

# 📈 Mejoras futuras
- Incorporar **validaciones negativas** más extensas
- Extender el framework a **nuevas APIs**
- Integrar ejecución automática mediante **CI/CD**
- Incorporar **reportes avanzados (Allure)** en proyectos futuros
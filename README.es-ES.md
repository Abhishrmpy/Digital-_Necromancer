

# 🧙‍♂️ Digital Necromancer

[![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)](https://nodejs.org/)
[![Next.js](https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white)](https://nextjs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)

## 📖 Descripción

Digital Necromancer es una potente aplicación web full-stack que le da nueva vida a bases de código antiguas y heredadas. Al igual que un nigromante que revive a los muertos, esta herramienta utiliza openai/gpt-oss-20b para analizar, explicar y modernizar fragmentos de código obsoletos y proyectos heredados completos.

Ya sea que te enfrentes al infierno de los callbacks de principios de la década de 2010, patrones de jQuery obsoletos o código PHP antiguo que te hace llorar, Digital Necromancer transforma tus pesadillas heredadas en obras maestras modernas y mantenibles.

**Problema que resuelve:**
- Migración y modernización de código heredado
- Comprensión de bases de código complejas y sin documentación
- Aprendizaje de alternativas modernas a patrones obsoletos
- Reducción de la deuda técnica en proyectos existentes

## ✨ Características Principales

- **🔮 Análisis de Código Impulsado por IA:** Aprovecha el modelo GPT OSS 20B de Hugging Face para una comprensión inteligente del código
- **⚡ Generación de Código Moderno:** Convierte patrones heredados en equivalentes modernos (callbacks → async/await, jQuery → JavaScript vanilla, etc.)
- **📚 Explicaciones Inteligentes:** Proporciona explicaciones detalladas y en lenguaje sencillo de las transformaciones del código
- **🔒 Entrada de Código Segura:** Interfaz segura y protegida para enviar código heredado sensible
- **💾 Historial de Transformaciones:** Guarda y administra tus proyectos de modernización de código (perfiles de usuario opcionales)
- **🎨 Interfaz Atractiva:** Interfaz moderna y responsiva construida con Tailwind CSS y Shadcn/UI
- **⚡ Rendimiento Rápido:** Construido sobre Next.js 14 con App Router para un rendimiento óptimo

## 🛠️ Stack Tecnológico

| Categoría | Tecnología |
|----------|------------|
| **Frontend** | Next.js 14 (App Router), React, TypeScript |
| **Estilos** | Tailwind CSS, Shadcn/UI |
| **Backend** | Python FastAPI |
| **IA/ML** | API de Hugging Face (GPT OSS 20B) |
| **Desarrollo** | Vite, ESLint, Prettier |

## 🚀 Inicio Rápido

### Requisitos Previos

- Node.js (v18 o superior)
- Python (v3.8 o superior)
- Administrador de paquetes npm o yarn

### Instalación

1. **Clona el repositorio**
   ```bash
   git clone https://github.com/yourusername/digital-necromancer.git
   cd digital-necromancer
   ```

2. **Instala las dependencias del Frontend**
   ```bash
   # Navega al directorio del frontend
   cd src/gptoss
   npm install
   ```

3. **Instala las dependencias del Backend**
   ```bash
   # Navega al directorio del backend (asumiendo que el backend está en una carpeta separada)
   cd ../backend
   pip install -r requirements.txt
   ```

4. **Configura las Variables de Entorno**
   
   Crea un archivo `.env.local` en la raíz del frontend y `.env` en la raíz del backend:

   **Frontend (.env.local):**
   ```env
   NEXT_PUBLIC_API_URL=http://localhost:8000
   ```

   **Backend (.env):**
   ```env
   HUGGINGFACE_API_KEY=your_huggingface_token_here
   CORS_ORIGINS=http://localhost:3000
   ```

5. **Inicia los Servidores de Desarrollo**

   **Backend (Terminal 1):**
   ```bash
   cd backend
   uvicorn main:app --reload --port 8000
   ```

   **Frontend (Terminal 2):**
   ```bash
   cd src/gptoss
   npm run dev
   ```

6. **Abre tu navegador**
   
   Navega a `http://localhost:3000` para ver la aplicación en ejecución.

## 🎯 Uso

1. **Pega tu Código Heredado:** Usa la interfaz de entrada segura para enviar tu código antiguo
2. **Selecciona el Tipo de Transformación:** Elige el tipo de modernización que necesitas
3. **Análisis con IA:** El sistema analiza tu código utilizando modelos avanzados de IA
4. **Revisa los Resultados:** Obtén código modernizado junto con explicaciones detalladas
5. **Guardar y Exportar:** Guarda tus transformaciones y exporta los resultados

*Espacio para captura de pantalla: Agrega una captura de la interfaz principal que muestre la comparación del código antes/después*

## 🏆 Innovación para Hackathon

**¿Qué hace especial a Digital Necromancer:**

- **🎯 Problema Real, Solución Real:** Aborda un punto de dolor de la industria de $85B
- **🤖 Enfoque Centrado en IA:** Aprovecha modelos de IA de código abierto de vanguardia  
- **⚡ Excelencia Full-Stack:** Stack tecnológico moderno con rendimiento óptimo
- **🎨 Diseño Centrado en el Usuario:** Interfaz intuitiva que cualquiera puede usar
- **🔧 Listo para Producción:** Arquitectura escalable lista para implementación en entornos reales

**Innovación Técnica:**
- Inducción personalizada de IA para análisis y transformación de código
- Procesamiento de código en tiempo real con backend FastAPI
- Componentes modernos de React con seguridad de TypeScript
- Diseño responsivo que funciona en todos los dispositivos

## 🚧 ¿Qué sigue?

**Hoja de Ruta Futura:**
- [ ] Soporte para más lenguajes de programación (Go, Rust, Swift)
- [ ] Integración con GitHub para procesamiento directo de repositorios  
- [ ] Revisión de código y análisis de seguridad impulsados por IA
- [ ] Funciones de colaboración en equipo
- [ ] Opciones de implementación empresarial

## 🏗️ Arquitectura

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │    Backend      │    │  Hugging Face   │
│   (Next.js)     │◄──►│   (FastAPI)     │◄──►│   AI Models     │
│                 │    │                 │    │                 │  
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

| Variable | Descripción | Requerida | Predeterminada |
|----------|-------------|----------|---------|
| `HUGGINGFACE_API_KEY` | Tu token de API de Hugging Face para acceso a modelos de IA | Sí | - |
| `NEXT_PUBLIC_API_URL` | URL de la API del backend para solicitudes del frontend | Sí | `http://localhost:8000` |
| `CORS_ORIGINS` | Orígenes CORS permitidos para el backend | Sí | `http://localhost:3000` |

## 🤝 Contribuciones

¡Bienvenidas las contribuciones de la comunidad! Así es como puedes ayudar:

1. **Haz un fork del repositorio**
2. **Crea una rama de funcionalidad**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Realiza commit de tus cambios**
   ```bash
   git commit -m 'Add some amazing feature'
   ```
4. **Sube (push) a la rama**
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Abre un Pull Request**

### Líneas Guías para Contribuir

- Sigue el estilo de código y convenciones existentes
- Agrega pruebas para las nuevas funcionalidades
- Actualiza la documentación según sea necesario
- Asegúrate de que todas las pruebas pasen antes de enviar

## 📄 Licencia

Este proyecto está licenciado bajo la Licencia Apache 2.0: consulta el archivo [LICENSE](LICENSE) para más detalles.

### Derechos de Uso

Eres libre de usar este proyecto mediante:

1. **Creando tu propio token de Hugging Face** en [Hugging Face](https://huggingface.co/settings/tokens)
2. **Configurando tu entorno** añadiendo tu token al archivo `.env` del backend
3. **Ejecutando la aplicación** siguiendo las instrucciones de instalación anteriores

La licencia Apache 2.0 te permite usar, modificar y distribuir este software libremente para fines tanto personales como comerciales.

## 🙏 Agradecimientos

- A Hugging Face por proporcionar potentes modelos de IA
- A la comunidad de código abierto por las increíbles herramientas y bibliotecas
- A todos los colaboradores que ayudan a mejorar este proyecto

## 📞 Soporte

Si encuentras algún problema o tienes preguntas:

- Abre un issue en GitHub
- Consulta la documentación
- Únete a nuestras discusiones comunitarias

---

**Hecho con ❤️ y un toque de nigromancia digital**

# 🤖 Portero Digital: Azure AI Bot Service

[![Deploy to Azure](https://github.com/antuansabe/portero-bot/actions/workflows/main.yml/badge.svg)](https://github.com/antuansabe/portero-bot/actions)
![Azure](https://img.shields.io/badge/azure-%230072C6.svg?style=for-the-badge&logo=microsoftazure&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## 🎯 Descripción del Proyecto
Este es un **Agente de Bienvenida Inteligente** diseñado para demostrar la integración de infraestructuras críticas en la nube de Microsoft Azure. El proyecto funciona como un "Portero Digital" capaz de gestionar el primer contacto con usuarios, ofreciendo navegación estructurada y respuestas automáticas.

Desarrollado con un enfoque en **escalabilidad y mantenibilidad**, este mini-proyecto sirve como base para implementar arquitecturas más complejas de Inteligencia Artificial Generativa.

---

## 🏗️ Arquitectura del Sistema
El proyecto utiliza una arquitectura desacoplada para optimizar costos y rendimiento:



* **Azure Bot Service:** Interfaz de mensajería y orquestación de canales.
* **Azure App Service (Plan F1):** Hospedaje del "cerebro" lógico desarrollado en Python.
* **GitHub Actions:** Pipeline de **CI/CD** para despliegues automatizados y continuos.
* **Application Insights:** Monitoreo y observabilidad en tiempo real (Logs y métricas).

---

## 🛠️ Stack Tecnológico
* **Lenguaje:** Python 3.12+
* **Framework:** Bot Framework SDK
* **Servidor:** aiohttp / Azure App Service
* **DevOps:** GitHub Actions

---

## 🚀 Funcionalidades
- [x] **Gestión de Estados:** Reconocimiento de nuevos miembros en la conversación.
- [x] **Salidas Estructuradas:** Menús interactivos para el usuario.
- [x] **Infraestructura como Código:** Configuración lista para despliegue en Azure.
- [x] **Monitoreo:** Seguimiento de errores y latencia mediante App Insights.

---

## ⚙️ Instalación Local
1. Clona el repositorio: `git clone https://github.com/TU_USUARIO/portero-bot.git`
2. Crea un entorno virtual: `python3 -m venv venv`
3. Activa el entorno: `source venv/bin/activate`
4. Instala dependencias: `pip install -r requirements.txt`
5. Ejecuta: `python3 app.py`

---

## 👨‍💻 Autor
**Antonio Fernandez** *AI Engineer en formación | Especialista en Microsoft Azure*

---

# 🏨 Sistema de Gestión Hotelera (Hotel Management System)

---


## Descripción
Este es un programa de consola escrito en **Python** diseñado para simular las operaciones básicas de la recepción de un hotel. El sistema permite gestionar reservas, calcular costos dinámicamente, modificar estancias y generar reportes en archivos de texto.

Este proyecto demuestra el uso de estructuras fundamentales de programación como **listas paralelas**, **ciclos**, **condicionales (match-case)** y **manipulación de archivos de texto**.

## 📋 Características Principales

* **Registro de Huéspedes:**
    * **Habitación Sencilla (1-3):** Tarifa fija de $1000.
    * **Habitación Doble (4-6):** Tarifa fija de $1500.
    * **Habitación Grupal (7-9):** Costo por persona ($500 c/u).
* **Facturación Automática:** Cálculo del total a pagar basado en días y tipo de habitación.
* **Reportes:** Generación de archivo `reporte.txt` con tabla de ocupación.
* **Búsqueda:** Localización de huéspedes dentro de los reportes generados.
* **Gestión:** Modificación de días de estancia (con recálculo de costo) y eliminación de reservas.
* **Cierre de Caja:** Muestra los ingresos totales del día al salir.

## 🛠️ Requisitos Tecnológicos

* **Python 3.10+**: Es necesario para soportar la sintaxis `match-case`.

## 🚀 Instrucciones de Uso

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/tu-usuario/tu-repositorio.git](https://github.com/tu-usuario/tu-repositorio.git)
    ```

2.  **Ejecutar el programa:**
    Asegúrate de estar en la carpeta del proyecto y ejecuta:
    ```bash
    python "PROYECTO HOTEL.py"
    ```

3.  **Navegación:**
    Utiliza el teclado numérico para seleccionar las opciones del menú (1-6).

## ⚠️ Notas
* El sistema utiliza almacenamiento en memoria (RAM) mediante listas. Los datos se reinician al cerrar el programa a menos que generes el reporte.
* Para usar la función de **Búsqueda (Opción 2)**, primero debes generar el archivo de reporte en la **Opción 3**.

### 👤 Author
**Jose Angel Márquez Ramírez**
* Estudiante en UPAEP 🦅
* GitHub: [@Jangelmqza](https://github.com/Jangelmqza)

---

## Description
This is a console-based **Python** application designed to simulate front-desk hotel operations. The system handles bookings, dynamic cost calculations, stay modifications, and text-file report generation.

This project showcases fundamental programming concepts such as **parallel lists**, **loops**, **conditionals (match-case)**, and **file handling**.

## 📋 Key Features

* **Guest Registration:**
    * **Single Room (1-3):** Flat rate of $1000.
    * **Double Room (4-6):** Flat rate of $1500.
    * **Group Room (7-9):** Per-person rate ($500 each).
* **Automatic Billing:** Calculates total cost based on stay duration and room type.
* **Reports:** Exports occupancy data to `reporte.txt`.
* **Search:** Finds guests within the generated report files.
* **Management:** Modify stay duration (auto-recalculates cost) and delete bookings.
* **Daily Close:** Displays total daily revenue upon exit.

## 🛠️ Tech Requirements

* **Python 3.10+**: Required to support the `match-case` syntax.

## 🚀 Usage

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repo.git](https://github.com/your-username/your-repo.git)
    ```

2.  **Run the program:**
    Navigate to the project folder and run:
    ```bash
    python "PROYECTO HOTEL.py"
    ```
### 👤 Author
**Jose Angel Márquez Ramírez**
* Student at UPAEP 🦅
* GitHub: [@Jangelmqza](https://github.com/Jangelmqza)

3.  **Navigation:**
    Use the number keys to select menu options (1-6).

## ⚠️ Notes
* The system uses in-memory storage (lists). Data is reset when the program closes unless you generate a report.
* To use the **Search (Option 2)** feature, you must first generate the report file via **Option 3**.

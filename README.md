# Invoice Generator

A simple desktop Invoice Generator built using Python and Tkinter.

## Features

* Interactive graphical user interface
* Customer information management
* Product and quantity management
* Unit price calculation
* Automatic subtotal calculation
* 10% sales tax calculation
* Automatic total calculation
* Input validation
* Multiple products in a single invoice
* DOCX invoice generation
* New Invoice / Reset functionality
* Interactive button hover effects
* Windows executable support using PyInstaller

## Technologies Used

* Python
* Tkinter
* ttk
* docxtpl
* python-docx template
* PyInstaller

## How to Run

Install the required package:

```bash
pip install docxtpl
```

Run the application:

```bash
python main.py
```

Make sure `invoice_template.docx` is available with the application.

## Create Windows EXE

Install PyInstaller:

```bash
pip install pyinstaller
```

Build the executable:

```bash
pyinstaller --onefile --windowed --add-data "invoice_template.docx;." main.py
```

The executable will be created inside the `dist` folder.

## Project Structure

```text
Invoice-Generator/
│
├── main.py
├── invoice_template.docx
├── requirements.txt
└── README.md
```

## Author

Kalaiyarasu S

B.Tech Artificial Intelligence and Data Science

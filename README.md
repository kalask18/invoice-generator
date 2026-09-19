# Invoice Generator

This project generates invoice output from Python.

## Run

```bash
python invoice_generator.py
```

## Build

To create a Windows executable with PyInstaller:

```bash
pyinstaller --onefile invoice_generator.py
```

## Notes

- The generated executable may appear in the `dist` folder.
- The project excludes build artifacts and Python cache files via `.gitignore`.

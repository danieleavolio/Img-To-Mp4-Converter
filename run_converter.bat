@echo off
:: Get the directory of the batch script
set DIR=%~dp0
:: Run the Python script
python "%DIR%converter_gui.py"
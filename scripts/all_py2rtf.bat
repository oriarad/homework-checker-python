@echo off
pip install virtualenv > nul
virtualenv .\virenv > nul
call virenv\scripts\activate > nul
pip install Pygments > nul
SET CURRENT_DIR=%CD%
cd %1
FOR /r %%i IN (*.py) DO (
  IF NOT EXIST %%~dpni.rtf (
    echo --- Now pygmentize %%i
    pygmentize -f rtf -l python -o "%%~dpni.rtf" "%%i"
  )
)
cd %CURRENT_DIR%
call deactivate
@echo off
REM ###########################################################################
REM # Format the pinaxai library
REM # Usage: scripts\format.bat
REM ###########################################################################

SETLOCAL ENABLEDELAYEDEXPANSION

REM Get current directory
SET "CURR_DIR=%~dp0"
SET "PINAXAI_DIR=%CURR_DIR%\.."

ECHO [INFO] Formatting Python code in %PINAXAI_DIR%

REM Check if black and isort are installed
python -c "import black" 2>nul
IF %ERRORLEVEL% NEQ 0 (
    ECHO [ERROR] black is not installed. Please install it with: pip install black
    EXIT /B 1
)

python -c "import isort" 2>nul
IF %ERRORLEVEL% NEQ 0 (
    ECHO [ERROR] isort is not installed. Please install it with: pip install isort
    EXIT /B 1
)

REM Format Python code with black and isort
ECHO [INFO] Running black...
python -m black "%PINAXAI_DIR%"

ECHO [INFO] Running isort...
python -m isort "%PINAXAI_DIR%"

ECHO [INFO] Pinaxai code formatting complete.
EXIT /B 
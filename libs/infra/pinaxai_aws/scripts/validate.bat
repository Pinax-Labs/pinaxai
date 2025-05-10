@echo off
REM ###########################################################################
REM # Validate the pinaxai_aws library using ruff and mypy
REM # Usage: libs\infra\pinaxai_aws\scripts\validate.bat
REM ###########################################################################

SETLOCAL ENABLEDELAYEDEXPANSION

REM Get current directory
SET "CURR_DIR=%~dp0"
SET "PINAXAI_AWS_DIR=%CURR_DIR%\.."

ECHO.
ECHO ##################################################
ECHO # Validating pinaxai_aws
ECHO ##################################################
ECHO.

REM Check if ruff and mypy are installed
python -c "import ruff" 2>nul
IF %ERRORLEVEL% NEQ 0 (
    ECHO [ERROR] ruff is not installed. Please install it with: pip install ruff
    EXIT /B 1
)

python -c "import mypy" 2>nul
IF %ERRORLEVEL% NEQ 0 (
    ECHO [ERROR] mypy is not installed. Please install it with: pip install mypy
    EXIT /B 1
)

ECHO.
ECHO ##################################################
ECHO # Running: ruff check %PINAXAI_AWS_DIR%
ECHO ##################################################
ECHO.

python -m ruff check "%PINAXAI_AWS_DIR%"
IF %ERRORLEVEL% NEQ 0 (
    ECHO [ERROR] ruff check failed with exit code %ERRORLEVEL%
    EXIT /B %ERRORLEVEL%
)

ECHO.
ECHO ##################################################
ECHO # Running: mypy %PINAXAI_AWS_DIR% --config-file %PINAXAI_AWS_DIR%\pyproject.toml
ECHO ##################################################
ECHO.

python -m mypy "%PINAXAI_AWS_DIR%" --config-file "%PINAXAI_AWS_DIR%\pyproject.toml"
IF %ERRORLEVEL% NEQ 0 (
    ECHO [ERROR] mypy validation failed with exit code %ERRORLEVEL%
    EXIT /B %ERRORLEVEL%
)

ECHO [INFO] pinaxai_aws validation complete.
EXIT /B 0 
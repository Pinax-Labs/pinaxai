@echo off
REM ###########################################################################
REM # Validate all libraries
REM # Usage: scripts\validate.bat
REM ###########################################################################

SETLOCAL ENABLEDELAYEDEXPANSION

REM Get current directory
SET "CURR_DIR=%~dp0"
SET "REPO_ROOT=%CURR_DIR%\.."
SET "PINAXAI_DIR=%REPO_ROOT%\libs\pinaxai"
SET "PINAXAI_DOCKER_DIR=%REPO_ROOT%\libs\infra\pinaxai_docker"
SET "PINAXAI_AWS_DIR=%REPO_ROOT%\libs\infra\pinaxai_aws"

REM Function to print headings
CALL :print_heading "Validating all libraries"

REM Check if directories exist
IF NOT EXIST "%PINAXAI_DIR%" (
    ECHO [ERROR] PINAXAI_DIR: %PINAXAI_DIR% does not exist
    EXIT /B 1
)

IF NOT EXIST "%PINAXAI_DOCKER_DIR%" (
    ECHO [ERROR] PINAXAI_DOCKER_DIR: %PINAXAI_DOCKER_DIR% does not exist
    EXIT /B 1
)

IF NOT EXIST "%PINAXAI_AWS_DIR%" (
    ECHO [ERROR] PINAXAI_AWS_DIR: %PINAXAI_AWS_DIR% does not exist
    EXIT /B 1
)

REM Validate all libraries
SET PINAXAI_VALIDATE="%PINAXAI_DIR%\scripts\validate.bat"
IF EXIST %PINAXAI_VALIDATE% (
    ECHO [INFO] Running %PINAXAI_VALIDATE%
    CALL %PINAXAI_VALIDATE%
    IF %ERRORLEVEL% NEQ 0 (
        ECHO [ERROR] %PINAXAI_VALIDATE% failed with exit code %ERRORLEVEL%
        EXIT /B %ERRORLEVEL%
    )
) ELSE (
    ECHO [WARNING] %PINAXAI_VALIDATE% does not exist, skipping
)

SET PINAXAI_DOCKER_VALIDATE="%PINAXAI_DOCKER_DIR%\scripts\validate.bat"
IF EXIST %PINAXAI_DOCKER_VALIDATE% (
    ECHO [INFO] Running %PINAXAI_DOCKER_VALIDATE%
    CALL %PINAXAI_DOCKER_VALIDATE%
    IF %ERRORLEVEL% NEQ 0 (
        ECHO [ERROR] %PINAXAI_DOCKER_VALIDATE% failed with exit code %ERRORLEVEL%
        EXIT /B %ERRORLEVEL%
    )
) ELSE (
    ECHO [WARNING] %PINAXAI_DOCKER_VALIDATE% does not exist, skipping
)

SET PINAXAI_AWS_VALIDATE="%PINAXAI_AWS_DIR%\scripts\validate.bat"
IF EXIST %PINAXAI_AWS_VALIDATE% (
    ECHO [INFO] Running %PINAXAI_AWS_VALIDATE%
    CALL %PINAXAI_AWS_VALIDATE%
    IF %ERRORLEVEL% NEQ 0 (
        ECHO [ERROR] %PINAXAI_AWS_VALIDATE% failed with exit code %ERRORLEVEL%
        EXIT /B %ERRORLEVEL%
    )
) ELSE (
    ECHO [WARNING] %PINAXAI_AWS_VALIDATE% does not exist, skipping
)

ECHO [INFO] All validations complete.
EXIT /B 0

REM Function to print headings
:print_heading
ECHO.
ECHO ##################################################
ECHO # %1
ECHO ##################################################
ECHO.
EXIT /B 
@echo off
REM ###########################################################################
REM # Format all libraries
REM # Usage: scripts\format.bat
REM ###########################################################################

SETLOCAL ENABLEDELAYEDEXPANSION

REM Get current directory
SET "CURR_DIR=%~dp0"
SET "REPO_ROOT=%CURR_DIR%\.."
SET "PINAXAI_DIR=%REPO_ROOT%\libs\pinaxai"
SET "PINAXAI_DOCKER_DIR=%REPO_ROOT%\libs\infra\pinaxai_docker"
SET "PINAXAI_AWS_DIR=%REPO_ROOT%\libs\infra\pinaxai_aws"
SET "COOKBOOK_DIR=%REPO_ROOT%\cookbook"

REM Function to print headings
CALL :print_heading "Formatting all libraries"

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

IF NOT EXIST "%COOKBOOK_DIR%" (
    ECHO [ERROR] COOKBOOK_DIR: %COOKBOOK_DIR% does not exist
    EXIT /B 1
)

REM Format all libraries
SET PINAXAI_FORMAT="%PINAXAI_DIR%\scripts\format.bat"
IF EXIST %PINAXAI_FORMAT% (
    ECHO [INFO] Running %PINAXAI_FORMAT%
    CALL %PINAXAI_FORMAT%
) ELSE (
    ECHO [WARNING] %PINAXAI_FORMAT% does not exist, skipping
)

SET PINAXAI_DOCKER_FORMAT="%PINAXAI_DOCKER_DIR%\scripts\format.bat"
IF EXIST %PINAXAI_DOCKER_FORMAT% (
    ECHO [INFO] Running %PINAXAI_DOCKER_FORMAT%
    CALL %PINAXAI_DOCKER_FORMAT%
) ELSE (
    ECHO [WARNING] %PINAXAI_DOCKER_FORMAT% does not exist, skipping
)

SET PINAXAI_AWS_FORMAT="%PINAXAI_AWS_DIR%\scripts\format.bat"
IF EXIST %PINAXAI_AWS_FORMAT% (
    ECHO [INFO] Running %PINAXAI_AWS_FORMAT%
    CALL %PINAXAI_AWS_FORMAT%
) ELSE (
    ECHO [WARNING] %PINAXAI_AWS_FORMAT% does not exist, skipping
)

REM Format all cookbook examples
SET COOKBOOK_FORMAT="%COOKBOOK_DIR%\scripts\format.bat"
IF EXIST %COOKBOOK_FORMAT% (
    ECHO [INFO] Running %COOKBOOK_FORMAT%
    CALL %COOKBOOK_FORMAT%
) ELSE (
    ECHO [WARNING] %COOKBOOK_FORMAT% does not exist, skipping
)

ECHO [INFO] All formatting complete.
EXIT /B

REM Function to print headings
:print_heading
ECHO.
ECHO ##################################################
ECHO # %1
ECHO ##################################################
ECHO.
EXIT /B 
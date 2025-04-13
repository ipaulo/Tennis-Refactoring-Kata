@echo off

coverage run -m pytest

IF %ERRORLEVEL% EQU 0 (
    echo. 
    coverage report -m
    ruff check --select I --fix
    ruff format

    echo.
    echo Don't forget to commit

)
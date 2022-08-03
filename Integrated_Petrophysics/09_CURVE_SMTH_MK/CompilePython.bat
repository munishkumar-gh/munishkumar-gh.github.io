cls
@echo off
echo.
echo Compilation in progress...
echo.

:: first argument gives the output dll name
:: remaining arguments give the quoted paths of assemblies to be linked to
SET OUTPUT_NAME=%1%
:: remove the file extension
set OUTPUT_NAME=%OUTPUT_NAME:~0,-4%
SHIFT

:Architecture
IF %PROCESSOR_ARCHITECTURE% EQU AMD64 (
GOTO X64
) ELSE (
GOTO X86
)

:X64
SET COMPILER=ipy64
GOTO DoCompile

:X86
SET COMPILER=ipy

:DoCompile
%COMPILER% pyc.py /out:"%OUTPUT_NAME%" /main:UserProgram.py /target:library
goto End

:End
if errorlevel == 9009 exit errorlevel else goto PauseWindow

:PauseWindow
echo.
echo To close this window,
pause 
exit errorlevel

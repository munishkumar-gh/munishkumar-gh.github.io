@echo off
python /? 1>nul
if errorlevel 9009 echo Python compiler not found. Make sure Python is installed and available at a command prompt.&pause&exit /b 1
echo Creating supporting python files...
if exist UserProgram.dll del UserProgram.dll
:Compile
python -m py_compile UsersPythonCode.py
if errorlevel 1 pause&exit /b 1
:: Create a fake dll so IP thinks the user app is valid etc...
echo dummy dll>UserProgram.dll
echo Python Files Created
pause
exit /b 0
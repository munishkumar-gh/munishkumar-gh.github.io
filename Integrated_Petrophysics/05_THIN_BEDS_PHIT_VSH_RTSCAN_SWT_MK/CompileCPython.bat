@echo off
python /? 1>nul
if errorlevel 9009 echo Python compiler not found. Make sure Python is installed and available at a command prompt.&pause&exit /b 1
echo Creating supporting python files...
if exist UserProgram.dll del UserProgram.dll
if exist Python.Runtime.dll goto Compile
:: Update the python runtime assembly 
:: These batch commands will test python is installed by trying to run some python code and also
:: report back the version of python installed. Then using this info the correct runtime assembly will be copied
%WINDIR%\system32\more /E +34 "%~0" | python -
if errorlevel 3333 set pyRuntime=PythonV3.Runtime.dll&goto Done
if errorlevel 2222 set pyRuntime=PythonV2.Runtime.dll&goto Done
if errorlevel 1 pause&exit /b 1
:Done
@setlocal enableDelayedExpansion
if not defined IntPetroPath (
  :: get the IP install location from the registry if not already defined
  FOR /F "usebackq skip=2 tokens=1-2*" %%A IN (`REG QUERY HKEY_CURRENT_USER\Software\Classes\CLSID\{033AECD9-0361-443A-8D90-F78350E2F0E2}\LocalServer32 /ve 2^>nul`) DO set IntPetroPath=%%C
  set IntPetroPath=!IntPetroPath:"=!
  set IntPetroPath=!IntPetroPath:IntPetro.exe=!
  set IntPetroPath=!IntPetroPath:IntPetro32.exe=!
)
echo Copying "%IntPetroPath%%pyRuntime%" to .\Python.Runtime.dll
copy /Y "%IntPetroPath%%pyRuntime%" .\Python.Runtime.dll
if errorlevel 1 pause&exit /b 1
:Compile
python -m py_compile UsersPythonCode.py
if errorlevel 1 pause&exit /b 1
:: Create a fake dll so IP thinks the user app is valid etc...
echo dummy dll>UserProgram.dll
echo Python Files Created
pause
exit /b 0
:: Enter this line number in the more command above
import sys
if (sys.version_info[0] < 2) or \
		(sys.version_info[0] > 3) or \
		(sys.version_info[0] == 2 and sys.version_info[1] < 7) or \
		(sys.version_info[0] == 3 and sys.version_info[1] >= 7):
	print('Supported python versions are 2.7 to 3.6')
	sys.exit(1)
if sys.version_info[0] >= 3:
	sys.exit(3333)
sys.exit(2222)

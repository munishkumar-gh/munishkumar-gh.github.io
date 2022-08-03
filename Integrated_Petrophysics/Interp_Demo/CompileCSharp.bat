cls
@echo off
echo.
echo Compilation in progress...
echo.

if [%DebugBuild%] == [TRUE] set DebugBuild=/debug

:: first argument gives the output dll name
:: remaining arguments give the quoted paths of assemblies to be linked to
SET OUTPUT_NAME=%1%
SHIFT

SET LIB_OPTS=

:ParamLoop
IF [%1]==[] GOTO DotNetVersion
SET LIB_OPTS=%LIB_OPTS% /r:%1%
SHIFT
GOTO ParamLoop

:DotNetVersion
if exist %windir%\Microsoft.NET\Framework\v4.5* ( 
	for /d %%d in (%windir%\Microsoft.NET\Framework\v4.5*) do (
			set frameworkDir=%%d
		)
) else (
	if exist %windir%\Microsoft.NET\Framework\v4.0* (
		for /d %%d in (%windir%\Microsoft.NET\Framework\v4.0*) do (
			set frameworkDir=%%d
		)
	) else (
		rem We cannot have IP without at least .NET 3.5
		for /d %%d in (%windir%\Microsoft.NET\Framework\v3.5*) do (
			set frameworkDir=%%d
		)
	)
)

%frameworkDir%\csc %DebugBuild% /t:library /out:"%OUTPUT_NAME%" /r:PGL.IP.UserProgDotNetInterface.dll /r:PGL.IP.API.dll  %LIB_OPTS%  *.cs 
goto End

:End
if errorlevel == 9009 exit errorlevel else goto PauseWindow

:PauseWindow
echo.
echo To close this window,
pause 
exit errorlevel

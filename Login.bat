@echo off
Title BloodyAra Started at %time%
color 0A
cls
echo Preventing Crashes.

:bot
cls
echo (%time%) BloodyAra  started.
start /wait %SystemDrive%\python34\python "%~dp0\ara.py"
echo (%time%) WARNING: BloodyAra closed or crashed, restarting.
goto bot
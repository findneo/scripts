@echo off
for /R f\ %%i in (*) do (
    @echo %%i
    sigcheck.exe -h %%i|findstr MD5
    rem @echo paste true sig:
    )
pause
@echo off
set name= �������
set phone= �˻�
set pass= ����
rasdial | findstr ������ > nul
if errorlevel 1 goto notfound

rem string was found
rasdial %name% /disconnect 

goto endfind

:notfound
rem string was not found
rasdial %name% %phone% %pass%

:endfind
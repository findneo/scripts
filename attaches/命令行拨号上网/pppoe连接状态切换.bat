@echo off
set name= 宽带名字
set phone= 账户
set pass= 密码
rasdial | findstr 已连接 > nul
if errorlevel 1 goto notfound

rem string was found
rasdial %name% /disconnect 

goto endfind

:notfound
rem string was not found
rasdial %name% %phone% %pass%

:endfind
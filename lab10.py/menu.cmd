@echo off
:menu
cls
echo =================================
echo          Menu-Driven Script
echo =================================
echo 1. Print IPv4 and IPv6 addresses
echo 2. Trace network path to hostname
echo 3. Get IP address of a hostname
echo 4. Encrypt file (Base64)
echo 5. Decrypt file (Base64)
echo 6. Compress file (ZIP)
echo 7. Restore file from ZIP
echo 8. Calculate MD5 hash of a file
echo 9. Exit
echo =================================
set /p choice=Choose an option: 

if "%choice%"=="1" goto ipv
if "%choice%"=="2" goto traceroute
if "%choice%"=="3" goto getip
if "%choice%"=="4" goto encrypt
if "%choice%"=="5" goto decrypt
if "%choice%"=="6" goto compress
if "%choice%"=="7" goto restore
if "%choice%"=="8" goto calcval
if "%choice%"=="9" exit
goto menu

:ipv
cls
echo IPv4 and IPv6 addresses:
ipconfig | findstr /i "IPv4 IPv6"
pause
goto menu

:traceroute
cls
set /p hostname=Enter hostname or URL: 
tracert %hostname%
pause
goto menu

:getip
cls
set /p hostname=Enter hostname or URL: 
for /f "tokens=2 delims=[]" %%a in ('ping -n 1 %hostname% ^| find "Pinging"') do echo IP Address: %%a
pause
goto menu

:encrypt
cls
set /p input=Enter file to encrypt: 
certutil -encode %input% %input%.enc
echo File encrypted as %input%.enc
pause
goto menu

:decrypt
cls
set /p input=Enter encrypted file to decrypt: 
certutil -decode %input% %input%.dec
echo File decrypted as %input%.dec
pause
goto menu

:compress
cls
set /p input=Enter file to compress: 
set zipfile=%input%.zip
echo Creating %zipfile%...
powershell -Command "Compress-Archive -Path '%input%' -DestinationPath '%zipfile%'"
echo File compressed as %zipfile%.
pause
goto menu

:restore
cls
set /p input=Enter ZIP file to restore: 
set restored_folder=%input%_restored
echo Restoring to folder %restored_folder%...
powershell -Command "Expand-Archive -Path '%input%' -DestinationPath '%restored_folder%'"
echo File restored to folder %restored_folder%.
pause
goto menu

:calcval
cls
set /p input=Enter file to calculate hash: 
certutil -hashfile %input% MD5
pause
goto menu

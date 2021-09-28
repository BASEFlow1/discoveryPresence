@echo off
:START
tasklist /fi "ImageName eq Discord.exe" /fo csv 2>NUL | find /I "discord.exe">NUL
if "%ERRORLEVEL%"=="0" python discoveryPresence.py "A:\Spiele\Freelancer\Discovery Freelancer 4.91.0"
timeout /T 5 /NOBREAK >NUL
goto START
pause >nul

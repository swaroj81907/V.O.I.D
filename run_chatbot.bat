@echo off
cd /d C:\Users\rswar\OneDrive\Desktop\chatbot_project

:: Check for admin privileges
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Please run this file as administrator!
    pause
    exit
)

:: Add voidchat.local to hosts file if not present
findstr /C:"voidchat.local" %SystemRoot%\System32\drivers\etc\hosts >nul
if %errorlevel% neq 0 (
    echo 127.0.0.1 voidchat.local >> %SystemRoot%\System32\drivers\etc\hosts
)

:: Run terminal animation
python animation.py

:: Open browser
start http:127.0.0.1:8080

:: Start Flask server silently (no banner needed anymore)
python app.py

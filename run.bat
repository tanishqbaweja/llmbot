@echo off
cd /d "H:\Github Repositories\llmbot"

git push -u origin main

:: Run the bot
python llmbot.py

pause

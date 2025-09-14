@echo off
cd /d "H:\Github Repositories\llmbot"

git add .
git commit -m "new commit"
git push -u origin main

:: Run the bot
python llmbot.py

pause

@echo off
cd /d "%~dp0"
python -m http.server 8000
echo Server running at http://localhost:8000
pause
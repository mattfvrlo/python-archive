@ECHO OFF
:start
cls
SET /P url= "Paste the youtube URL you want to download: "
youtube-dl -f bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio --embed-thumbnail --add-metadata -o "%%(title)s." --merge-output-format mp4 %url%
pause
goto start
PAUSE
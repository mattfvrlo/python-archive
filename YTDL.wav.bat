@ECHO OFF

cls

SET /P url= "Paste the youtube URL you want to download: "

youtube-dl -x --audio-format wav %url%

PAUSE
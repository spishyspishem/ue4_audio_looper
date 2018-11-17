# ue4_audio_looper

Put libav in the same directory referred to in the powershell script.  You can get it here if you don't have it:
http://builds.libav.org/windows/

Install Python 3 64 bit from here:
https://www.python.org/ftp/python/3.7.0/python-3.7.0-amd64.exe

More info about that is here:
https://www.python.org/downloads/release/python-370/

Open file explorer.
Press Alt + F + S + A in that order, not all at once.
Select yes to the UAC prompt
You should get a PowerShell Window.  Type exactly:

pip install pydub

and press enter.

Then double click the .reg file to change your powershell execution policy so you can run the powershell script.

Then right click on "AddLibavToEnvVars.ps1" and choose "Run with PowerShell."  Don't worry about the windows that popup.  This adds libav to your system environment variables.

Then you're good to go.  UE4 Audio Looper.py should always work now.

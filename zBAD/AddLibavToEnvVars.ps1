# Author: PK2
# Reference: https://blogs.technet.microsoft.com/heyscriptingguy/2011/07/23/use-powershell-to-modify-your-environmental-path/
# Incompatibility: None

$principal = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
if($principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator))
{
  Set-Location -Path $PSScriptRoot
  # code starts here...
  $libav_path = ";" + $PSScriptRoot + "\win64\usr\bin"
  [Environment]::SetEnvironmentVariable("Path", $Env:Path + $libav_path, "Machine")

}
else
{
  Start-Process -FilePath "powershell" -ArgumentList "-NoLogo $('-File ""')$(Get-Location)$('\')$($MyInvocation.MyCommand.Name)$('""')" -Verb runAs
}
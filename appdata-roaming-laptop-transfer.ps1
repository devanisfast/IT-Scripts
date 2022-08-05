#Appdata Roaming Transfers

$PCnum = Read-Host -Prompt 'Enter the old PC number'
$userName = Read-Host -Prompt 'Enter username'
$PCdest = Read-Host -Prompt 'Enter the new PC number'

$exclude = @("*.crl","*.log","*.bin","*.jfm","*.vol","*.edb","*.jcp","*.jtx","*.jrs","*.ost","*.nst","*.pst","*.exe")
$sourceFolder = '\\'+$PCnum+'\c$\Users\'+$userName+'\appdata\Roaming\'
$destination  = '\\'+$PCdest+'\c$\Users\'+$userName+'\appdata\Roaming\'

New-Item -ItemType Directory -Force -Path $destination
Get-ChildItem $sourceFolder -Exclude $exclude | Copy-Item -Destination $destination -Exclude $exclude -Recurse -Container -Force -ErrorAction SilentlyContinue
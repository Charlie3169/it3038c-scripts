function getIP {
    (Get-NetIPAddress).IPv4Address | Select-String "192*"
}

$IP = getIP
$USER = whoami
$DATE = Get-Date

$BODY = ("This machine's IP is {0}. User is {1}. Hostname is {2}. PowerShell Version {3}. Today's Date is {4}" -f $IP, $USER, $HOST.Name, $HOST.Version, $DATE)
$BODY |  Out-File C:\it3038c-scripts\powershell\systemInfo.txt

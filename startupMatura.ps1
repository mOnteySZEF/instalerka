$username = "matura"
$userExists = Get-LocalUser -Name $username -ErrorAction SilentlyContinue

if ($userExists) {
Write-Host "Użytkownik $username istnieje. Log na uzytkownika..."
} else {
Write-Host "Uzytkownik $username nie istnieje. Tworzenie użytkownika..."
New-LocalUser -Name $username -FullName "Matura" -Password (ConvertTo-SecureString "" -AsPlainText -Force) -UserMayChangePassword $false -PasswordNeverExpires $true -AccountNeverExpires $true
Write-Host "uzytkownik $username został utworzony!"
}

Start-Process "C:\Windows\System32\Logoff.exe"

© FazeRP.eu - Skopiowano z notatek, pozdrawiam mOntey
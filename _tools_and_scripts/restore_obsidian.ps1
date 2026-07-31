$appDataDir = Join-Path $env:APPDATA "obsidian"
if (-not (Test-Path $appDataDir)) {
    New-Item -ItemType Directory -Path $appDataDir -Force | Out-Null
}

$jsonPath = Join-Path $appDataDir "obsidian.json"

# Restore both echo and abdominal ultrasound vaults
$echoPath = "C:/Antigravity/超音波検査/心エコー"
$abdomPath = "C:/Antigravity/超音波検査/腹部超音波検査_教科書"

$md5 = [System.Security.Cryptography.MD5]::Create()

# Hash 1: Echo
$hashEcho = ([System.BitConverter]::ToString($md5.ComputeHash([System.Text.Encoding]::UTF8.GetBytes($echoPath)))).Replace("-", "").ToLower().Substring(0, 16)

# Hash 2: Abdomen
$hashAbdom = ([System.BitConverter]::ToString($md5.ComputeHash([System.Text.Encoding]::UTF8.GetBytes($abdomPath)))).Replace("-", "").ToLower().Substring(0, 16)

$vaultsObj = [ordered]@{}

if (Test-Path $echoPath) {
    $vaultsObj[$hashEcho] = [ordered]@{
        path = $echoPath
        open = $false
    }
}

if (Test-Path $abdomPath) {
    $vaultsObj[$hashAbdom] = [ordered]@{
        path = $abdomPath
        open = $true
    }
}

$jsonObj = [ordered]@{
    vaults = $vaultsObj
}

$jsonString = $jsonObj | ConvertTo-Json -Depth 5
[System.IO.File]::WriteAllText($jsonPath, $jsonString, [System.Text.Encoding]::UTF8)
Write-Output "Restored both Echo and Abdomen vaults in Obsidian!"

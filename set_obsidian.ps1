$appDataDir = Join-Path $env:APPDATA "obsidian"
if (-not (Test-Path $appDataDir)) {
    New-Item -ItemType Directory -Path $appDataDir -Force | Out-Null
}

$jsonPath = Join-Path $appDataDir "obsidian.json"
$targetPath = "C:/Antigravity/超音波検査/腹部超音波検査_教科書"

# Generate a 16-char hex ID for vault
$md5 = [System.Security.Cryptography.MD5]::Create()
$hashBytes = $md5.ComputeHash([System.Text.Encoding]::UTF8.GetBytes($targetPath))
$vaultId = ([System.BitConverter]::ToString($hashBytes)).Replace("-", "").ToLower().Substring(0, 16)

$vaultsObj = [ordered]@{}
$vaultsObj[$vaultId] = [ordered]@{
    path = $targetPath
    open = $true
}

$jsonObj = [ordered]@{
    vaults = $vaultsObj
}

$jsonString = $jsonObj | ConvertTo-Json -Depth 5
[System.IO.File]::WriteAllText($jsonPath, $jsonString, [System.Text.Encoding]::UTF8)
Write-Output "Successfully updated Obsidian config at $jsonPath"

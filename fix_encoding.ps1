$targetDir = "C:\Antigravity\超音波検査\腹部超音波検査_教科書"

# Fix encoding to pure UTF-8 for all md files recursively
$files = Get-ChildItem -Path $targetDir -Filter "*.md" -Recurse

foreach ($file in $files) {
    try {
        $content = [System.IO.File]::ReadAllText($file.FullName, [System.Text.Encoding]::UTF8)
        # Re-save with UTF8 Encoding (BOM enabled to guarantee Windows/Obsidian compatibility)
        $utf8WithBom = New-Object System.Text.UTF8Encoding($true)
        [System.IO.File]::WriteAllText($file.FullName, $content, $utf8WithBom)
        Write-Output "Fixed encoding for: $($file.Name)"
    } catch {
        Write-Output "Error processing $($file.Name): $_"
    }
}

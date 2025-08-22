param(
    [string[]]$Files = @(),
    [string]$OutFile = "anki_cards.tsv",
    [string]$DeckRoot = "计算机组成原理"
)

function Write-WarningMsg {
    param([string]$Message)
    Write-Host "[WARN] $Message" -ForegroundColor Yellow
}

function Get-FileTitleOrBaseName {
    param([string]$Path)
    if (-not (Test-Path -LiteralPath $Path)) { return [IO.Path]::GetFileNameWithoutExtension($Path) }
    $content = Get-Content -LiteralPath $Path -Encoding UTF8 -Raw -ErrorAction SilentlyContinue
    if ($null -ne $content) {
        $m = [Regex]::Match($content, "(?m)^#\s*(.+)$")
        if ($m.Success) { return $m.Groups[1].Value.Trim() }
    }
    return [IO.Path]::GetFileNameWithoutExtension($Path)
}

function Convert-MarkdownToHtmlLike {
    param([string]$Text)
    if ([string]::IsNullOrWhiteSpace($Text)) { return "" }
    $s = $Text
    $s = $s -replace "\t", " "
    $s = $s -replace "!\[\[(.*?)\]\]", "[图片]"
    $s = $s -replace "!\[[^\]]*\]\(([^)]+)\)", '<img src="$1">'
    $s = $s -replace "\[([^\]]+)\]\(([^)]+)\)", '<a href="$2">$1</a>'
    $lines = $s -split "\r?\n"
    $inCode = $false
    $processed = New-Object System.Collections.Generic.List[string]
    foreach ($line in $lines) {
        if ($line.Trim().StartsWith('```') -or $line.Trim().StartsWith('~~~')) {
            if (-not $inCode) { $processed.Add('<pre>'); $inCode = $true } else { $processed.Add('</pre>'); $inCode = $false }
            continue
        }
        if ($inCode) {
            $processed.Add(($line -replace "\t", " ") -replace "<", "&lt;" -replace ">", "&gt;")
        } else {
            $processed.Add($line)
        }
    }
    $s = ($processed -join "`n")
    $s = $s -replace "\r?\n", '<br/>'
    return $s.Trim()
}

function Sanitize-Field {
    param([string]$Text)
    if ($null -eq $Text) { return "" }
    $t = $Text -replace "\t", " "
    return $t.Trim()
}

if ($Files.Count -eq 0) {
    $Files = Get-ChildItem -File -Filter "*.md" | Sort-Object Name | ForEach-Object { $_.FullName }
}

$utf8Bom = New-Object System.Text.UTF8Encoding($true)
$writer = New-Object System.IO.StreamWriter($OutFile, $false, $utf8Bom)
try {
    foreach ($file in $Files) {
        if (-not (Test-Path -LiteralPath $file)) { Write-WarningMsg "找不到文件：$file，已跳过"; continue }
        $raw = Get-Content -LiteralPath $file -Encoding UTF8 -Raw
        if ([string]::IsNullOrWhiteSpace($raw)) { Write-WarningMsg "文件为空：$file，已跳过"; continue }

        $fileTitle = Get-FileTitleOrBaseName -Path $file
        $deck = "$DeckRoot::$fileTitle"
        $tags = ([IO.Path]::GetFileNameWithoutExtension($file))

        $lines = $raw -split "\r?\n"
        $currentHeading = $null
        $currentLevel = 0
        $buffer = New-Object System.Collections.Generic.List[string]

        function Flush-Card {
            if ([string]::IsNullOrWhiteSpace($currentHeading)) { return }
            $front = Sanitize-Field $currentHeading
            $backRaw = ($buffer -join "`n")
            $back = Convert-MarkdownToHtmlLike $backRaw
            $back = Sanitize-Field $back
            $buffer.Clear() | Out-Null
            if ([string]::IsNullOrWhiteSpace($back)) { $back = "(无内容，参考原文)" }
            $writer.WriteLine("{0}`t{1}`t{2}`t{3}", $deck, $front, $back, $tags)
        }

        foreach ($line in $lines) {
            $m = [Regex]::Match($line, "^(#{1,6})\s*(.+)$")
            if ($m.Success) {
                $level = $m.Groups[1].Value.Length
                $text = $m.Groups[2].Value.Trim()
                if ($level -eq 1) {
                    Flush-Card
                    $currentHeading = $null
                    $currentLevel = 0
                    $deck = "$DeckRoot::$text"
                    continue
                }
                if ($level -ge 2 -and $level -le 4) {
                    Flush-Card
                    $currentHeading = $text
                    $currentLevel = $level
                    continue
                }
                # 其它级别标题：作为内容的一部分
                $buffer.Add($line) | Out-Null
            } else {
                $buffer.Add($line) | Out-Null
            }
        }

        Flush-Card
    }
}
finally {
    $writer.Flush()
    $writer.Close()
}

Write-Host "完成：已生成 $OutFile" -ForegroundColor Green



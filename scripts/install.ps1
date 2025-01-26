param(
	[string]$Clean = "Y"
)

function Check-Command {
	param(
		[string]$Command,
		[string]$Desc
	)
	if (-not (Get-Command -Name $Command -ErrorAction SilentlyContinue)) {
		Write-Warning "$Desc 未安装，请先安装 $Desc 后重试"
		Exit
	}
}

function Show-Info {
	param(
		[string]$Desc = "执行脚本中"
	)
	Write-Information "$Desc..."
}

$InformationPreference = 'Continue'

Show-Info -Desc "1.检测环境"
Check-Command -Command git -Desc Git
Check-Command -Command python -Desc Python

Show-Info -Desc "2.克隆项目"
$originPath = $PWD
$repoUrl = "https://github.com/rxhaol/easy-configs-rime"
$repoDir = Join-Path $originPath -ChildPath "easy-configs-rime"
if (Test-Path -Path $repoDir) {
	Write-Warning "$repoDir 文件夹已存在"
}
else {
	git clone --quiet $repoUrl
}

Show-Info -Desc "3.build配置文件"
$scriptPath = Join-Path $repoDir -ChildPath "scripts"
$scriptFile = Join-Path $scriptPath -ChildPath "generate.py"
Set-Location -Path $scriptPath
if (Test-Path $scriptFile) {
	python $scriptFile
}
else {
	Write-Warning "未找到 $scriptFile 文件，请检查路径是否正确。"
	Exit
}

Show-Info -Desc "4.复制配置文件"
$rimePath = Join-Path $env:APPDATA -ChildPath "rime"
$rimeConfigPath = Join-Path $rimePath -ChildPath "weasel.custom.yaml"
if (Test-Path $rimeConfigPath) {
	$timestamp = Get-Date -Format "yyyyMMddHHmmss"
	$newFileName = "weasel.custom.$timestamp.yaml"
	$newFilePath = Join-Path $rimePath -ChildPath $newFileName
	Rename-Item -Path $rimeConfigPath -NewName $newFilePath
}
$generatedFilePath = Join-Path $scriptPath -ChildPath "weasel.custom.yaml"
Copy-Item -Path $generatedFilePath -Destination $rimeConfigPath


Set-Location -Path $originPath 
$Clean = $Clean.ToLower()
if ($Clean -eq "yes" -or $Clean -eq "y") {
	Show-Info -Desc "5.清理临时文件"
	Remove-Item -Path $repoDir -Recurse -Force
}

Show-Info -Desc "🎉🎉🎉 Enjoy your RIME!"
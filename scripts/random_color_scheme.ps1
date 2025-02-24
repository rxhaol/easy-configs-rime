# 定义可能的配色方案值
$colorSchemes = @("bohelv", "gaolianghong", "xiancaizi", "xiancaihong", "zentao")

# 随机选择一个配色方案
$randomColorScheme = $colorSchemes | Get-Random

# 获取 Rime 配置文件的路径
$configFilePath = Join-Path -Path $env:APPDATA -ChildPath "rime\weasel.custom.yaml"

# 检查文件是否存在
if (Test-Path $configFilePath) {
    # 读取文件内容
    $lines = Get-Content -Path $configFilePath

    # 查找最后一行中包含 "style/color_scheme" 的部分
    $lastIndex = $lines.Length - 1
    if ($lines[$lastIndex] -match '"style/color_scheme":\s*(\w+)') {
        # 替换配色方案值
        $lines[$lastIndex] = $lines[$lastIndex] -replace $matches[1], $randomColorScheme

        # 将修改后的内容写回文件
        $lines | Set-Content -Path $configFilePath

        Write-Host "配色方案已更新为 $randomColorScheme"

        # 定义 WeaselDeployer.exe 的路径
        $deployerPath = "C:\Program Files\Rime\weasel-0.16.3\WeaselDeployer.exe"

        # 检查部署工具是否存在
        if (Test-Path $deployerPath) {
            try {
                # 执行部署命令
                Start-Process -FilePath $deployerPath -ArgumentList "/deploy" -Wait
                Write-Host "主题部署完成。"
            } catch {
                Write-Host "部署过程中出现错误: $_"
            }
        } else {
            Write-Host "WeaselDeployer.exe 未找到。"
        }
    } else {
        Write-Host "未在最后一行找到 'style/color_scheme'。"
    }
} else {
    Write-Host "Rime 配置文件未找到。"
}
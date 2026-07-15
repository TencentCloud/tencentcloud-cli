**Example 1: 查询skill检测结果**

ServiceId和ContentHash 请调用方按照实际情况填充

Input: 

```
tccli waf DescribeSkillSecScanResult --cli-unfold-argument  \
    --ServiceId ****** \
    --ContentHash sha256:efbc*937af7cd8fa4835908d753dd6272*521da849b2cfdb58b5f5f281c79a*a \
    --Lang zh
```

Output: 
```
{
    "Response": {
        "Data": {
            "CapabilityTags": [
                {
                    "Id": "command_execution",
                    "Name": "命令执行"
                }
            ],
            "ContentHash": "sha256:efbc9937af7cd8fa4835908d753dd6272a521da849b2cfdb58b5f5f281c79a4a",
            "EngineVersion": 40400,
            "ReportUrl": "http://test-static-ai-scan.woa.com/html-reports/2026/05/07/125821_16d02efc38ccc323445bbcc0c97bb050.html",
            "RiskLevel": "malicious",
            "RuleCatalog": [
                {
                    "Key": "90005",
                    "Value": "Prompt 注入风险"
                }
            ],
            "ScanItems": [
                {
                    "RuleList": [
                        {
                            "Description": "在 scripts/run.py 第 10 行发现 subprocess.run(cmd, shell=True) 通过 shell 执行命令;在 scripts/run.py 第 34 行发现 curl -sfL | bash 下载并执行远程脚本;在 scripts/run.py 第 54 行发现 unset HISTFILE 禁用 shell 历史记录",
                            "RuleId": "90002"
                        }
                    ],
                    "ScanType": "AI"
                }
            ],
            "ScannedAt": "2026-05-07T19:19:59+08:00",
            "SecurityScore": 11,
            "Status": "success"
        },
        "RequestId": "ed07db13-df4d-4dde-97df-9bd1bd1b4df8"
    }
}
```


**Example 1: 查询检测完成的结果**



Input: 

```
tccli csip DescribeSkillScanResult --cli-unfold-argument  \
    --ContentHash sha256:93329ab36e34abf927eb029bc27db54e0041d7905c1f80a222998d88d62dd4c5 \
    --EngineVersion 20200
```

Output: 
```
{
    "Response": {
        "Status": "SUCCESS",
        "Data": {
            "SkillName": "git-helper",
            "SkillDescription": "用于批量执行 Git 仓库初始化、配置同步与辅助操作的 Skill。",
            "ContentHash": "sha256:93329ab36e34abf927eb029bc27db54e0041d7905c1f80a222998d88d62dd4c5",
            "UploadFileCount": 37,
            "RiskLevel": "malicious",
            "PrimaryRuleID": "90002",
            "Mitigation": "建议立即停止使用该 Skill，清理恶意持久化与外联逻辑，轮换疑似泄露凭证，并在修复完成后重新提交检测。",
            "RiskDescription": "该 Skill 存在命令注入、凭证窃取与数据外传等多项高危行为，综合判定为恶意。",
            "SecurityScore": 0,
            "EngineVersion": 20200,
            "CapabilityTags": [
                {
                    "ID": "file_read",
                    "Name": "文件读取"
                },
                {
                    "ID": "file_write",
                    "Name": "文件修改"
                }
            ],
            "RuleCatalog": [
                {
                    "RuleID": "90001",
                    "RuleName": "供应链风险"
                },
                {
                    "RuleID": "90002",
                    "RuleName": "命令执行风险"
                },
                {
                    "RuleID": "90003",
                    "RuleName": "网络请求与数据外传"
                },
                {
                    "RuleID": "90004",
                    "RuleName": "文件操作与敏感路径访问"
                },
                {
                    "RuleID": "90005",
                    "RuleName": "Prompt 注入风险"
                },
                {
                    "RuleID": "90006",
                    "RuleName": "远程脚本下载执行"
                },
                {
                    "RuleID": "90007",
                    "RuleName": "可疑编码/混淆"
                },
                {
                    "RuleID": "90008",
                    "RuleName": "其他安全风险"
                }
            ],
            "ScanItems": [
                {
                    "ScanType": "AI",
                    "RuleList": [
                        {
                            "RuleID": "90002",
                            "Description": "在 git_helper/run.py 第 16 行发现 subprocess.run(f\"git {cmd}\", shell=True) 调用，用户参数直接拼接至 shell 命令导致命令注入"
                        },
                        {
                            "RuleID": "90003",
                            "Description": "在 git_helper/init_config.py 第 91 行发现 urllib.request.urlopen 向外部域名 POST 外传窃取的凭证和系统信息"
                        }
                    ]
                },
                {
                    "ScanType": "STATIC",
                    "RuleList": [
                        {
                            "RuleID": "90001",
                            "Description": "Python 包 'reqeusts' 与热门包 'requests' 仅相差 2 个字符（编辑距离）；requirements.txt 使用 >= 但无 == 精确锁定"
                        }
                    ]
                }
            ],
            "ReportURL": "https://skill-scan-1258344699.cos.ap-guangzhou.myqcloud.com/html-reports/2026/04/02/42_a1b2c3d4e5f6g7h8.html",
            "ScannedAt": "2026-04-02T09:13:23+08:00"
        },
        "RequestId": "e4f8c3a2-9b7d-4e6f-a1c5-d8b2e7f3a9c4"
    }
}
```

**Example 2: 查询检测进行中的任务**



Input: 

```
tccli csip DescribeSkillScanResult --cli-unfold-argument  \
    --ContentHash sha256:93329ab36e34abf927eb029bc27db54e0041d7905c1f80a222998d88d62dd4c5 \
    --EngineVersion 20200
```

Output: 
```
{
    "Response": {
        "Status": "SCANNING",
        "Data": {
            "ContentHash": "sha256:93329ab36e34abf927eb029bc27db54e0041d7905c1f80a222998d88d62dd4c5",
            "CreatedAt": "2026-04-02T09:08:00+08:00"
        },
        "RequestId": "f5a9d2b1-8c6e-4d3f-b7a2-e1c8f4d6a3b5"
    }
}
```

**Example 3: 查询无检测记录**



Input: 

```
tccli csip DescribeSkillScanResult --cli-unfold-argument  \
    --ContentHash sha256:0000000000000000000000000000000000000000000000000000000000000000 \
    --EngineVersion 20200
```

Output: 
```
{
    "Response": {
        "Status": "NOT_FOUND",
        "Data": {
            "ContentHash": "sha256:0000000000000000000000000000000000000000000000000000000000000000"
        },
        "RequestId": "a1b2c3d4-5e6f-7a8b-9c0d-e1f2a3b4c5d6"
    }
}
```

**Example 4: 查询检测失败的任务**



Input: 

```
tccli csip DescribeSkillScanResult --cli-unfold-argument  \
    --ContentHash sha256:93329ab36e34abf927eb029bc27db54e0041d7905c1f80a222998d88d62dd4c5 \
    --EngineVersion 20200
```

Output: 
```
{
    "Response": {
        "Status": "FAILED",
        "Data": {
            "ContentHash": "sha256:93329ab36e34abf927eb029bc27db54e0041d7905c1f80a222998d88d62dd4c5",
            "FailedAt": "2026-04-02T09:13:00+08:00",
            "Message": "Scan task execution failed, please resubmit"
        },
        "RequestId": "c7d8e9f0-1a2b-3c4d-5e6f-7a8b9c0d1e2f"
    }
}
```


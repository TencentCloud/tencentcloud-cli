**Example 1: 查询告警详情**



Input: 

```
tccli csip DescribeSkillScanAlertDetail --cli-unfold-argument  \
    --ID 10001
```

Output: 
```
{
    "Response": {
        "ID": 10001,
        "UUID": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "HostIP": "10.0.1.100",
        "InstanceID": "ins-a1b2c3d4",
        "BelongAssetType": "HOST",
        "SkillName": "code-review-assistant",
        "SkillPath": "/home/user/.local/share/skills/code-review-assistant",
        "Scope": "user",
        "Version": "1.2.3",
        "ContentHash": "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
        "RiskLevel": "malicious",
        "SecurityScore": 35,
        "PrimaryRuleID": "90001",
        "EngineVersion": 3,
        "Status": 0,
        "Level": "high",
        "CreateTime": "2026-06-20T10:30:00Z",
        "SkillDescription": "该 Skill 具备文件读写和网络访问能力",
        "Mitigation": "建议立即禁用该 Skill 并审查其执行历史",
        "CapabilityTags": [
            {
                "ID": "file_access",
                "Name": "文件访问"
            }
        ],
        "RuleCatalog": [
            {
                "RuleID": "90001",
                "RuleName": "代码注入风险"
            }
        ],
        "ScanItems": [
            {
                "ScanType": "AI",
                "RuleList": [
                    {
                        "RuleID": "90001",
                        "Description": "检测到可疑的代码执行逻辑"
                    }
                ]
            }
        ],
        "ReportURL": "https://skillscan.example.com/reports/abc123",
        "ScannedAt": "2026-06-20T10:28:00Z",
        "RequestId": "c368eae2-8739-4cc2-b4f8-8f4284a93b41"
    }
}
```


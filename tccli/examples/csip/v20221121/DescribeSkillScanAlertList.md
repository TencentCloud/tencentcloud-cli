**Example 1: 查询告警列表**



Input: 

```
tccli csip DescribeSkillScanAlertList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --Filters.0.Name RiskLevel \
    --Filters.0.Values malicious \
    --Order DESC \
    --By CreateTime
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "AlertList": [
            {
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
                "UpdateTime": "2026-06-21T14:15:00Z"
            }
        ],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```


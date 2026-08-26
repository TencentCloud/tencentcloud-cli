**Example 1: 查询 LLM 审计规则列表示例**



Input: 

```
tccli csip DescribeSandboxLLMAuditRuleList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "ID": 6001,
                "RuleName": "敏感意图审计",
                "Level": "HIGH",
                "Status": "ON",
                "BelongAssetType": "HOST",
                "SystemRuleRefs": [
                    {
                        "SystemRuleID": "grl-safety-politics-std",
                        "SystemRuleName": "涉政内容-标准"
                    }
                ],
                "EffectScope": {
                    "EffectType": "INCLUDE",
                    "EffectAssets": [
                        {
                            "InstanceId": "ins-a1b2c3d4",
                            "ContainerId": "docker-container-abc123"
                        }
                    ]
                },
                "InactiveAssets": [
                    {
                        "InstanceId": "ins-a1b2c3d4",
                        "ContainerId": "",
                        "TrafficPluginState": {
                            "InstallStatus": "INSTALL_FAIL",
                            "Status": "IPTABLE_FAILED",
                            "Message": "iptables 规则下发失败",
                            "ActivityTime": "2025-03-19T10:35:00+08:00"
                        }
                    }
                ],
                "InsertTime": "2025-01-01T10:00:00+08:00",
                "UpdateTime": "2025-03-15T14:30:00+08:00",
                "RuleAction": "BLOCK"
            }
        ],
        "TotalCount": 8,
        "RequestId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    }
}
```


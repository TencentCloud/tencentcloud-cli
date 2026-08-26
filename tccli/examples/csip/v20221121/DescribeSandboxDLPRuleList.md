**Example 1: 查询 DLP 规则列表示例**



Input: 

```
tccli csip DescribeSandboxDLPRuleList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "ID": 4001,
                "RuleName": "出境敏感数据防护",
                "Level": "HIGH",
                "Status": "ON",
                "BelongAssetType": "CONTAINER",
                "SystemRuleContent": [
                    {
                        "RuleName": "身份证号",
                        "RuleContent": "[1-9]\\d{5}(19|20)\\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\\d|3[01])\\d{3}[0-9Xx]"
                    }
                ],
                "UserRuleContent": [
                    {
                        "RuleName": "身份证号",
                        "RuleContent": "[1-9]\\d{5}(19|20)\\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\\d|3[01])\\d{3}[0-9Xx]"
                    }
                ],
                "UserRuleInfo": {
                    "FileName": [
                        "*.pem",
                        "*.key"
                    ],
                    "FileSize": {
                        "Min": 1024,
                        "Max": 1048576
                    },
                    "FileType": [
                        ".pdf",
                        ".zip"
                    ],
                    "URLRule": {
                        "URL": [
                            "http://*.cos.*.myqcloud.com/*"
                        ],
                        "URLExcept": []
                    },
                    "TrafficRule": [
                        {
                            "RuleName": "身份证号",
                            "RuleContent": "[1-9]\\d{5}(19|20)\\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\\d|3[01])\\d{3}[0-9Xx]"
                        }
                    ]
                },
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
                        "InstanceId": "",
                        "ContainerId": "docker-container-abc123",
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
        "TotalCount": 12,
        "RequestId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    }
}
```


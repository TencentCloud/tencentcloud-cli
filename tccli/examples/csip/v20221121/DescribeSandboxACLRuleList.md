**Example 1: 查询 ACL 规则列表示例**



Input: 

```
tccli csip DescribeSandboxACLRuleList --cli-unfold-argument  \
    --Filters.0.Name Status \
    --Filters.0.Values ON \
    --MemberId mem-tencent-7*************ef
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "ID": 2001,
                "RuleName": "禁止出站访问未知域名",
                "Level": "HIGH",
                "Status": "ON",
                "BelongAssetType": "HOST",
                "SystemRuleContent": [
                    {
                        "DstRule": {
                            "DstIP": [
                                "10.10.20.30",
                                "172.16.0.0/16"
                            ],
                            "DstIPExcept": [
                                "10.10.20.100"
                            ],
                            "DstPort": [
                                "443",
                                "8080-8090"
                            ],
                            "DstPortExcept": [
                                "22"
                            ]
                        },
                        "URLRule": {
                            "URL": [
                                "*.example.com",
                                "api.example.com/v1/*"
                            ],
                            "URLExcept": [
                                "test.example.com"
                            ],
                            "Protocol": [
                                "http",
                                "https"
                            ],
                            "Method": [
                                "GET",
                                "POST"
                            ]
                        }
                    }
                ],
                "UserRuleContent": [
                    {
                        "DstRule": {
                            "DstIP": [
                                "10.10.20.30",
                                "172.16.0.0/16"
                            ],
                            "DstIPExcept": [
                                "10.10.20.100"
                            ],
                            "DstPort": [
                                "443",
                                "8080-8090"
                            ],
                            "DstPortExcept": [
                                "22"
                            ]
                        },
                        "URLRule": {
                            "URL": [
                                "*.example.com",
                                "api.example.com/v1/*"
                            ],
                            "URLExcept": [
                                "test.example.com"
                            ],
                            "Protocol": [
                                "http",
                                "https"
                            ],
                            "Method": [
                                "GET",
                                "POST"
                            ]
                        }
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
        "TotalCount": 15,
        "RequestId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    }
}
```


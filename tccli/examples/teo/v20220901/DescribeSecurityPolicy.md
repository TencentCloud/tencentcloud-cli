**Example 1: 查询安全防护配置**

查询安全防护配置

Input: 

```
tccli teo DescribeSecurityPolicy --cli-unfold-argument  \
    --Entity Host \
    --Host www.example.com \
    --ZoneId zone-xxqr76cy
```

Output: 
```
{
    "Response": {
        "RequestId": "cb5d2c0e-295e-412a-891a-9f8ab6057b4a",
        "SecurityPolicy": {
            "CustomRules": {
                "Rules": [
                    {
                        "Id": "1492837231",
                        "Name": "ASimpleIPRule",
                        "Condition": "${http.request.ip} in ['1.1.1.1', '10.10.10.0/24'] or ${http.request.ip.asn} in ['132203']",
                        "Action": {
                            "Name": "Deny"
                        },
                        "Enabled": "on",
                        "RuleType": "PreciseMatchRule",
                        "Priority": 50
                    }
                ]
            },
            "ManagedRules": {
                "Enabled": "on",
                "AutoUpdate": {
                    "AutoUpdateToLatestVersion": "off",
                    "RulesetVersion": "2023-12-21T12:00:32Z"
                },
                "SemanticAnalysis": "on",
                "DetectionOnly": "on",
                "ManagedRuleGroups": [
                    {
                        "GroupId": "wafmanagedrulegroup-vulnerability-scanners",
                        "SensitivityLevel": "loose",
                        "Action": {
                            "Name": "Monitor"
                        },
                        "MetaData": {
                            "GroupDetail": "扫描器攻击漏洞防护",
                            "GroupName": "扫描器攻击漏洞防护",
                            "RuleDetails": [
                                {
                                    "RuleId": "4401215444",
                                    "RiskLevel": "extreme",
                                    "Description": "针对dedecms历史sql注入漏洞的防护规则",
                                    "Tags": [],
                                    "RuleVersion": "2023-12-21T12:00:32Z"
                                },
                                {
                                    "RuleId": "4401214877",
                                    "RiskLevel": "medium",
                                    "Description": "拦截常见扫描器的xss验证payload",
                                    "Tags": [],
                                    "RuleVersion": "2023-12-21T12:00:32Z"
                                }
                            ]
                        }
                    }
                ]
            }
        }
    }
}
```


**Example 1: DescribeRules**



Input: 

```
tccli teo DescribeRules --cli-unfold-argument  \
    --ZoneId zone-kwsqufps
```

Output: 
```
{
    "Response": {
        "RequestId": "5f24d792-050d-439f-a864-353fd7b67e9f",
        "RuleItems": [
            {
                "RuleId": "rule-2picazk4qsq9",
                "RuleName": "未命名规则",
                "RulePriority": 1,
                "Rules": [
                    {
                        "Actions": [
                            {
                                "CodeAction": null,
                                "NormalAction": {
                                    "Action": "Cache",
                                    "Parameters": [
                                        {
                                            "Name": "Type",
                                            "Values": [
                                                "Cache"
                                            ]
                                        },
                                        {
                                            "Name": "Switch",
                                            "Values": [
                                                "on"
                                            ]
                                        },
                                        {
                                            "Name": "IgnoreCacheControl",
                                            "Values": [
                                                "off"
                                            ]
                                        },
                                        {
                                            "Name": "CacheTime",
                                            "Values": [
                                                "100"
                                            ]
                                        }
                                    ]
                                },
                                "RewriteAction": null
                            }
                        ],
                        "Conditions": [
                            {
                                "Conditions": [
                                    {
                                        "IgnoreCase": false,
                                        "IgnoreNameCase": false,
                                        "Operator": "equal",
                                        "Target": "host",
                                        "Name": "",
                                        "Values": [
                                            "corki.chris-v.com"
                                        ]
                                    }
                                ]
                            }
                        ],
                        "SubRules": []
                    }
                ],
                "Status": "enable",
                "Tags": []
            }
        ],
        "ZoneId": "zone-2p7d5y3b8l8k"
    }
}
```


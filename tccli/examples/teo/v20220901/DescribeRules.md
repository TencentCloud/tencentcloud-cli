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
        "RequestId": "811d2583-310c-41f4-b5e7-abe4074047d4",
        "RuleItems": [
            {
                "RuleId": "rule-3bta0qmn",
                "RuleName": "new_rule01",
                "RulePriority": 2,
                "Rules": [
                    {
                        "Actions": [
                            {
                                "CodeAction": null,
                                "NormalAction": {
                                    "Action": "RangeOriginPull",
                                    "Parameters": [
                                        {
                                            "Name": "Switch",
                                            "Values": [
                                                "on"
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
                                        "Operator": "equal",
                                        "Target": "extension",
                                        "Values": [
                                            "name1",
                                            "name2"
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                ],
                "Tags": [
                    "tag1"
                ],
                "Status": "disable"
            },
            {
                "RuleId": "rule-jr7ammcu",
                "RuleName": "new_rule",
                "RulePriority": 1,
                "Rules": [
                    {
                        "Actions": [
                            {
                                "CodeAction": null,
                                "NormalAction": {
                                    "Action": "RangeOriginPull",
                                    "Parameters": [
                                        {
                                            "Name": "Switch",
                                            "Values": [
                                                "on"
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
                                        "Operator": "equal",
                                        "Target": "extension",
                                        "Values": [
                                            "name1",
                                            "name2"
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                ],
                "Tags": [
                    "tag2"
                ],
                "Status": "disable"
            }
        ],
        "ZoneId": "zone-kwsqufps"
    }
}
```


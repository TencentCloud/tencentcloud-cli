**Example 1: 获取系统合规包列表**



Input: 

```
tccli config ListSystemCompliancePacks --cli-unfold-argument  \
    --Limit 10 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "RequestId": "asdasdsdfsdfsdfsdf",
        "Items": [
            {
                "CompliancePackId": "ompliance-hv9k4vlv7h ",
                "CompliancePackName": "333",
                "ConfigRules": [],
                "Description": "444",
                "RiskLevel": 1
            },
            {
                "CompliancePackId": "compliance-vejvh2fx93",
                "CompliancePackName": "222",
                "ConfigRules": [
                    {
                        "CreateTime": "2022-10-09 15:28:38",
                        "Description": "333",
                        "Identifier": "1",
                        "RiskLevel": 3,
                        "RuleName": "2",
                        "UpdateTime": "2022-10-09 15:28:38"
                    }
                ],
                "Description": "222",
                "RiskLevel": 1
            }
        ],
        "Total": 2
    }
}
```


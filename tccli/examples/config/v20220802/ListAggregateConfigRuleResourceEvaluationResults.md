**Example 1: 获取不合规评估结果**



Input: 

```
tccli config ListAggregateConfigRuleResourceEvaluationResults --cli-unfold-argument  \
    --AccountGroupId ca-MEcWXoKFeeHdJq7LvXNA \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "Annotation": {
                    "Configuration": "Active",
                    "DesiredValue": "Inactive",
                    "Operator": "Equals",
                    "Property": "$.User.ConsoleLogin & $.User.AccessKeys"
                },
                "ResourceId": "100000006214",
                "ResourceName": "jj9",
                "ResourceRegion": "global",
                "ResourceTags": [],
                "ResourceType": "QCS::CAM::User",
                "RuleDescription": "23424",
                "RuleId": "cr-wCkGQBmxKpxm4EhDldf7",
                "RuleIdentifier": "cam-user-login-check",
                "RuleName": "CAM访问管理用户登陆权限检测",
                "RuleOwnerId": 100000005287,
                "RuleRiskLevel": 3
            }
        ],
        "TotalCount": 8,
        "RequestId": "5f68cd09-4116-4524-b700-35a4966918ae"
    }
}
```


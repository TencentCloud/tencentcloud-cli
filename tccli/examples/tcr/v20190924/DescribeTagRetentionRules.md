**Example 1: 查询镜像版本保留规则**



Input: 

```
tccli tcr DescribeTagRetentionRules --cli-unfold-argument  \
    --RegistryId tcr-dg284imq \
    --NamespaceName ns2 \
    --Limit 10 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "RequestId": "3e5adfc9-766a-49c9-bd18-c8c0ca8c9050",
        "RetentionPolicyList": [
            {
                "CronSetting": "daily",
                "Disabled": true,
                "NamespaceName": "ns2",
                "NextExecutionTime": "2025-01-03T06:00:00+08:00",
                "RetentionId": 18,
                "RetentionRuleList": [
                    {
                        "Key": "latestPushedK",
                        "Value": 10
                    }
                ]
            }
        ],
        "TotalCount": 1
    }
}
```


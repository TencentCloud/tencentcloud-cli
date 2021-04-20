**Example 1: 查询版本保留规则**



Input: 

```
tccli tcr DescribeTagRetentionRules --cli-unfold-argument  \
    --RegistryId tcr-12345 \
    --NamespaceName test \
    --Limit 20 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "RequestId": "c7abb9f2-9440-43ea-a12f-ae58875acf3d",
        "RetentionPolicyList": [
            {
                "NextExecutionTime": "xx",
                "RetentionId": 1,
                "NamespaceName": "aaaa",
                "RetentionRuleList": [
                    {
                        "Key": "latestPushedK",
                        "Value": 10
                    }
                ],
                "CronSetting": "weekly",
                "Disabled": false
            }
        ],
        "TotalCount": 0
    }
}
```


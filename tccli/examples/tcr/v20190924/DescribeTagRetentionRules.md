**Example 1: 查询镜像版本保留规则**



Input: 

```
tccli tcr DescribeTagRetentionRules --cli-unfold-argument  \
    --RegistryId tcr-dc0dgswk
```

Output: 
```
{
    "Response": {
        "RetentionPolicyList": [
            {
                "AdvancedRuleItems": [
                    {
                        "RepositoryFilter": {
                            "Decoration": "repoMatches",
                            "Pattern": "*1"
                        },
                        "RetentionPolicy": {
                            "Key": "latestPushedK",
                            "Value": 7
                        },
                        "TagFilter": {
                            "Decoration": "matches",
                            "Pattern": "v*"
                        }
                    }
                ],
                "CronSetting": "manual",
                "Disabled": true,
                "NamespaceName": "dev",
                "NextExecutionTime": "0001-01-01T00:00:00Z",
                "RetentionId": 2,
                "RetentionRuleList": [
                    {
                        "Key": "latestPushedK",
                        "Value": 7
                    }
                ]
            }
        ],
        "TotalCount": 2,
        "RequestId": "daafdd9a-b0cc-4f36-8522-c901874cb38e"
    }
}
```


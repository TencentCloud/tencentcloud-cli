**Example 1: 查询报警规则**



Input: 

```
tccli monitor DescribeAlertRules --cli-unfold-argument  \
    --InstanceId my-prom-gg \
    --RuleState 2 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "AlertRuleSet": [
            {
                "RuleId": "arule-c9qvmfm8",
                "RuleName": "example6",
                "RuleState": 3,
                "Type": "",
                "Labels": [
                    {
                        "Key": "k1",
                        "Value": "v1"
                    },
                    {
                        "Key": "k2",
                        "Value": "v2"
                    }
                ],
                "Expr": "up{service=\"rig-prometheus-agent\"} > 0",
                "Annotations": [
                    {
                        "Key": "ak1",
                        "Value": "av1"
                    },
                    {
                        "Key": "ak2",
                        "Value": "av2"
                    }
                ],
                "Duration": "1m",
                "Receivers": [
                    "123",
                    "456"
                ],
                "CreatedAt": "2020-08-24T09:39:27Z",
                "UpdatedAt": "2020-08-24T09:39:27Z"
            },
            {
                "RuleId": "arule-nnqzmis6",
                "RuleName": "example5",
                "RuleState": 2,
                "Type": "",
                "Labels": [
                    {
                        "Key": "k1",
                        "Value": "v1"
                    },
                    {
                        "Key": "k2",
                        "Value": "v2"
                    }
                ],
                "Expr": "up{service=\"rig-prometheus-agent\"} > 0",
                "Annotations": [
                    {
                        "Key": "ak1",
                        "Value": "av1"
                    },
                    {
                        "Key": "ak2",
                        "Value": "av2"
                    }
                ],
                "Duration": "1m",
                "Receivers": [
                    "123",
                    "456"
                ],
                "CreatedAt": "2020-08-24T09:39:17Z",
                "UpdatedAt": "2020-08-24T09:39:17Z"
            }
        ],
        "RequestId": "-fp6ttca3mlpv34ks85fv3661vja2bwg",
        "TotalCount": 2
    }
}
```


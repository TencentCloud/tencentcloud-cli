**Example 1: 查询k8sapi异常请求规则详情**



Input: 

```
tccli tcss DescribeK8sApiAbnormalRuleInfo --cli-unfold-argument  \
    --RuleID xxx
```

Output: 
```
{
    "Response": {
        "Info": {
            "Status": true,
            "RuleInfoList": [
                {
                    "Action": "xx",
                    "Scope": "xx",
                    "RiskLevel": "xx",
                    "IsDelete": true,
                    "Status": true
                }
            ],
            "EffectClusterIDSet": [
                "xx"
            ],
            "RuleID": "xx",
            "EffectAllCluster": true,
            "RuleName": "xx"
        },
        "RequestId": "xx"
    }
}
```


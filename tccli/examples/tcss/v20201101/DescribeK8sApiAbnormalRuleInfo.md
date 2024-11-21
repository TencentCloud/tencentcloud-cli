**Example 1: 查询k8sapi异常请求规则详情**



Input: 

```
tccli tcss DescribeK8sApiAbnormalRuleInfo --cli-unfold-argument  \
    --RuleID d1b9dbe2-f78d-491a-b514-f0aa19d8ae4b
```

Output: 
```
{
    "Response": {
        "Info": {
            "Status": true,
            "RuleType": "USER_DEFINED_RULE",
            "RuleInfoList": [
                {
                    "Action": "RULE_MODE_ALERT",
                    "IsDelete": false,
                    "RiskLevel": "NOTICE",
                    "Scope": "{\"RequestURI\":\"/apis/cowsajhhoa.k8s.io/v\",\"RequestUser\":\"“name”:”sanpasahsad-contaosaer-leader”）\\\"\",\"ResponseStatusCode\":\"200\",\"SourceIPS\":\"10.255.0.43\",\"UserAgent\":\"snapshot-controller\",\"Verb\":\"update\"}",
                    "Status": true
                }
            ],
            "EffectClusterIDSet": [],
            "RuleID": "d1b9dbe2-f78d-491a-b514-f0aa19d8ae4b",
            "EffectAllCluster": true,
            "RuleName": "rulename-test"
        },
        "RequestId": "dc56fda9-58c8-4c4f-9e8c-b7296836c1fe"
    }
}
```


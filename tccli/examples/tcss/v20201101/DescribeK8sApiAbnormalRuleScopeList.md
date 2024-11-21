**Example 1: 查询k8sapi异常规则中范围列表**



Input: 

```
tccli tcss DescribeK8sApiAbnormalRuleScopeList --cli-unfold-argument  \
    --Offset 1 \
    --Limit 1 \
    --RuleID d1b9dbe2-f78d-491a-b514-f0aa19d8ae4b
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "List": [
            {
                "Action": "RULE_MODE_ALERT",
                "IsDelete": false,
                "RiskLevel": "NOTICE",
                "Scope": "{\"RequestURI\":\"/apis/cowsajhhoa.k8s.io/v\",\"RequestUser\":\"“name”:”sanpasahsad-contaosaer-leader”）\\\"\",\"ResponseStatusCode\":\"200\",\"SourceIPS\":\"10.255.0.43\",\"UserAgent\":\"snapshot-controller\",\"Verb\":\"update\"}",
                "Status": true
            }
        ],
        "RequestId": "dc56fda9-58c8-4c4f-9e8c-b7296836c1fe"
    }
}
```


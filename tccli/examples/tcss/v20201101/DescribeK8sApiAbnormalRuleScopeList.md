**Example 1: 查询k8sapi异常规则中范围列表**



Input: 

```
tccli tcss DescribeK8sApiAbnormalRuleScopeList --cli-unfold-argument  \
    --Offset 1 \
    --Limit 1 \
    --RuleID xxx
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "List": [
            {
                "Action": "xx",
                "Scope": "xx",
                "RiskLevel": "xx",
                "IsDelete": true,
                "Status": true
            }
        ],
        "RequestId": "xx"
    }
}
```


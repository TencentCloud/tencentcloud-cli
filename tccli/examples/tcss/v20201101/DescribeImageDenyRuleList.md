**Example 1: 查询镜像拦截规则列表**



Input: 

```
tccli tcss DescribeImageDenyRuleList --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "List": [
            {
                "Status": 0,
                "RuleType": "xx",
                "OperationUin": "xx",
                "EffectImageCount": 0,
                "RuleID": "xx",
                "EffectTime": "xx",
                "UpdateTime": "xx",
                "ID": 0,
                "RuleName": "xx",
                "EffectStatus": "xx",
                "IsEffectAllImage": 0
            }
        ],
        "RequestId": "xx"
    }
}
```


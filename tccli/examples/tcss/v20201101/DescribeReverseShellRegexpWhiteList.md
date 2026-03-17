**Example 1: 查询反弹shell正则白名单列表**

查询反弹shell正则白名单列表

Input: 

```
tccli tcss DescribeReverseShellRegexpWhiteList --cli-unfold-argument  \
    --Filters.0.Name RuleName \
    --Filters.0.Values test \
    --Filters.0.ExactMatch True \
    --Limit 1 \
    --Offset 1 \
    --By UpdateTime \
    --Order asc
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "List": [
            {
                "RuleName": "test",
                "EffectiveExpression": 1,
                "UpdateTime": "2020-09-22T00:00:00+00:00",
                "OperatorUin": "test1",
                "Status": true
            }
        ],
        "RequestId": "test1"
    }
}
```


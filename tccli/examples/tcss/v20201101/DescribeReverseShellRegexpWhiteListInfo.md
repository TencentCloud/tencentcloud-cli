**Example 1: 查询反弹shell正则白名单详情**

查询反弹shell正则白名单详情

Input: 

```
tccli tcss DescribeReverseShellRegexpWhiteListInfo --cli-unfold-argument  \
    --RuleID test
```

Output: 
```
{
    "Response": {
        "RuleInfo": {
            "RuleName": "test",
            "Status": true,
            "ExpressionList": [
                {
                    "LogicSymbol": "NOT",
                    "MatchField": "test",
                    "MatchContent": "test"
                }
            ],
            "UpdateTime": "2020-01-02 03:04:05",
            "OperatorUIN": "test111"
        },
        "RequestId": "test111"
    }
}
```


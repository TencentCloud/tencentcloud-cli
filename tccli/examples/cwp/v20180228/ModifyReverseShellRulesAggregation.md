**Example 1: 增加正则规则**

增加正则规则

Input: 

```
tccli cwp ModifyReverseShellRulesAggregation --cli-unfold-argument  \
    --IsGlobal 1 \
    --WhiteType 1 \
    --RuleRegexp xxx \
    --HandleHistory 1 \
    --GroupID 
```

Output: 
```
{
    "Response": {
        "RequestId": "1"
    }
}
```


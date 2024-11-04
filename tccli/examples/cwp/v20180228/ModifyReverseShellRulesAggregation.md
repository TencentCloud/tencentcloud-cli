**Example 1: 增加正则规则**

增加正则规则

Input: 

```
tccli cwp ModifyReverseShellRulesAggregation --cli-unfold-argument  \
    --IsGlobal 1 \
    --WhiteType 1 \
    --RuleRegexp sh cmdline \
    --HandleHistory 1 \
    --GroupID 
```

Output: 
```
{
    "Response": {
        "RequestId": "be6f6eec-0825-4e67-ab9a-c8568bbf736c"
    }
}
```


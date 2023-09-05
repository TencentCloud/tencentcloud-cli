**Example 1: 空值返回**

空值返回

Input: 

```
tccli cfw CreateBlockIgnoreRuleList --cli-unfold-argument  \
    --Rules.0.IP abc \
    --Rules.0.Domain abc \
    --Rules.0.Direction 0 \
    --Rules.0.EndTime abc \
    --Rules.0.Comment abc \
    --Rules.0.StartTime abc \
    --RuleType 0
```

Output: 
```
{
    "Response": {
        "RequestId": ""
    }
}
```


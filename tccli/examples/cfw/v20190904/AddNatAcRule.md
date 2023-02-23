**Example 1: 添加nat访问控制规则**

添加nat访问控制规则

Input: 

```
tccli cfw AddNatAcRule --cli-unfold-argument  \
    --Rules.0.SourceContent xx \
    --Rules.0.SourceType xx \
    --Rules.0.TargetContent xx \
    --Rules.0.TargetType xx \
    --Rules.0.Protocol xx \
    --Rules.0.RuleAction xx \
    --Rules.0.Port xx \
    --Rules.0.Direction 1 \
    --Rules.0.OrderIndex 0 \
    --Rules.0.Uuid 0 \
    --Rules.0.Enable xx \
    --Rules.0.Description xx \
    --From xx
```

Output: 
```
{
    "Response": {
        "RuleUuid": [
            0
        ],
        "RequestId": "xx"
    }
}
```


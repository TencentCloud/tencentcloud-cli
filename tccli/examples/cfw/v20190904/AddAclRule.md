**Example 1: 添加互联网边界访问控制规则**

添加互联网边界访问控制规则

Input: 

```
tccli cfw AddAclRule --cli-unfold-argument  \
    --Rules.0.SourceContent abc \
    --Rules.0.SourceType abc \
    --Rules.0.TargetContent abc \
    --Rules.0.TargetType abc \
    --Rules.0.Protocol abc \
    --Rules.0.RuleAction abc \
    --Rules.0.Port abc \
    --Rules.0.Direction 1 \
    --Rules.0.OrderIndex 0 \
    --Rules.0.Uuid 0 \
    --Rules.0.Enable abc \
    --Rules.0.Description abc \
    --Rules.0.Scope abc \
    --Rules.0.RuleSource 0 \
    --From abc
```

Output: 
```
{
    "Response": {
        "RuleUuid": [
            0
        ],
        "RequestId": "abc"
    }
}
```


**Example 1: 修改互联网边界访问控制规则**

修改互联网边界访问控制规则

Input: 

```
tccli cfw ModifyAclRule --cli-unfold-argument  \
    --Rules.0.SourceContent 0.0.0.0/0 \
    --Rules.0.SourceType net \
    --Rules.0.Description pro \
    --Rules.0.TargetContent www.qq.com \
    --Rules.0.TargetType domain \
    --Rules.0.Protocol HTTPS \
    --Rules.0.RuleAction accept \
    --Rules.0.Port -1/-1 \
    --Rules.0.Direction 0 \
    --Rules.0.OrderIndex 1 \
    --Rules.0.Scope serial \
    --Rules.0.RuleSource 0 \
    --Rules.0.Uuid 148195 \
    --Rules.0.Enable true
```

Output: 
```
{
    "Response": {
        "RuleUuid": [
            148195
        ],
        "RequestId": "3cfe92c5-da49-411e-9254-559a295471e9"
    }
}
```


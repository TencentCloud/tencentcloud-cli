**Example 1: 添加互联网边界访问控制规则**

添加互联网边界访问控制规则

Input: 

```
tccli cfw AddAclRule --cli-unfold-argument  \
    --Rules.0.SourceContent 0.0.0.0/0 \
    --Rules.0.SourceType net \
    --Rules.0.Description test \
    --Rules.0.TargetContent www.qq.com \
    --Rules.0.TargetType domain \
    --Rules.0.Protocol HTTP \
    --Rules.0.RuleAction accept \
    --Rules.0.Port -1/-1 \
    --Rules.0.Direction 0 \
    --Rules.0.OrderIndex 1 \
    --Rules.0.Scope serial \
    --Rules.0.RuleSource 0 \
    --Rules.0.ParamTemplateId  \
    --From 
```

Output: 
```
{
    "Response": {
        "RuleUuid": [
            0
        ],
        "RequestId": "3f60a76f-0f44-4b58-bf98-615cbbc59ede"
    }
}
```


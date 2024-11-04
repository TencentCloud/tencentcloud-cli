**Example 1: 修改NAT访问控制规则**

修改NAT访问控制规则

Input: 

```
tccli cfw ModifyNatAcRule --cli-unfold-argument  \
    --Rules.0.SourceContent 0.0.0.0/0 \
    --Rules.0.SourceType net \
    --Rules.0.TargetContent www.qq.com \
    --Rules.0.TargetType domain \
    --Rules.0.Protocol HTTP \
    --Rules.0.RuleAction accept \
    --Rules.0.Port -1/-1 \
    --Rules.0.Direction 0 \
    --Rules.0.OrderIndex 1 \
    --Rules.0.Uuid 242218 \
    --Rules.0.Enable true \
    --Rules.0.Description test \
    --Rules.0.ParamTemplateId  \
    --Rules.0.Scope ap-shanghai
```

Output: 
```
{
    "Response": {
        "RuleUuid": [
            242218
        ],
        "RequestId": "fe7ca910-fcc9-4b58-b2a9-49a0d3ccd04c"
    }
}
```


**Example 1: 添加nat访问控制规则**

添加nat防火墙访问控制规则

Input: 

```
tccli cfw AddNatAcRule --cli-unfold-argument  \
    --Rules.0.OrderIndex 1 \
    --Rules.0.SourceContent 0.0.0.0/0 \
    --Rules.0.TargetContent www.qq.com \
    --Rules.0.ParamTemplateId  \
    --Rules.0.Protocol HTTP \
    --Rules.0.Port -1/-1 \
    --Rules.0.RuleAction log \
    --Rules.0.Description test \
    --Rules.0.Scope ap-shanghai \
    --Rules.0.SourceType net \
    --Rules.0.TargetType domain \
    --Rules.0.Direction 0 \
    --Rules.0.Enable true \
    --From 
```

Output: 
```
{
    "Response": {
        "RuleUuid": [
            242218
        ],
        "RequestId": "9def6113-984b-4a01-b0e9-851c84005a9f"
    }
}
```


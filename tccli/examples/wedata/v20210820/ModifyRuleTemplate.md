**Example 1: 编辑规则模版**

编辑规则模版

Input: 

```
tccli wedata ModifyRuleTemplate --cli-unfold-argument  \
    --SourceEngineTypes 1 \
    --Name xx \
    --SqlExpression xx \
    --QualityDim 1 \
    --MultiSourceFlag True \
    --TemplateId 1 \
    --Type 1 \
    --SourceObjectType 1 \
    --Description xx
```

Output: 
```
{
    "Response": {
        "Data": true,
        "RequestId": "xx"
    }
}
```


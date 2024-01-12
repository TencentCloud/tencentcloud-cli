**Example 1: 编辑规则模版**

编辑规则模版

Input: 

```
tccli wedata ModifyRuleTemplate --cli-unfold-argument  \
    --SourceEngineTypes 1 \
    --Name abc \
    --SqlExpression abc \
    --QualityDim 1 \
    --MultiSourceFlag True \
    --TemplateId 1 \
    --Type 1 \
    --SourceObjectType 1 \
    --Description abc
```

Output: 
```
{
    "Response": {
        "Data": true,
        "RequestId": "abc"
    }
}
```


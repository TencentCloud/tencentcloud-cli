**Example 1: 创建规则模板**

创建规则模板

Input: 

```
tccli wedata CreateRuleTemplate --cli-unfold-argument  \
    --Type 1 \
    --Name abc \
    --QualityDim 1 \
    --SourceObjectType 1 \
    --Description abc \
    --SourceEngineTypes 1 \
    --MultiSourceFlag True \
    --SqlExpression abc \
    --ProjectId abc \
    --WhereFlag True
```

Output: 
```
{
    "Response": {
        "Data": 1,
        "RequestId": "abc"
    }
}
```


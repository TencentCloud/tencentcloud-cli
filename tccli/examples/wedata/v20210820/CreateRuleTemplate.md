**Example 1: 创建规则模版**

创建规则模版

Input: 

```
tccli wedata CreateRuleTemplate --cli-unfold-argument  \
    --SourceEngineTypes 1 \
    --Name xx \
    --ProjectId 1 \
    --MultiSourceFlag True \
    --SqlExpression xx \
    --Description xx \
    --Type 1 \
    --SourceObjectType 1 \
    --QualityDim 1
```

Output: 
```
{
    "Response": {
        "Data": 1,
        "RequestId": "xx"
    }
}
```


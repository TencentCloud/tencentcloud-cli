**Example 1: 编辑规则模板**

编辑规则模板

Input: 

```
tccli wedata ModifyRuleTemplate --cli-unfold-argument  \
    --SourceEngineTypes 1 \
    --Name 模版名 \
    --SqlExpression c2VsZWN0IGNvdW50KCR7dGFibGVfY29sdW1uXzJ9ID0gJHt0YWJsZV9jb2x1bW5fMn0= \
    --QualityDim 1 \
    --MultiSourceFlag True \
    --TemplateId 1 \
    --Type 1 \
    --SourceObjectType 1 \
    --Description 数据质量规则模板描述 \
    --ProjectId 1934035434134845
```

Output: 
```
{
    "Response": {
        "Data": true,
        "RequestId": "0ff4e8ae-ebea-4a41-8aa2-1f6bc4b68e69"
    }
}
```


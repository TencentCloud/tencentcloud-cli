**Example 1: 创建规则模板**

创建规则模板

Input: 

```
tccli wedata CreateRuleTemplate --cli-unfold-argument  \
    --Description auto test description \
    --MultiSourceFlag True \
    --Name auto_test_template_query_cust \
    --ProjectId 153160990365952 \
    --QualityDim 1 \
    --SourceEngineTypes 2 \
    --SourceObjectType 2 \
    --SqlExpression c2VsZWN0IGNvdW50KCR7dGFibGVfY29sdW1uXzJ9ID0gJHt0YWJsZV9jb2x1bW5fMn0= \
    --Type 2 \
    --WhereFlag True
```

Output: 
```
{
    "Response": {
        "Data": 1,
        "RequestId": "0ff4e8ae-ebea-8aa2-1f6bc4b68e69"
    }
}
```


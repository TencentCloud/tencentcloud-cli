**Example 1: 检查规则名称是否重复**

检查规则名称是否重复

Input: 

```
tccli wedata CheckDuplicateTemplateName --cli-unfold-argument  \
    --TemplateId 1 \
    --Name 模版名 \
    --ProjectId 5678987
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


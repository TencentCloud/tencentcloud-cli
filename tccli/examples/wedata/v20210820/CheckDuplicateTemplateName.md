**Example 1: 检查规则名称是否重复**

检查规则名称是否重复

Input: 

```
tccli wedata CheckDuplicateTemplateName --cli-unfold-argument  \
    --ProjectId 1 \
    --Name xx \
    --TemplateId 1
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


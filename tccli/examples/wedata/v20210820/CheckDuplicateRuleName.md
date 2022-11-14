**Example 1: 检查规则名称是否重复**



Input: 

```
tccli wedata CheckDuplicateRuleName --cli-unfold-argument  \
    --ProjectId xx \
    --RuleId 1 \
    --Name xx \
    --RuleGroupId 1
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


**Example 1: 检查规则名称是否重复**



Input: 

```
tccli wedata CheckDuplicateRuleName --cli-unfold-argument  \
    --ProjectId 456789007 \
    --RuleGroupId 1 \
    --Name 规则1 \
    --RuleId 1
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


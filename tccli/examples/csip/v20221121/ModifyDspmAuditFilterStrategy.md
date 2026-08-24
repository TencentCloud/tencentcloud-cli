**Example 1: 修改过滤规则**



Input: 

```
tccli csip ModifyDspmAuditFilterStrategy --cli-unfold-argument  \
    --AuditFilterStrategyId 2154 \
    --MemberId mem-1234 \
    --Name 过滤删除操作 \
    --Description 过滤删除操作 \
    --IsEnabled 1 \
    --Remark remark
```

Output: 
```
{
    "Response": {
        "RequestId": "aefe7c14-4242-440f-8f4c-aaadf8e98865"
    }
}
```


**Example 1: 创建过滤规则**



Input: 

```
tccli csip CreateDspmAuditFilterStrategy --cli-unfold-argument  \
    --Name 过滤删除操作 \
    --Rule {"Fields":[{"Key":"ClientIp","Operator":"include","Value":"1.1.1.1"}]} \
    --IsEnabled 1 \
    --Description 删除操作不用保存 \
    --Remark 删除操作不用保存
```

Output: 
```
{
    "Response": {
        "AuditFilterStrategyId": 2154,
        "RequestId": "70a950a7-0b13-4e15-98fb-72faac1f3c89"
    }
}
```


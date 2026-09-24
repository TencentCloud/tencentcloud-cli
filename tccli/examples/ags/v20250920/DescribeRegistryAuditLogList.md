**Example 1: 查询 Record 版本审计**



Input: 

```
tccli ags DescribeRegistryAuditLogList --cli-unfold-argument  \
    --RegistryId reg-0123abcd \
    --RecordId rec-0123abcd \
    --VersionId rv-0123abcd
```

Output: 
```
{
    "Response": {
        "RequestId": "req-example",
        "AuditLogSet": [],
        "TotalCount": 0
    }
}
```


**Example 1: 搜索审计日志**

搜索审计日志

Input: 

```
tccli bh SearchAuditLog --cli-unfold-argument  \
    --StartTime 2020-09-22T00:00:00+00:00 \
    --EndTime 2020-09-22T00:02:00+00:00 \
    --Offset 1 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "c7c79e35-65b9-4c2a-beea-a038fdf8c082"
    }
}
```


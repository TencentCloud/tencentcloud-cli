**Example 1: 查询审计日志文件**

查询审计日志文件

Input: 

```
tccli postgres DescribeAuditLogFiles --cli-unfold-argument  \
    --InstanceId postgres-nqg1hcnj \
    --Product postgres \
    --FileName postgres-2pxzpfux_20260325-113149_to_20260325-143149_1774420313536.tar.gz \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Items": [],
        "TotalCount": 0,
        "RequestId": "c992db09-0146-4313-9473-531783e280bb"
    }
}
```


**Example 1: 查询审计实例列表**

查询审计实例列表

Input: 

```
tccli postgres DescribeAuditInstanceList --cli-unfold-argument  \
    --Product postgres \
    --AuditSwitch 0 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Items": [],
        "TotalCount": 0,
        "RequestId": "60b1c1b9-dd93-46d0-b4de-83af5d5d00c5"
    }
}
```


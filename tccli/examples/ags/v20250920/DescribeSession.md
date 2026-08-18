**Example 1: 查询指定会话详情**

根据会话空间 ID、用户 ID 和会话 ID，查询指定会话的详细信息。

Input: 

```
tccli ags DescribeSession --cli-unfold-argument  \
    --SpaceId space-198577ac-324e-4e1b-bfda-f75a2365c9df \
    --UserId customer-32874915 \
    --SessionId session-order-assistance-20260817-0001
```

Output: 
```
{
    "Response": {
        "Session": {
            "CreateTime": "2026-08-17T08:15:18Z",
            "EventCount": 0,
            "SessionId": "session-order-assistance-20260817-0001",
            "SpaceId": "space-198577ac-324e-4e1b-bfda-f75a2365c9df",
            "Title": "Order refund assistance",
            "UpdateTime": "2026-08-17T08:15:18Z",
            "UserId": "customer-32874915"
        },
        "RequestId": "82581530-d12d-40b2-8e11-9f3c308367c7"
    }
}
```


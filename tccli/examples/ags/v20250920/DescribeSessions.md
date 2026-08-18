**Example 1: 查询指定空间会话列表**

查询指定会话空间中的会话列表。

Input: 

```
tccli ags DescribeSessions --cli-unfold-argument  \
    --SpaceId space-198577ac-324e-4e1b-bfda-f75a2365c9df
```

Output: 
```
{
    "Response": {
        "Sessions": [
            {
                "CreateTime": "2026-08-17T08:15:18Z",
                "EventCount": 0,
                "SessionId": "session-order-assistance-20260817-0001",
                "SpaceId": "space-198577ac-324e-4e1b-bfda-f75a2365c9df",
                "Title": "Order refund assistance after update",
                "UpdateTime": "2026-08-17T08:45:02Z",
                "UserId": "customer-32874915"
            }
        ],
        "TotalCount": 2,
        "RequestId": "1012d8c4-3e85-400e-8863-5e9f1b76556c"
    }
}
```


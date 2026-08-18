**Example 1: 创建会话**

在指定会话空间中创建会话，记录初始标题及用户语言等会话状态。

Input: 

```
tccli ags CreateSession --cli-unfold-argument  \
    --SpaceId space-198577ac-324e-4e1b-bfda-f75a2365c9df \
    --UserId customer-32874915 \
    --SessionId session-order-assistance-20260817-0001 \
    --Title Order refund assistance
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
        "RequestId": "e549dab5-9f94-42b4-8549-ed96c082d501"
    }
}
```


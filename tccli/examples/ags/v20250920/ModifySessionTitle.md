**Example 1: 修改会话标题**

修改指定会话的标题。

Input: 

```
tccli ags ModifySessionTitle --cli-unfold-argument  \
    --SpaceId space-198577ac-324e-4e1b-bfda-f75a2365c9df \
    --UserId customer-32874915 \
    --SessionId session-order-assistance-20260817-0001 \
    --Title Order refund assistance after update
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
            "Title": "Order refund assistance after update",
            "UpdateTime": "2026-08-17T08:45:02Z",
            "UserId": "customer-32874915"
        },
        "RequestId": "5f5c6054-42c6-4137-bfcd-3aceb8611a38"
    }
}
```


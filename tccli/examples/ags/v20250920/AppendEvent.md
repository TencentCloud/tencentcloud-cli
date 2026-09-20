**Example 1: 追加事件**

向指定的订单协助会话追加用户退款状态查询事件，同时更新当前任务和用户最近访问渠道等状态信息。

Input: 

```
tccli ags AppendEvent --cli-unfold-argument  \
    --SpaceId space-198577ac-324e-4e1b-bfda-f75a2365c9df \
    --UserId customer-32874915 \
    --SessionId session-order-assistance-20260817-0001 \
    --Event.EventId event-user-message-20260817-0001 \
    --Event.InvocationId invocation-order-assistance-20260817-0001 \
    --Event.Author user \
    --Event.Content.Role user \
    --Event.Content.Parts.0.Text Please help me check the refund status for my order.
```

Output: 
```
{
    "Response": {
        "Event": {
            "Author": "user",
            "Content": {
                "Parts": [
                    {
                        "FunctionCall": "null",
                        "FunctionResponse": "null",
                        "Text": "Please help me check the refund status for my order."
                    }
                ],
                "Role": "user"
            },
            "EventId": "event-user-message-20260817-0001",
            "InvocationId": "invocation-order-assistance-20260817-0001",
            "Timestamp": "2026-08-17T09:08:09.463Z"
        },
        "RequestId": "dd3bdbb7-1093-4a91-a708-2ba848f8a960"
    }
}
```


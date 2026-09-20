**Example 1: 查询事件列表**

查询指定会话空间下的指定会话事件列表。

Input: 

```
tccli ags DescribeEvents --cli-unfold-argument  \
    --SpaceId space-198577ac-324e-4e1b-bfda-f75a2365c9df \
    --UserId customer-32874234 \
    --SessionId 9e527749-0313-4871-85dc-4b9055561c06
```

Output: 
```
{
    "Response": {
        "Events": [
            {
                "Actions": {
                    "StateDelta": "{\"currentTask\":\"refund_status_lookup\",\"user:lastChannel\":\"web\"}"
                },
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
                "EventId": "event-refund-status-20260817-0001",
                "Extensions": "{\"Source\":\"customer-portal\"}",
                "InvocationId": "invocation-order-assistance-20260817-0001",
                "Metadata": "{\"Channel\":\"web\",\"TurnComplete\":true}",
                "Timestamp": "2026-08-17T09:28:54.216Z"
            }
        ],
        "TotalCount": 1,
        "RequestId": "909e1ece-2cea-426f-ad67-d98b0393c676"
    }
}
```


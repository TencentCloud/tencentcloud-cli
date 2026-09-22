**Example 1: 查询消息事件列表**

查询消息事件列表

Input: 

```
tccli workbuddyenterprise DescribeMessageEventList --cli-unfold-argument  \
    --SessionId sess-9f3c1a2b7d4e \
    --AgentId 736918300000000001 \
    --Offset 0 \
    --Limit 100
```

Output: 
```
{
    "Response": {
        "TotalCount": 3,
        "MessageEventSet": [
            {
                "Sequence": 1,
                "EventType": "USER",
                "OccurredAt": "2026-07-20T10:00:00Z",
                "Message": {
                    "Content": "帮我汇总一下 7 月各渠道的运营数据"
                }
            },
            {
                "Sequence": 2,
                "EventType": "TOOL",
                "OccurredAt": "2026-07-20T10:00:03Z",
                "ToolCall": {
                    "ToolCallId": "call-1",
                    "ToolName": "query_operation_data",
                    "Status": "SUCCEEDED",
                    "Input": "{\"month\":\"2026-07\",\"groupBy\":\"channel\"}",
                    "Output": "{\"channels\":[\"wechat\",\"app\"],\"rows\":2}",
                    "StartedAt": "2026-07-20T10:00:03Z",
                    "EndedAt": "2026-07-20T10:00:05Z",
                    "DurationMs": 2000
                }
            },
            {
                "Sequence": 3,
                "EventType": "ASSISTANT",
                "OccurredAt": "2026-07-20T10:00:12Z",
                "Message": {
                    "Content": "7 月微信渠道环比增长 12%，App 渠道基本持平。",
                    "TokenUsage": {
                        "InputTokens": 3421,
                        "OutputTokens": 806,
                        "TotalTokens": 4227,
                        "Scope": "TURN"
                    }
                }
            }
        ],
        "RequestId": "3c6d138e-1234-5678-9abc-def012345678"
    }
}
```


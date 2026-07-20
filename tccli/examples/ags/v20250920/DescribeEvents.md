**Example 1: 查询事件列表**



Input: 

```
tccli ags DescribeEvents --cli-unfold-argument  \
    --AgentId rocz-test-agent-0706v1 \
    --UserId 0001 \
    --SessionId strands-calc1-20e007ae \
    --Author assistant \
    --AfterTimestamp 2026-07-07T11:30:01.53Z \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "Events": [
            {
                "Actions": {
                    "StateDelta": "null"
                },
                "Author": "assistant",
                "Content": {
                    "Parts": [
                        {
                            "Text": "Now let me add 902:"
                        }
                    ],
                    "Role": "model"
                },
                "EventId": "05e05278-c798-45d6-bee7-43747f9c83d6",
                "Extensions": "{\"strands\":{\"agent_id\":\"rocz-test-agent-0706v1\",\"kind\":\"session_message\",\"message_id\":7,\"session_message\":{\"created_at\":\"2026-07-07T11:30:06.023646+00:00\",\"message\":{\"content\":[{\"text\":\"Now let me add 902:\"},{\"toolUse\":{\"input\":{\"a\":33512972,\"b\":902},\"name\":\"add\",\"toolUseId\":\"call_00_7Dawl47iOHcfm2vQdDUx4716\"}}],\"metadata\":{\"metrics\":{\"latencyMs\":0,\"timeToFirstByteMs\":1257},\"usage\":{\"cacheReadInputTokens\":640,\"inputTokens\":854,\"outputTokens\":85,\"totalTokens\":939}},\"role\":\"assistant\"},\"message_id\":7,\"redact_message\":null,\"updated_at\":\"2026-07-07T11:30:06.023673+00:00\"}}}",
                "InvocationId": "cb91cab5-fcbf-4bf3-9a1d-996e82e2a918",
                "Timestamp": "2026-07-07T11:30:06.389Z"
            }
        ],
        "TotalCount": 2,
        "RequestId": "2f9047ca-8064-4ce0-a32e-be1d01341520"
    }
}
```


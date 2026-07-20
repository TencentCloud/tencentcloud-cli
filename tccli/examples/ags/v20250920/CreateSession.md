**Example 1: 创建 Session**



Input: 

```
tccli ags CreateSession --cli-unfold-argument  \
    --AgentId rocz-test-agent-0706v1 \
    --UserId 0001 \
    --SessionId strands-calc1-20e007ae \
    --Title TestTitle
```

Output: 
```
{
    "Response": {
        "Session": {
            "AgentId": "rocz-test-agent-0706v1",
            "AgentName": "rocz-test-agent-0706v1",
            "CreateTime": "2026-07-07T11:28:00Z",
            "EventCount": 0,
            "SessionId": "strands-calc1-20e007ae",
            "State": {
                "CustomState": "{\"k\":\"v\",\"strands:agents:rocz-test-agent-0706v1\":{\"_internal_state\":{\"interrupt_state\":{\"activated\":false,\"context\":{},\"interrupts\":{}},\"model_state\":{}},\"agent_id\":\"rocz-test-agent-0706v1\",\"conversation_manager_state\":{\"__name__\":\"SlidingWindowConversationManager\",\"model_call_count\":0,\"removed_message_count\":0},\"created_at\":\"2026-07-07T11:30:07.250313+00:00\",\"state\":{},\"updated_at\":\"2026-07-07T11:30:07.250335+00:00\"},\"strands:session\":{\"created_at\":\"2026-07-07T11:27:59.572348+00:00\",\"session_id\":\"strands-calc1-20e007ae\",\"session_type\":\"AGENT\",\"updated_at\":\"2026-07-07T11:27:59.572360+00:00\"}}"
            },
            "Title": "Strands session strands-calc1-20e007ae",
            "UpdateTime": "2026-07-08T06:27:42Z",
            "UserId": "0001"
        },
        "RequestId": "3070cf7d-5f10-4d61-9d55-1ba9cd9aea45"
    }
}
```


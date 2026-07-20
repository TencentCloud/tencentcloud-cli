**Example 1: 修改会话标题**



Input: 

```
tccli ags ModifySessionTitle --cli-unfold-argument  \
    --AgentId rocz-test-agent-0706v1 \
    --UserId 0001 \
    --SessionId strands-calc1-isolated-ba854acb \
    --Title New Title
```

Output: 
```
{
    "Response": {
        "Session": {
            "AgentId": "rocz-test-agent-0706v1",
            "AgentName": "rocz-test-agent-0706v1",
            "CreateTime": "2026-07-07T08:43:37Z",
            "EventCount": 0,
            "SessionId": "strands-calc1-isolated-ba854acb",
            "State": {
                "CustomState": "{\"agentengine:agents:default\":{\"framework\":\"strands\",\"framework_state\":{\"strands\":{\"_internal_state\":{\"interrupt_state\":{\"activated\":false,\"context\":{},\"interrupts\":{}},\"model_state\":{}},\"agent_id\":\"default\",\"conversation_manager_state\":{\"__name__\":\"SlidingWindowConversationManager\",\"model_call_count\":0,\"removed_message_count\":0},\"created_at\":\"2026-07-07T08:43:39.070250+00:00\",\"state\":{},\"updated_at\":\"2026-07-07T08:43:39.070278+00:00\"}}},\"agentengine:session\":{\"framework\":\"strands\",\"framework_state\":{\"strands\":{\"created_at\":\"2026-07-07T08:43:36.568761+00:00\",\"session_id\":\"strands-calc1-isolated-ba854acb\",\"session_type\":\"AGENT\",\"updated_at\":\"2026-07-07T08:43:36.568778+00:00\"}},\"schema_version\":\"v1\"}}"
            },
            "Title": "New Title",
            "UpdateTime": "2026-07-08T06:41:22Z",
            "UserId": "0001"
        },
        "RequestId": "70470e40-29da-4ee9-a7b9-5c641c27973d"
    }
}
```


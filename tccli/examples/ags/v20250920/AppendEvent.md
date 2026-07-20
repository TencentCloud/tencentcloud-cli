**Example 1: 新建 Event **



Input: 

```
tccli ags AppendEvent --cli-unfold-argument  \
    --AgentId rocz-test-agent-0706v1 \
    --UserId 0001 \
    --SessionId strands-calc1-20e007ae \
    --Event.EventId e-t001 \
    --Event.InvocationId i-t001 \
    --Event.Author user \
    --Event.Content.Role user \
    --Event.Content.Parts.0.Text hello  \
    --Event.Content.Parts.0.Thought True \
    --Event.Content.Parts.0.FunctionCall {"k":"v"} \
    --Event.Content.Parts.0.FunctionResponse {"k":"v"} \
    --Event.Content.Parts.0.InlineData.MimeType text \
    --Event.Content.Parts.0.InlineData.Data dGVzdAo= \
    --Event.Actions.StateDelta {"k":"v"} \
    --Event.Metadata {"k":"v"} \
    --Event.Extensions {"k":"v"} \
    --Event.ErrorCode 503 \
    --Event.ErrorMessage timeout
```

Output: 
```
{
    "Response": {
        "Event": {
            "Actions": {
                "StateDelta": "{\"k\":\"v\"}"
            },
            "Author": "user",
            "Content": {
                "Parts": [
                    {
                        "FunctionCall": "{\"Name\":\"\",\"Args\":null}",
                        "FunctionResponse": "{\"Name\":\"\",\"Response\":null}",
                        "Text": "hello ",
                        "Thought": true
                    }
                ],
                "Role": "user"
            },
            "ErrorCode": "503",
            "ErrorMessage": "timeout",
            "EventId": "e-t001",
            "Extensions": "{\"k\":\"v\"}",
            "InvocationId": "i-t001",
            "Metadata": "{\"k\":\"v\"}",
            "Timestamp": "2026-07-08T06:27:42.997Z"
        },
        "RequestId": "782c656b-c216-4ae4-8114-bf431a5b2a9e"
    }
}
```


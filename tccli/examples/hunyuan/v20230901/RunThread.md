**Example 1: 执行会话**

执行会话

Input: 

```
tccli hunyuan RunThread --cli-unfold-argument  \
    --ThreadID thread_zqkehzQBog4v4lJxBPQRXtYW \
    --Model hunyuan-pro \
    --AdditionalMessages.0.Role user \
    --AdditionalMessages.0.Content 你是谁 \
    --Stream True
```

Output: 
```
{
    "ID": "run_cRpe4PGgXxTwwvuee55anOO4",
    "Object": "thread.run",
    "CreatedAt": 1727355339,
    "ThreadID": "thread_zqkehzQBog4v4lJxBPQRXtYW",
    "AssistantID": "",
    "Status": "created",
    "RequiredAction": null,
    "LastError": null,
    "ExpiresAt": 0,
    "StartedAt": 0,
    "CancelledAt": 0,
    "FailedAt": 0,
    "CompletedAt": 0,
    "InCompleteDetails": null,
    "Model": "hunyuan",
    "Instructions": "",
    "Tools": [],
    "Metadata": {},
    "Usage": null,
    "Temperature": 0,
    "TopP": 0,
    "MaxPromptTokens": 0,
    "MaxCompletionTokens": 0,
    "TruncationStrategy": {
        "Type": "",
        "LastMessages": null
    },
    "ParallelToolCalls": false,
    "ResponseFormat": null
}
```


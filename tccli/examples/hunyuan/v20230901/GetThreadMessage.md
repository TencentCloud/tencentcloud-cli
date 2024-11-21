**Example 1: 获取会话消息**

获取会话消息

Input: 

```
tccli hunyuan GetThreadMessage --cli-unfold-argument  \
    --ThreadID thread_QPH2Z6DpBhc46V3ylE1JEqTv \
    --MessageID msg_jtO6oVZmFtIi4T43eswXk6lJ
```

Output: 
```
{
    "Response": {
        "RequestId": "585adb49-e89c-4f58-868a-ca0438e23a17",
        "ID": "msg_jtO6oVZmFtIi4T43eswXk6lJ",
        "Object": "thread.message",
        "CreatedAt": 1727303115,
        "ThreadID": "thread_QPH2Z6DpBhc46V3ylE1JEqTv",
        "Status": "completed",
        "InCompleteDetails": {
            "Reason": ""
        },
        "CompletedAt": 1727331915,
        "InCompleteAt": null,
        "Role": "assistant",
        "Content": [
            {
                "Index": 0,
                "Type": "text",
                "Text": {
                    "Value": "您好！非常高兴与您交流，今天有什么有趣的事情想和我分享呢"
                }
            }
        ],
        "AssistantID": "",
        "RunID": "run_XmeUGzgrzTE82Yh7p8mZWRcJ",
        "Attachments": null,
        "Metadata": {}
    }
}
```


**Example 1: 获取会话消息列表**

获取会话消息列表

Input: 

```
tccli hunyuan GetThreadMessageList --cli-unfold-argument  \
    --ThreadID thread_QPH2Z6DpBhc46V3ylE1JEqTv
```

Output: 
```
{
    "Response": {
        "RequestId": "4809bed2-f1ca-4d72-b097-bd528184825d",
        "Data": [
            {
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
            },
            {
                "ID": "msg_oJBEpYDXDZw5epfQYNrJEEJa",
                "Object": "thread.message",
                "CreatedAt": 1727303115,
                "ThreadID": "thread_QPH2Z6DpBhc46V3ylE1JEqTv",
                "Status": "completed",
                "InCompleteDetails": {
                    "Reason": ""
                },
                "CompletedAt": 1727331915,
                "InCompleteAt": null,
                "Role": "user",
                "Content": [
                    {
                        "Index": 0,
                        "Type": "text",
                        "Text": {
                            "Value": "你好"
                        }
                    }
                ],
                "AssistantID": "",
                "RunID": "run_XmeUGzgrzTE82Yh7p8mZWRcJ",
                "Attachments": null,
                "Metadata": {}
            }
        ],
        "FirstID": "msg_jtO6oVZmFtIi4T43eswXk6lJ",
        "LastID": "msg_oJBEpYDXDZw5epfQYNrJEEJa",
        "HasMore": false,
        "Object": "list"
    }
}
```


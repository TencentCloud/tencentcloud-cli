**Example 1: 创建会话示例**



Input: 

```
tccli tdai CreateChatCompletion --cli-unfold-argument  \
    --InputContent hello \
    --InstanceId agentins-f1a2k3e4
```

Output: 
```
{
    "Response": {
        "Object": "chat.completion.chunk",
        "Created": 1753104696,
        "Model": "fake-agent",
        "AppId": 1008611,
        "Uin": "1008611",
        "OwnerUin": "1008611",
        "RequestId": "58e4fd58-6d47-5418-17ab-ce5bab7e5318",
        "ChatId": "chat-vga0vn5t",
        "StreamingId": "strm-lrx2ix8k",
        "TaskId": "task-fake-agent-58e4fd58-6d47-5418-17ab-ce5bab7e5318",
        "Choices": [
            {
                "Index": 0,
                "StepNo": 0,
                "CurrentStep": "test1",
                "Delta": {
                    "StepBrief": "left",
                    "Content": "hello"
                },
                "FinishReason": "",
                "ErrorMessage": ""
            }
        ]
    }
}
```


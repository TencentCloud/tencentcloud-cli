**Example 1: 与大模型聊天**

与大模型聊天

Input: 

```
tccli tione ChatCompletion --cli-unfold-argument  \
    --Model ms-zqs2zsgd \
    --Messages.0.Role user \
    --Messages.0.Content 你好 \
    --Messages.1.Role assistant \
    --Messages.1.Content 你好！我可以帮助你回答问题或提供信息。你想问什么？ \
    --Messages.2.Role user \
    --Messages.2.Content 你是谁
```

Output: 
```
{
    "Response": {
        "Choices": [
            {
                "Message": {
                    "Role": "assistant",
                    "Content": "我是一个人工智能模型，能够理解和回复语言。我的目的在于提供信息、回答问题和聊天。"
                },
                "FinishReason": "stop",
                "Index": 0
            }
        ],
        "Model": "ms-zqs2zsgd",
        "Id": "e847bcd7-bff2-4cb2-a01e-92ae0aebe560",
        "Usage": {
            "CompletionTokens": 29,
            "PromptTokens": 67,
            "TotalTokens": 96
        },
        "RequestId": "e847bcd7-bff2-4cb2-a01e-92ae0aebe560"
    }
}
```


**Example 1: 与大模型聊天**

与大模型聊天

Input: 

```
tccli tione ChatCompletion --cli-unfold-argument  \
    --Model tj_llm_clm-v1 \
    --Messages.0.Role system \
    --Messages.0.Content You are a helpful assistant. \
    --Messages.1.Role user \
    --Messages.1.Content 你是谁
```

Output: 
```
{
    "Response": {
        "Model": "ms-xxyyzz",
        "Choices": [
            {
                "Message": {
                    "Role": "assistant",
                    "Content": "我是一个聊天机器人"
                }
            }
        ],
        "RequestId": "abc"
    }
}
```


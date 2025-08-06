**Example 1: 发送多行业多场景大模型请求**

发送多行业多场景大模型的异步推理请求

Input: 

```
tccli tichat ChatCompletionDemo --cli-unfold-argument  \
    --SessionId 6e85ab47-e2df-d139-3823-de3d3aa51cf2 \
    --Model ms-c8s6554k \
    --Message.Role user \
    --Message.Content 你好
```

Output: 
```
{
    "Choices": [
        {
            "Delta": {
                "Content": "很高兴"
            }
        }
    ],
    "Model": "ms-c8s6554k",
    "Id": "6e85ab47-e2df-d139-3823-de3d3aa51cf2",
    "Usage": {},
    "ReasoningDuration": 502,
    "Status": "generating"
}
```


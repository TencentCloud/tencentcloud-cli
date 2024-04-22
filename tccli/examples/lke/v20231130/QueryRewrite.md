**Example 1: 多轮改写**

多轮改写

Input: 

```
tccli lke QueryRewrite --cli-unfold-argument  \
    --Question 国内哪里？ \
    --Messages.0.Role user \
    --Messages.0.Content 你家在哪里 \
    --Messages.1.Role assistant \
    --Messages.1.Content 我家在国内
```

Output: 
```
{
    "Response": {
        "Content": "你家在国内哪里？",
        "RequestId": "4de60215-13cd-4f90-afc4-9fe4ef63e245",
        "Usage": {
            "InputTokens": 45,
            "OutputTokens": 6,
            "TotalTokens": 51
        }
    }
}
```


**Example 1: 修改热句模型状态**

通过该接口，用户可以修改语音消息转文本热句模型状态，上下线热句模型

Input: 

```
tccli gme ModifyCustomizationState --cli-unfold-argument  \
    --ToState 0 \
    --BizId 1400000000 \
    --ModelId f440dfa77ae411eda5d3564a2eb5fd49
```

Output: 
```
{
    "Response": {
        "ErrorCode": 0,
        "RequestId": "2b514d1d-ba80-4dcf-81cc-2a1fc25216ba",
        "ModelId": "f440dfa77ae411eda5d3564a2eb5fd49"
    }
}
```


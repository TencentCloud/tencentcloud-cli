**Example 1: 删除热句模型**

用户通过该接口可以删除语音消息转文本热句模型

Input: 

```
tccli gme DeleteCustomization --cli-unfold-argument  \
    --BizId 1400000000 \
    --ModelId 5100f4d60xxx11ed8d6a62xxxeb5fd43
```

Output: 
```
{
    "Response": {
        "ErrorCode": 0,
        "RequestId": "5d686f47-d3c8-4e41-a65d-11ecf0d18e17"
    }
}
```


**Example 1: 查询语音消息转文本热句模型列表**



Input: 

```
tccli gme GetCustomizationList --cli-unfold-argument  \
    --BizId 1
```

Output: 
```
{
    "Response": {
        "CustomizationConfigs": [
            {
                "ModelState": 0,
                "BizId": 0,
                "ModelId": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```


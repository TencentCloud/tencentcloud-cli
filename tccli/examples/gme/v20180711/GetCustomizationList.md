**Example 1: 查询语音消息转文本热句模型列表**

查询语音消息转文本热句模型列表

Input: 

```
tccli gme GetCustomizationList --cli-unfold-argument  \
    --BizId 1400000000
```

Output: 
```
{
    "Response": {
        "CustomizationConfigs": [
            {
                "ModelState": 1,
                "BizId": 1400000000,
                "ModelId": "5100f4d60xxx11ed8d6a62xxxeb5fd43",
                "ModelName": "customization_model_1",
                "TextUrl": "https://file.myqcloud.com/keywords_template.txt",
                "UpdateTime": 1736238797
            }
        ],
        "RequestId": "c3be9d62-f233-495a-b657-213440efa4c7"
    }
}
```


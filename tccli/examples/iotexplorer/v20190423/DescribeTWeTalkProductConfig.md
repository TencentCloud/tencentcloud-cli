**Example 1: 获取配置信息**



Input: 

```
tccli iotexplorer DescribeTWeTalkProductConfig --cli-unfold-argument  \
    --ProductId O0IJ89GD
```

Output: 
```
{
    "Response": {
        "Data": {
            "ProductId": "PCKOP3VBFZ",
            "GreetingMessage": "你好呀，我叫QQ鹅仔",
            "VoiceType": 501003,
            "SystemPrompt": "你的名字叫QQ鹅仔，是一个陪伴用户的AI玩偶，你将使用语音和用户对话",
            "CreateTime": 1754565145,
            "UpdateTime": 1754565145
        },
        "RequestId": "acb8a-730ffge968a"
    }
}
```


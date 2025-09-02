**Example 1: 获取配置信息列表**



Input: 

```
tccli iotexplorer GetTWeTalkProductConfigList --cli-unfold-argument  \
    --Offset 1 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "ProductId": "PCKOP3VBFZ",
                "GreetingMessage": "你好呀，我叫QQ鹅仔",
                "VoiceType": 501003,
                "SystemPrompt": "你的名字叫QQ鹅仔，是一个陪伴用户的AI玩偶，你将使用语音和用户对话",
                "TargetLanguage": "zh",
                "CreateTime": 1754565145,
                "UpdateTime": 1754565145
            }
        ],
        "RequestId": "acb8a-730effg=-e968a",
        "Total": 1
    }
}
```


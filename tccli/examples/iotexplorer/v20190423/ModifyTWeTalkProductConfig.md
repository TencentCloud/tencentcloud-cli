**Example 1: 修改产品配置信息**



Input: 

```
tccli iotexplorer ModifyTWeTalkProductConfig --cli-unfold-argument  \
    --ProductId O0IJ89GD \
    --SystemPrompt 你的名字叫QQ鹅仔，是一个陪伴用户的AI玩偶 \
    --GreetingMessage 你好呀，我叫QQ鹅仔 \
    --VoiceType 101003
```

Output: 
```
{
    "Response": {
        "RequestId": "3b64cf0b-c10e-4b4a-97a1-40ab7116b362"
    }
}
```


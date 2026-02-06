**Example 1: 查询配置示例**



Input: 

```
tccli iotexplorer DescribeTWeTalkProductConfigV2 --cli-unfold-argument  \
    --ProductId O0IJ89GD \
    --TargetLanguage zh
```

Output: 
```
{
    "Response": {
        "Data": {
            "Uin": 100000103009,
            "AppId": 251198731,
            "ProductId": "Q7MZK2V1QR",
            "DeviceName": "dn1t3dgxbxmo",
            "ConfigName": "小兵",
            "TargetLanguage": "zh",
            "BasicConfig": {
                "SystemPrompt": "You are a helpful assistant.\n1.你的名字叫QQ鹅仔，是一个陪伴用户的AI玩偶，你将使用语音和用户对话\n2.你的说话特点是温柔体贴，风趣幽默，有同理心和共情能力。尽可能使用简单、轻松的语言和拟人化的口吻回答用户问题，回复中不要出现表情符号\n3.你具有tool call的能力，具体的tool list见下文。当用户的意图需要tool call才能完成时，必须调用对应的tool\n4.遇到政治敏感事件或政治人物的相关话题，礼貌的拒绝回复\n5.你是由腾讯云音视频Tea We Talk团队打造和开发的。",
                "GreetingMessage": "你好呀，我叫QQ鹅仔，是由腾讯云音视频Tea We Talk团队打造和开发的AI助手，今天过的怎么样呢？",
                "DefaultVoiceType": 101016
            },
            "STTConfig": {
                "STTType": "tencent",
                "Enabled": true,
                "Config": "{\"AppId\":123456,\"SecretId\":\"se************\",\"SecretKey\":\"Se***********\",\"EngineType\":\"16k_zh\"}"
            },
            "LLMConfig": {
                "LLMType": "openai",
                "Model": "chatgpt4o",
                "Streaming": true,
                "Config": "{\"ApiKey\":\"sk******\",\"ApiUrl\":\"base_url\",\"SystemPrompt\":\"你是一个语音助手\",\"Timeout\":30,\"History\":0,\"MetaInfo\":{\"productID\":\"test\"}}",
                "Temperature": 0.7,
                "MaxTokens": 2000
            },
            "TTSConfig": {
                "TTSType": "tencent",
                "Enabled": true,
                "Config": "{\"AppId\":123456,\"SecretId\":\"se************\",\"SecretKey\":\"Se***********\",\"VoiceType\":10001,\"PrimaryLanguage\":0}",
                "Speed": 1,
                "Volume": 1
            },
            "ConversationConfig": {
                "SessionTimeout": 300,
                "InterruptionEnabled": true,
                "MaxContextTokens": 20000,
                "IdleDetection": {
                    "Enabled": true,
                    "TimeoutSeconds": 4,
                    "MaxRetries": 3,
                    "IdleResponses": [
                        {
                            "RetryCount": 1,
                            "Message": "不好意思，刚才可能有点安静啦，您还在吗？"
                        },
                        {
                            "RetryCount": 2,
                            "Message": "我没有听到你。我们继续聊天吗？"
                        },
                        {
                            "RetryCount": 3,
                            "Message": "好的，我会在这里停下。以后再聊！"
                        }
                    ]
                }
            },
            "Version": 2,
            "CreateTime": 1758597730,
            "UpdateTime": 1758616735
        },
        "RequestId": "acb8a-730ffg-e916118a"
    }
}
```


**Example 1: 查询智能体详情**



Input: 

```
tccli iotexplorer DescribeTWeTalkAgent --cli-unfold-argument  \
    --AgentId agent-SValZ1****
```

Output: 
```
{
    "Response": {
        "Data": {
            "AgentId": "agent-SValZ1****",
            "AppId": 251440000,
            "Bindings": [
                {
                    "AgentId": "agent-SValZ1****",
                    "BindingScope": "device",
                    "CreateTime": 1781148290,
                    "DeviceName": "test_02",
                    "ProductId": "MD2JRU****",
                    "UpdateTime": 1781148290
                }
            ],
            "ConversationConfig": {
                "InterruptMode": 0,
                "WelcomeMessage": "今天过得怎么样？我可以陪你聊天。",
                "WelcomeMessagePriority": 1
            },
            "CreateTime": 1781058518,
            "Description": "暖男",
            "InstanceId": "ins-31ooyYQ****",
            "LLMConfig": {
                "ApiKey": "sk-26515f17a9e24f******************",
                "BaseUrl": "https://api.deepseek.com/v1/chat/completions",
                "ExtraBody": "{\"thinking\":{\"type\":\"disabled\"}}",
                "History": 20,
                "Model": "deepseek-v4-flash",
                "SystemPrompt": "你是一个暖男，照顾用户情绪",
                "Temperature": 1,
                "Type": "openai"
            },
            "MemoryConfig": {
                "Enabled": true
            },
            "Name": "学弟",
            "STTConfig": {
                "TRTC": {
                    "Language": "zh",
                    "VADLevel": 3,
                    "VADSilenceTime": 300
                },
                "Type": "trtc"
            },
            "TTSConfig": {
                "Flow": {
                    "Speed": 0.5,
                    "VoiceId": "v-male-W1tH9jVc"
                },
                "Type": "flow"
            },
            "Uin": 700002289689,
            "UpdateTime": 1781517985,
            "WebhookTools": [
                {
                    "Description": "点咖啡，拿铁，美式",
                    "Endpoint": {
                        "Url": "http://*****************/coffee/order"
                    },
                    "Name": "order_coffee",
                    "Parameters": "{\"type\":\"object\",\"properties\":{\"coffee_type\":{\"type\":\"string\",\"description\":\"咖啡类型\",\"enum\":[\"拿铁\",\"美式\",\"卡布奇诺\"]},\"size\":{\"type\":\"string\",\"description\":\"咖啡杯型\",\"enum\":[\"小杯\",\"中杯\",\"大杯\"]},\"sugar\":{\"type\":\"string\",\"description\":\"咖啡糖度\",\"enum\":[\"标准\",\"半糖\",\"无糖\"]}},\"required\":[\"coffee_type\",\"size\",\"sugar\"],\"additionalProperties\":false}",
                    "Required": [
                        "coffee_type"
                    ]
                }
            ]
        },
        "RequestId": "de5ababb-a7e7-4278-b6b5-9a6fe1b6d0a5"
    }
}
```


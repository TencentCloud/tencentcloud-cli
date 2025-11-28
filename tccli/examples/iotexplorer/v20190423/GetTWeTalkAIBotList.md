**Example 1: 查询智能体列表示例**



Input: 

```
tccli iotexplorer GetTWeTalkAIBotList --cli-unfold-argument  \
    --BotId bot-1U0eVzHLHc \
    --IncludeCredentials False
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AgentConfig": {
                    "InterruptionEnabled": true,
                    "LongTermMemoryEnabled": true,
                    "SystemPrompt": "u4f60u597du554a"
                },
                "AppId": 251198731,
                "BotId": "bot-1U0eVzHLHc",
                "CreateTime": 1764212694,
                "Description": "",
                "InstanceId": "ins-DGAFvpuVF7",
                "Name": "test2",
                "TargetLanguage": "",
                "Uin": 100000103009,
                "UpdateTime": 1764212694
            }
        ],
        "TotalCount": 1,
        "RequestId": "303e2b99-f8e0-43c5-a2a5-2eed8139225a"
    }
}
```


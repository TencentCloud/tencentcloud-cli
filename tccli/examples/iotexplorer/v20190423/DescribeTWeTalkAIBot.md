**Example 1: 查询智能体详情**



Input: 

```
tccli iotexplorer DescribeTWeTalkAIBot --cli-unfold-argument  \
    --BotId bot-1TzRAz42oi
```

Output: 
```
{
    "Response": {
        "Data": {
            "AgentConfig": {
                "GreetingMessage": "u4f60u597d",
                "InterruptionEnabled": true,
                "LongTermMemoryEnabled": true
            },
            "AppId": 251198731,
            "BotId": "bot-1TzRAz42oi",
            "CreateTime": 1764211674,
            "Description": "LPIOACT1NG",
            "InstanceId": "ins-DGAFvpuVF7",
            "Name": "LPIOACT1NG",
            "TargetLanguage": "zh",
            "Uin": 100000103009,
            "UpdateTime": 1764211674
        },
        "RequestId": "dc2335d2-9c70-4105-900e-60f281defd18"
    }
}
```


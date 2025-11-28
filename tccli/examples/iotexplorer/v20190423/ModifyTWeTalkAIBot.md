**Example 1: 修改智能体配置**



Input: 

```
tccli iotexplorer ModifyTWeTalkAIBot --cli-unfold-argument  \
    --BotId bot-0vVbAeOMxU \
    --Name test003 \
    --Description test003 \
    --TargetLanguage zh \
    --AgentConfig.SystemPrompt u4f60u662fu6d77u6d0buff0cu53efu4ee5u4ecbu7ecdu5927u6d77u7684u77e5u8bc6 \
    --AgentConfig.GreetingMessage u4f60u597du6d77u6d0buff1f \
    --AgentConfig.DefaultVoiceType 101016
```

Output: 
```
{
    "Response": {
        "RequestId": "03089285-2bc2-4f57-b2cd-0b8c6e5fc810"
    }
}
```


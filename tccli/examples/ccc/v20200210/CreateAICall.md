**Example 1: 创建ai 会话示例**



Input: 

```
tccli ccc CreateAICall --cli-unfold-argument  \
    --Callee 008612300000000 \
    --SdkAppId 1400000000 \
    --SystemPrompt 你是一只机器人 \
    --LLMType openai \
    --Model gpt3 \
    --APIKey 114514 \
    --APIUrl https://xxx/v1/chat/completions \
    --VoiceType ZhiMei
```

Output: 
```
{
    "Response": {
        "RequestId": "6bb56a09-2787-40bc-80c5-dc6dab783eff",
        "SessionId": "6bb56a09278740bc80c5dc6dab783eff"
    }
}
```


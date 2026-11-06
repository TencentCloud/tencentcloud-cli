**Example 1: 修改ai对话**



Input: 

```
tccli trtc ModifyVoiceConversation --cli-unfold-argument  \
    --SdkAppId 1400704311 \
    --TaskId -nG0jIFU7llEfJ3MR8El60TD18*************************bOp75dg0i7c+NqbBQ2tAxOAE. \
    --SequenceNumber 0 \
    --LLMConfig.LLMType openai \
    --LLMConfig.Model gpt-4o-mini \
    --LLMConfig.APIUrl https://translationsllm.openai.azure.com****************************************pletions?api-version=2025-01-01-preview \
    --LLMConfig.APIKey CKLhA70tjVXN8Tp0ADnCiv5YSqFe****************************99BJAC4f1cMXJ3w3AAABACOG9t8q \
    --LLMConfig.SystemPrompt 你是一个简洁的对话助手。 \
    --LLMConfig.MaxTokens 2048 \
    --LLMConfig.MaxHistory 50 \
    --LLMConfig.MaxToolRound 20 \
    --LLMConfig.Timeout 20000 \
    --LLMConfig.Temperature 0.5 \
    --LLMConfig.TopP 0.9 \
    --LLMConfig.McpServer.Name weather-mcp \
    --LLMConfig.McpServer.Url https://m*********e.com/v1 \
    --LLMConfig.McpServer.Timeout 5000 \
    --LLMConfig.McpServer.ToolList get_weather \
    --DialogConfig.InterruptMode 2 \
    --DialogConfig.InterruptKeywords 停止
```

Output: 
```
{
    "Response": {
        "TaskId": "-nG0jIFU7llEfJ3MR8El60TD18*************************bOp75dg0i7c+NqbBQ2tAxOAE.",
        "RequestId": "0842be45-1e51-401a-8372-f57f6c86edb9"
    }
}
```


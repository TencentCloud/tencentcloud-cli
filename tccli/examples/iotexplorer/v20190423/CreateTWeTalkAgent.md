**Example 1: 创建智能体**



Input: 

```
tccli iotexplorer CreateTWeTalkAgent --cli-unfold-argument  \
    --STTConfig.Type trtc \
    --STTConfig.TRTC.Language zh \
    --STTConfig.TRTC.VADSilenceTime 300 \
    --STTConfig.TRTC.VADLevel 3 \
    --LLMConfig.Type default \
    --LLMConfig.SystemPrompt 你是一个暖男，照顾用户情绪 \
    --TTSConfig.Type flow \
    --TTSConfig.Flow.VoiceId v-male-P6q7LzD8 \
    --TTSConfig.Flow.Speed 1 \
    --Name 小伙伴 \
    --InstanceId ins-31ooyYQG4ym \
    --Description 智能助理 \
    --ConversationConfig.WelcomeMessage 你好，很高兴见到你 \
    --ConversationConfig.WelcomeMessagePriority 1 \
    --ConversationConfig.InterruptMode 0 \
    --MemoryConfig.Enabled False \
    --Metadata {"a": 123}
```

Output: 
```
{
    "Response": {
        "AgentId": "agent-StCcdhLC4m",
        "RequestId": "ee01d12f-0e2c-437e-97a8-321b1cd6d141"
    }
}
```


**Example 1: 修改智能体**



Input: 

```
tccli iotexplorer ModifyTWeTalkAgent --cli-unfold-argument  \
    --AgentId agent-SValZ1qdEm \
    --Name 学弟 \
    --Description 暖男 \
    --STTConfig.Type trtc \
    --STTConfig.TRTC.Language en \
    --STTConfig.TRTC.VADSilenceTime 300 \
    --STTConfig.TRTC.VADLevel 3 \
    --LLMConfig.Type default \
    --LLMConfig.SystemPrompt 你是一个暖男，照顾用户情绪 \
    --LLMConfig.Temperature 1 \
    --LLMConfig.History 20 \
    --TTSConfig.Type flow \
    --TTSConfig.Flow.VoiceId v-male-P6q7LzD8 \
    --TTSConfig.Flow.Speed 1
```

Output: 
```
{
    "Response": {
        "RequestId": "357c4fb4-6ddb-462d-aed4-4e78a34b1ac8"
    }
}
```


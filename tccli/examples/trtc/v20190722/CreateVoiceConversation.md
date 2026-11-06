**Example 1: 开始对话任务（三段式）**



Input: 

```
tccli trtc CreateVoiceConversation --cli-unfold-argument  \
    --SdkAppId 1400000311 \
    --RoomId 99884336 \
    --RoomIdType 0 \
    --AgentConfig.UserId test2 \
    --AgentConfig.UserSig eJyrVgrxCdYrzkxXslJQyvEsqDTzcyrzyHGNcgoMKsuudEt2D3D1KUwsi8jy8PD3NQnK********************************************************************cmWpRSDrjPQMYKaUZOaCzTA3MzYwMDI2NYOKZ6ak5pVkpmVCNJSkFpcYKdUCAKlEMxg_ \
    --AgentConfig.TargetUserId Jeff \
    --AgentConfig.TTSPushRoomParams.UserId tts-bot-001 \
    --AgentConfig.MaxIdleTime 5000 \
    --AgentConfig.FilterBracketsContent 1 \
    --AgentConfig.SubtitleMode 0 \
    --AgentConfig.TurnDetectionMode auto \
    --ConversationMode Cascade \
    --STTConfig.Provider trtc \
    --STTConfig.Params {"engine_model_type":"bigmodel", "max_speak_time":"60000", "language":"zh"} \
    --LLMConfig.LLMType tencent \
    --LLMConfig.Model hunyu*****0628 \
    --LLMConfig.APIUrl http://api.taiji.w*****************/chat/completions \
    --LLMConfig.APIKey n21LYT6WmpE***********mqWKCrQlzJ \
    --LLMConfig.SystemPrompt 你是一个简洁的对话助手。 \
    --LLMConfig.FailureMessage 系统繁忙请稍后再试 \
    --LLMConfig.MaxTokens 0 \
    --LLMConfig.ThinkingMode False \
    --LLMConfig.MaxHistory 50 \
    --LLMConfig.MaxToolRound 20 \
    --LLMConfig.Timeout 60000 \
    --LLMConfig.Temperature 0.5 \
    --LLMConfig.TopP 0.9 \
    --LLMConfig.McpServer.Name weath****ools \
    --LLMConfig.McpServer.Url https://m*********e.com/sse \
    --LLMConfig.McpServer.Timeout 10000 \
    --LLMConfig.McpServer.Headers.0.Key enable_search \
    --LLMConfig.McpServer.Headers.0.Value true \
    --LLMConfig.McpServer.ToolList get_****her \
    --LLMConfig.CustomHeaders.0.Key X-Request-Source \
    --LLMConfig.CustomHeaders.0.Value trtc-conversation \
    --LLMConfig.CustomFields.0.Key enable_search \
    --LLMConfig.CustomFields.0.Value true \
    --LLMConfig.HistoryMessages.0.Role user \
    --LLMConfig.HistoryMessages.0.Content 你好 \
    --TTSConfig.Provider trtc \
    --TTSConfig.Params {"model":"flow_02_turbo","voice_id":"v-female-R2s4N9qJ","speed":1.0,"volume":1.0,"pitch":0} \
    --DialogConfig.InterruptMode 2 \
    --DialogConfig.InterruptSpeechDuration 200 \
    --DialogConfig.InterruptKeywords 停止 \
    --DialogConfig.SilenceFollowUp 50 \
    --DialogConfig.SilenceFollowUpText 你还在吗？有想问的直接告诉我。 \
    --DialogConfig.WelcomeMessage 您好，我是你的ai助手，请问有什么可以帮您？ \
    --VisionConfig.Enable True \
    --VisionConfig.StorageType 0
```

Output: 
```
{
    "Response": {
        "TaskId": "-nG0jIFU7iHfG3DHVsI24YFXEn*************************bRRKvrG-CxBxuPyrGvSr2ZQE.",
        "RequestId": "45192e66-a49e-4ea4-92f0-519955e3c903"
    }
}
```

**Example 2: 开始对话任务（端到端语音大模型）**



Input: 

```
tccli trtc CreateVoiceConversation --cli-unfold-argument  \
    --SdkAppId 1400704311 \
    --RoomId 9988123 \
    --RoomIdType 0 \
    --AgentConfig.UserId test2 \
    --AgentConfig.UserSig eJyrVgrxCdYrzkxXslJQyvEsqDTzcyrzyHGNcgoMKsuudEt2D3D1KUwsi8jy8PD3NQnK********************************************************************cmWpRSDrjPQMYKaUZOaCzTA3MzYwMDI2NYOKZ6ak5pVkpmVCNJSkFpcYKdUCAKlEMxg_ \
    --AgentConfig.TargetUserId Jeff \
    --AgentConfig.TTSPushRoomParams.UserId tts-bot-001 \
    --AgentConfig.MaxIdleTime 50 \
    --ConversationMode S2S \
    --S2SConfig.Provider doubao \
    --S2SConfig.Params {"api_key":"xxxxxx","type":"session.create","session":{"id":"","model":"1.2.6.1","instructions":"你是一位生活小助手，擅长回答菜谱、旅游、育儿、健康、购物、法律等日常问题，请用中文简洁清晰地回答。","type":"realtime","audio":{"input":{"format":{"type":"pcm","rate":16000}},"output":{"format":{"type":"pcm_s16le","rate":24000},"voice":"zh_female_vv_jupiter_bigtts"}}},"extension":{"asr":{"extra":{}},"dialog":{"bot_name":"豆包"},"tts":{"speaker":"zh_female_vv_jupiter_bigtts","audio_config":{"channel":1,"format":"pcm_s16le","sample_rate":24000}}}}
```

Output: 
```
{
    "Response": {
        "TaskId": "-nG0jIFU7g8UyQOwf8uvyfe1ph*************************bAp-C8HdhuD+Acd+5Tavn6AE.",
        "RequestId": "32151e30-fd9f-47d4-b59d-72a372eb61f0"
    }
}
```


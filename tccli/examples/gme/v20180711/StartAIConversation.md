**Example 1: 启动一个AI机器人对话**



Input: 

```
tccli gme StartAIConversation --cli-unfold-argument  \
    --SdkAppId 12345678 \
    --RoomId room_987654321 \
    --AgentConfig.UserId user_12345 \
    --AgentConfig.UserSig user_signature_example \
    --AgentConfig.MaxIdleTime 120 \
    --AgentConfig.TargetUserId target_user_54321 \
    --STTConfig.Language zh \
    --LLMConfig {"LLMType": "openai", "Model": "gpt-3.5-turbo", "APIKey": "xxx", "APIUrl": "http://xxxx-api.xxxx.com/v1/chat/completions", "Streaming": true} \
    --TTSConfig {"TTSType": "tencent", "AppId": 130000000, "SecretId": "AKIDxxxxx", "SecretKey": "HlDxxxxxx", "VoiceType": 1008, "Speed": 1}
```

Output: 
```
{
    "Response": {
        "TaskId": "v2_20250224_udqgoOzzpAFOoiXR_sHbeVCwys3hy0PLs1uRLvS7wY9mjZMEIQuDPhT",
        "RequestId": "df81f274-c1b8-4342-b0a1-e552072cc48e"
    }
}
```


**Example 1: 中途合成出错**

注意sse接口需要使用trtc.ai.tencentcloudapi.com域名，否则会调用接口失败

Input: 

```
tccli trtc TextToSpeechSSE --cli-unfold-argument  \
    --Text 你好呀 \
    --SdkAppId 14600000000 \
    --Voice.VoiceId v-female-R2s4N9qJ \
    --AlignmentMode 1
```

Output: 
```
data: {"Type": "chunk", "RequestId": "456e7890-e12b-34d5-a678-426614174000", "ChunkId": "chunk_0", "Audio": "base64编码的音频数据...", "Seq": 0, "IsEnd": false}

data: {"Type": "error", "RequestId": "456e7890-e12b-34d5-a678-426614174000", "Error": {"Code": "InternalError", "Message": "internal error message"}}
```

**Example 2: 流式语音合成**

注意sse接口需要使用trtc.ai.tencentcloudapi.com域名，否则会调用接口失败

Input: 

```
tccli trtc TextToSpeechSSE --cli-unfold-argument  \
    --Text 你好呀 \
    --SdkAppId 14600000000 \
    --Voice.VoiceId v-female-R2s4N9qJ \
    --AlignmentMode 1
```

Output: 
```
data: {"Type": "chunk", "RequestId": "456e7890-e12b-34d5-a678-426614174000", "ChunkId": "chunk_0", "Audio": "base64编码的音频数据...", "Seq": 0, "IsEnd": false}

data: {"Type": "chunk", "RequestId": "456e7890-e12b-34d5-a678-426614174000", "ChunkId": "chunk_1", "Audio": "base64编码的音频数据...", "Seq": 1, "Alignments": [{"TimeBeginMs": 0, "TimeEndMs": 600, "TextBegin": 0, "TextEnd": 2}, "IsEnd": false}

data: {"Type": "chunk", "RequestId": "456e7890-e12b-34d5-a678-426614174000", "ChunkId": "chunk_2", "Audio": "base64编码的音频数据...", "Seq": 2, "IsEnd": true}
```


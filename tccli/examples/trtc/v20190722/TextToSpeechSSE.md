**Example 1: 启动一个SSE流式语音合成**

启动一个SSE流式语音合成，注意在解析时，音频的Type为chunk，其他的Type 非音频

Input: 

```
tccli trtc TextToSpeechSSE --cli-unfold-argument  \
    --Text 你好呀 \
    --SdkAppId 14600000000 \
    --Voice.VoiceId 256
```

Output: 
```
data: {"Type": "chunk", "RequestId": "456e7890-e12b-34d5-a678-426614174000", "ChunkId": "chunk_0", "Audio": "base64编码的音频数据...", "Seq": 0, "IsEnd": false}

data: {"Type": "chunk", "RequestId": "456e7890-e12b-34d5-a678-426614174000", "ChunkId": "chunk_1", "Audio": "base64编码的音频数据...", "Seq": 1, "IsEnd": false}

data: {"Type": "chunk", "RequestId": "456e7890-e12b-34d5-a678-426614174000", "ChunkId": "chunk_2", "Audio": "base64编码的音频数据...", "Seq": 2, "IsEnd": true}
```


**Example 1: 中途合成出错**

在合成过程中，如果出现错误，会返回sse格式的错误

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

**Example 2: 合成前出错**

在正式进行合成前，如果有参数错误，会直接返回一个json错误，可以通过content type来判断这种情况

Input: 

```
tccli trtc TextToSpeechSSE --cli-unfold-argument  \
    --Text 你好呀 \
    --SdkAppId 14600000000 \
    --Voice.VoiceId fake \
    --AlignmentMode 1
```

Output: 
```
{
    "Response": {
        "RequestId": "78033210-b9c2-4c2a-b378-6a0c63646d81",
        "Error": {
            "Code": "InvalidParameter.VoiceId",
            "Message": "Cloud API TTS parameter error: Voice ID 'fake' not found. Please check if the voice exists or create it via voice clone API."
        }
    }
}
```

**Example 3: 流式语音合成**

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


**Example 1: 更新tts音色**

在对话过程中，想要动态更新tts的音色

Input: 

```
tccli trtc UpdateAIConversation --cli-unfold-argument  \
    --TaskId your-taskid \
    --TTSConfig your-tts-config-json
```

Output: 
```
{
    "Response": {
        "RequestId": "df81f274-c1b8-4342-b0a1-e552072cc48e"
    }
}
```


**Example 1: API调用**



Input: 

```
tccli aai TextToVoice --cli-unfold-argument  \
    --Text 你好 \
    --SessionId session-1234 \
    --Volume 1 \
    --Speed 1 \
    --ProjectId 0 \
    --ModelType 1 \
    --PrimaryLanguage 1 \
    --SampleRate 16000 \
    --Codec wav
```

Output: 
```
{
    "Response": {
        "Audio": "UklGRlR/AABXQVZFZm10IBAAAAABAAEAgD4AAAB9AAACABAAZGF0YSx9AAD+////AQD//wAAAAAAAAIAAQADAAMABgAEAAYABQAGAAUABwAIAAgACQAAE......AAgACAAEAAgADAAIAAwACAAQAAwACAAIAAgADAAMAAgACAAIAAwABAAAAAAAAAAAAAAD/////AAAAAAAA//8AAP///v/9//7//v///////v8AAP///////wAA/////wAA/////wAAAAAAAAAAAAAAAAAAAAAAAAAA",
        "RequestId": "9a7a1615-3e09-4db2-8032-5c6f497f7e6a",
        "SessionId": "session-1234"
    }
}
```


**Example 1: 录音识别请求**



Input: 

```
tccli asr CreateRecTask --cli-unfold-argument  \
    --EngineModelType 16k_zh_en \
    --ChannelNum 1 \
    --ResTextFormat 0 \
    --SourceType 0 \
    --Url https://audio.wav
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": 1000000286
        },
        "RequestId": "b6b0e328-d84d-866507b97435"
    }
}
```


**Example 1: 关联字幕**



Input: 

```
tccli vod AttachMediaSubtitles --cli-unfold-argument  \
    --FileId 123 \
    --AdaptiveDynamicStreamingDefinition 10000 \
    --Operation Attach \
    --SubtitleIds subtitle1 subtitle2
```

Output: 
```
{
    "Response": {
        "RequestId": "requestId"
    }
}
```


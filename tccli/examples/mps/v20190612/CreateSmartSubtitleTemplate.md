**Example 1: 创建智能字幕模板**



Input: 

```
tccli mps CreateSmartSubtitleTemplate --cli-unfold-argument  \
    --Name 智能字幕模板测试 \
    --VideoSrcLanguage zh \
    --SubtitleType 2 \
    --SubtitleFormat vtt \
    --TranslateSwitch ON \
    --TranslateDstLanguage en/ja \
    --SubtitleEmbedId 0
```

Output: 
```
{
    "Response": {
        "Definition": 304479,
        "RequestId": "92b23ad2-452e-4887-927e-7b4cc9325538"
    }
}
```


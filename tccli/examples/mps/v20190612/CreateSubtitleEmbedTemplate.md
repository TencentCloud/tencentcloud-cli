**Example 1: 创建字幕压制模板**



Input: 

```
tccli mps CreateSubtitleEmbedTemplate --cli-unfold-argument  \
    --Name 字幕压制模板 \
    --SubtitleEmbedConfig.FontType kai \
    --SubtitleEmbedConfig.FontSize 50 \
    --SubtitleEmbedConfig.FontSizeUnit 0
```

Output: 
```
{
    "Response": {
        "Definition": 260513,
        "RequestId": "3fceb699-e7de-4e17-8f6f-48976bf04c9e"
    }
}
```


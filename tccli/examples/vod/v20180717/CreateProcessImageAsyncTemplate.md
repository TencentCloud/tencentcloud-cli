**Example 1: 创建高级超分模板**



Input: 

```
tccli vod CreateProcessImageAsyncTemplate --cli-unfold-argument  \
    --ProcessImageConfigure.EncodeConfig.Format PNG \
    --ProcessImageConfigure.EnhanceConfig.AdvancedSuperResolution.Switch ON \
    --ProcessImageConfigure.EnhanceConfig.AdvancedSuperResolution.Type super \
    --ProcessImageConfigure.EnhanceConfig.AdvancedSuperResolution.Mode fixed \
    --ProcessImageConfigure.EnhanceConfig.AdvancedSuperResolution.Width 1920 \
    --ProcessImageConfigure.EnhanceConfig.AdvancedSuperResolution.Height 1080
```

Output: 
```
{
    "Response": {
        "Definition": 30023,
        "RequestId": "e35641c1-4b92-49e8-9786-06d20161b5d7"
    }
}
```


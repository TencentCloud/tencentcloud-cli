**Example 1: 修改模板配置**



Input: 

```
tccli vod ModifyProcessImageAsyncTemplate --cli-unfold-argument  \
    --Definition 7 \
    --SubAppId 221073 \
    --Name test3 \
    --Comment testcomment \
    --ProcessImageConfigure.EncodeConfig.Format JPEG \
    --ProcessImageConfigure.EncodeConfig.Quality 100 \
    --ProcessImageConfigure.EnhanceConfig.SuperResolution.Switch ON \
    --ProcessImageConfigure.EnhanceConfig.SuperResolution.Type lq \
    --ProcessImageConfigure.EnhanceConfig.SuperResolution.Size 2 \
    --ProcessImageConfigure.EnhanceConfig.Denoise.Switch ON \
    --ProcessImageConfigure.EnhanceConfig.Denoise.Type weak \
    --ProcessImageConfigure.EnhanceConfig.ImageQualityEnhance.Switch ON \
    --ProcessImageConfigure.EnhanceConfig.ImageQualityEnhance.Type weak \
    --ProcessImageConfigure.EnhanceConfig.ColorEnhance.Switch ON \
    --ProcessImageConfigure.EnhanceConfig.ColorEnhance.Type weak \
    --ProcessImageConfigure.EnhanceConfig.SharpEnhance.Switch ON \
    --ProcessImageConfigure.EnhanceConfig.SharpEnhance.Intensity 1 \
    --ProcessImageConfigure.EnhanceConfig.FaceEnhance.Switch ON \
    --ProcessImageConfigure.EnhanceConfig.FaceEnhance.Intensity 1 \
    --ProcessImageConfigure.EnhanceConfig.LowLightEnhance.Switch ON \
    --ProcessImageConfigure.EnhanceConfig.LowLightEnhance.Type normal
```

Output: 
```
{
    "Response": {
        "RequestId": "108471cb-3414-4309-ac74-24443116ddda"
    }
}
```


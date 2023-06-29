**Example 1: 选脸融合**



Input: 

```
tccli facefusion FuseFace --cli-unfold-argument  \
    --LogoParam.LogoRect.Y 0 \
    --LogoParam.LogoRect.X 0 \
    --LogoParam.LogoRect.Height 0 \
    --LogoParam.LogoRect.Width 0 \
    --LogoParam.LogoUrl test1.jpg \
    --ProjectId at_1603326187690926080 \
    --LogoAdd 1 \
    --RspImgType url \
    --MergeInfos.0.Url test.jpg \
    --MergeInfos.0.TemplateFaceID mt_1603586676924403712_1 \
    --ModelId mt_1603586676924403712
```

Output: 
```
{
    "Response": {
        "FusedImage": "result.jpg",
        "RequestId": "1a2e88a4-3614-48a0-96b9-d09bf6de2fe4"
    }
}
```


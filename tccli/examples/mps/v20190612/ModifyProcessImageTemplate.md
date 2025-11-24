**Example 1: 修改图片处理模板**

修改图片处理模板

Input: 

```
tccli mps ModifyProcessImageTemplate --cli-unfold-argument  \
    --Definition 200043 \
    --Name Template100 \
    --Comment ProcessImageTemplate100 \
    --ProcessImageTemplate.EncodeConfig.Format jpeg \
    --ProcessImageTemplate.EncodeConfig.Quality 50 \
    --ProcessImageTemplate.EnhanceConfig.SuperResolution.Switch OFF
```

Output: 
```
{
    "Response": {
        "RequestId": "7c43b64a-8f21-4c2e-ab6e-a490ee5c439d"
    }
}
```


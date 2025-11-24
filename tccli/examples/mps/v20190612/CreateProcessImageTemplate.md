**Example 1: 创建图片处理模板**

创建图片处理模板

Input: 

```
tccli mps CreateProcessImageTemplate --cli-unfold-argument  \
    --Name Template1 \
    --Comment ProcessImageTemplate \
    --ProcessImageTemplate.EncodeConfig.Format jpeg \
    --ProcessImageTemplate.EncodeConfig.Quality 75 \
    --ProcessImageTemplate.EnhanceConfig.SuperResolution.Switch ON
```

Output: 
```
{
    "Response": {
        "RequestId": "03b25aab-8883-497e-838f-d760c3e220f6",
        "Definition": 200043
    }
}
```


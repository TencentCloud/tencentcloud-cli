**Example 1: 多视角图生 3D**



Input: 

```
tccli mps SubmitHunyuan3DTask --cli-unfold-argument  \
    --MultiViewImages.0.ViewType front \
    --MultiViewImages.0.ViewImageUrl https://hunyuan-base-test-1258344703.cos.ap-guangzhou.myqcloud.com/public/test/eba3542f-5e19-4862-b95d-c2d28e7ef91e-latent.png \
    --EnablePBR True
```

Output: 
```
{
    "Response": {
        "TaskId": "r_fbdac9ac98c311f18af6166e9d240373",
        "RequestId": "1a15321e-f92f-404e-8ccc-8b33d5359f14"
    }
}
```


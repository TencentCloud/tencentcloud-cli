**Example 1: 请求示例**



Input: 

```
tccli mps CreateAigcVideoTask --cli-unfold-argument  \
    --ModelName veo \
    --Prompt move the picture \
    --NegativePrompt Top lighting,bright colors \
    --EnhancePrompt False \
    --ImageUrl https://1500039689.vod-xxx.com/6cd2c44bvodcq1500039689/179cafb25145403699605999621/CxxoxE6jcA.png \
    --LastImageUrl https://aigc-xx-image-1303333058.cos.ap-guangzhou.myqcloud.com/xxx_8655.png \
    --Duration 8 \
    --ExtraParameters.Resolution 720*1280 \
    --ExtraParameters.AspectRatio 16:9 \
    --StoreCosParam.CosBucketName aigc-test-video-1303333058 \
    --StoreCosParam.CosBucketRegion ap-guangzhou \
    --StoreCosParam.CosBucketPath my_cos_file \
    --Operator admin
```

Output: 
```
{
    "Response": {
        "TaskId": "2147483792",
        "RequestId": "643fb583-0032-44ac-bfa8-bef25e310998"
    }
}
```


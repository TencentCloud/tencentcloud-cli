**Example 1: 设置 DRM 密钥提供商信息**



Input: 

```
tccli vod SetDrmKeyProviderInfo --cli-unfold-argument  \
    --SDMCInfo.SecretKey testKey \
    --SDMCInfo.SecretId testId \
    --SDMCInfo.Uid 123 \
    --SDMCInfo.FairPlayCertificateUrl https://xx/fairplay.cer
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3"
    }
}
```


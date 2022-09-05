**Example 1: 查询 DRM 密钥提供商信息**



Input: 

```
tccli vod DescribeDrmKeyProviderInfo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "12ae8d8e-dce3-4151-9d4b-4594145287e1",
        "SDMCInfo": {
            "Uid": "123",
            "SecretId": "testId",
            "SecretKey": "testKey",
            "FairPlayCertificateUrl": "https://xx/fairplay.cer"
        }
    }
}
```


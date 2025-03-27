**Example 1: CreateModelVersionRegister**

创建模型

Input: 

```
tccli afc CreateModelVersionRegister --cli-unfold-argument  \
    --BusinessSecurityData.ModelName mstest2_xyxj_dezg20241010_model_0325_000169830 \
    --BusinessSecurityData.Description mstest2-1309242001】-【mstest2_xyxj_dezg20241010_model_0325_000169830】_mstest2_xyxj_dezg20241010_model_0325_000169830_vignyshen_模型平台 \
    --BusinessSecurityData.MissingValue 123 \
    --BusinessSecurityData.DoubleFeatures s2434 \
    --BusinessSecurityData.RequiredFeaturesWeight 1 \
    --BusinessSecurityData.ModelFound 1 \
    --BusinessSecurityData.StringFeatures s6534 \
    --BusinessSecurityData.ModelType 0 \
    --BusinessSecurityData.RequiredFeatures s6555 \
    --BusinessSecurityData.ModelPassThrough 1 \
    --BusinessSecurityData.FailedThreshold 10 \
    --BusinessSecurityData.PackageTag HJ2DMAU2 \
    --BusinessSecurityData.Backups 1 \
    --BusinessSecurityData.Backup 1 \
    --BusinessSecurityData.FullUrl https://finance-model-1300429106.cos.ap-guangzhou.myqcloud.com/HJ2DMAU2/2/mstest2_xyxj_dezg20241010_model_0325_000169830.zip
```

Output: 
```
{
    "Response": {
        "Data": {
            "Code": 0,
            "Message": "OK",
            "Value": "0"
        },
        "RequestId": "7796f52d-f5ca-42d4-b52c-82c2dd50bb7f"
    }
}
```


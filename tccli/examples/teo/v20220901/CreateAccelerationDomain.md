**Example 1: 创建加速域名**

创建加速域名

Input: 

```
tccli teo CreateAccelerationDomain --cli-unfold-argument  \
    --DomainName qq.com \
    --ZoneId zone-225qgrnvbi9w \
    --OriginInfo.OriginType ip_domain \
    --OriginInfo.Origin qq.com \
    --OriginInfo.BackupOrigin 
```

Output: 
```
{
    "Response": {
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a707"
    }
}
```

**Example 2: 创建AWS signature v2鉴权类型的加速域名**

创建源站类型为S3兼容，鉴权版本为AWS signature v2的加速域名

Input: 

```
tccli teo CreateAccelerationDomain --cli-unfold-argument  \
    --DomainName qq.com \
    --ZoneId zone-225qgrnvbi9w \
    --OriginInfo.OriginType AWS_S3 \
    --OriginInfo.Origin https://teo.cos.ap-beijing.myqcloud.com \
    --OriginInfo.PrivateParameters.0.Name AccessKeyId \
    --OriginInfo.PrivateParameters.0.Value AKIDdDva7VjFk7LQJ0X5WnbKE7mQTest \
    --OriginInfo.PrivateParameters.1.Name SecretAccessKey \
    --OriginInfo.PrivateParameters.1.Value nMirpdWhhT6bxPsaFwYM1SzQrTest \
    --OriginInfo.PrivateParameters.2.Name SignatureVersion \
    --OriginInfo.PrivateParameters.2.Value v2 \
    --OriginInfo.PrivateParameters.3.Name Region \
    --OriginInfo.PrivateParameters.3.Value ap-beijing
```

Output: 
```
{
    "Response": {
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a703"
    }
}
```


**Example 1: 创建源站类型为 AWS S3 的加速域名**

创建源站类型为 AWS S3，开启私有访问，鉴权算法版本为 AWS signature v2 的加速域名。

Input: 

```
tccli teo CreateAccelerationDomain --cli-unfold-argument  \
    --ZoneId zone-225qgrnvbi9w \
    --DomainName qq.com \
    --OriginInfo.OriginType AWS_S3 \
    --OriginInfo.Origin https://test.s3.ap-east-1.amazonaws.com \
    --OriginInfo.PrivateAccess on \
    --OriginInfo.PrivateParameters.0.Name AccessKeyId \
    --OriginInfo.PrivateParameters.0.Value AKIDdDva7VjFk7LQJ0X5WnbKE7mQTest \
    --OriginInfo.PrivateParameters.1.Name SecretAccessKey \
    --OriginInfo.PrivateParameters.1.Value nMirpdWhhT6bxPsaFwYM1SzQrTest \
    --OriginInfo.PrivateParameters.2.Name SignatureVersion \
    --OriginInfo.PrivateParameters.2.Value v2 \
    --OriginInfo.PrivateParameters.3.Name Region \
    --OriginInfo.PrivateParameters.3.Value ap-east-1
```

Output: 
```
{
    "Response": {
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a703"
    }
}
```

**Example 2: 创建源站类型为域名的加速域名**

创建源站类型为域名的加速域名。

Input: 

```
tccli teo CreateAccelerationDomain --cli-unfold-argument  \
    --ZoneId zone-225qgrnvbi9w \
    --DomainName qq.com \
    --OriginInfo.OriginType ip_domain \
    --OriginInfo.Origin www.test.com
```

Output: 
```
{
    "Response": {
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a707"
    }
}
```


**Example 1: 创建使用共享 CNAME 的加速域名**

创建加速域名并使用指定的共享 CNAME。

Input: 

```
tccli teo CreateAccelerationDomain --cli-unfold-argument  \
    --ZoneId zone-225qgrnvbi9w \
    --DomainName www.example.com \
    --OriginInfo.OriginType ip_domain \
    --OriginInfo.Origin 1.1.1.1 \
    --OriginProtocol FOLLOW \
    --HttpOriginPort 80 \
    --HttpsOriginPort 443 \
    --IPv6Status follow
```

Output: 
```
{
    "Response": {
        "OwnershipVerification": null,
        "RequestId": "3d310306-f298-439a-9daa-29eec8490769"
    }
}
```

**Example 2: 创建源站类型为 AWS S3 的加速域名**

创建源站类型为 AWS S3，开启私有访问，鉴权算法版本为 AWS signature v2 的加速域名。

Input: 

```
tccli teo CreateAccelerationDomain --cli-unfold-argument  \
    --ZoneId zone-225qgrnvbi9w \
    --DomainName qq.com \
    --OriginInfo.OriginType AWS_S3 \
    --OriginInfo.Origin test.s3.ap-east-1.amazonaws.com \
    --OriginInfo.PrivateAccess on \
    --OriginInfo.PrivateParameters.0.Name AccessKeyId \
    --OriginInfo.PrivateParameters.0.Value nMirpdWhhT6bxPsaFwYM1SzQrTest \
    --OriginInfo.PrivateParameters.1.Name SecretAccessKey \
    --OriginInfo.PrivateParameters.1.Value AKID*********************************************** \
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

**Example 3: 创建源站类型为云点播的加速域名，回源范围：all**

创建源站类型为云点播的加速域名，并指定回源范围为当前源站对应的 VOD应用内所有文件。

Input: 

```
tccli teo CreateAccelerationDomain --cli-unfold-argument  \
    --ZoneId zone-36oiczk333c3 \
    --DomainName vbt-06.bennyddeng.work \
    --OriginInfo.OriginType VOD \
    --OriginInfo.Origin 220643 \
    --OriginInfo.VodOriginScope all
```

Output: 
```
{
    "Response": {
        "OwnershipVerification": null,
        "RequestId": "ec58b4d5-9154-4fd8-a148-7b39af634f2b"
    }
}
```

**Example 4: 创建源站类型为云点播的加速域名，回源范围：bucket**

创建源站类型为云点播的加速域名，并指定回源范围为当前源站对应的 VOD 应用下某一个存储桶内的文件。

Input: 

```
tccli teo CreateAccelerationDomain --cli-unfold-argument  \
    --ZoneId zone-36oiczk333c3 \
    --DomainName vbt-05.bennyddeng.work \
    --OriginInfo.OriginType VOD \
    --OriginInfo.Origin 220643 \
    --OriginInfo.VodOriginScope bucket \
    --OriginInfo.VodBucketId 9n15dnlrwu800zh
```

Output: 
```
{
    "Response": {
        "OwnershipVerification": null,
        "RequestId": "8e26894c-e6f5-43ae-be0e-ef2377b88ea6"
    }
}
```

**Example 5: 创建源站类型为域名的加速域名**

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


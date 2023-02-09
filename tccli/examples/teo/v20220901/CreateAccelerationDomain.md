**Example 1: 创建加速域名**



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


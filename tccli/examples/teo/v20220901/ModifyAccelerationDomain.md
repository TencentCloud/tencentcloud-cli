**Example 1: 修改加速域名信息**

POST / HTTP/1.1
Host: teo.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: ModifyAccelerationDomains
<公共请求参数>

{
    "DomainName":"qq.com",
    "ZoneId":"zone-225qgrnvbi9w",
    "OriginInfo":{
        "OriginType":"ip_domain",
        "Origin":"qq.com"
    }
}

Input: 

```
tccli teo ModifyAccelerationDomain --cli-unfold-argument  \
    --DomainName example.com \
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


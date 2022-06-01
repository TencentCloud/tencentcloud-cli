**Example 1: 修改域名证书配置**



Input: 

```
tccli teo ModifyHostsCertificate --cli-unfold-argument  \
    --ZoneId zone-xxxx \
    --Hosts xxx.test.com \
    --CertInfo.0.CertId EO-xxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```


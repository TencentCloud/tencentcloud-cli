**Example 1: 修改域名证书配置**



Input: 

```
tccli teo ModifyHostsCertificate --cli-unfold-argument  \
    --ZoneId zone-asdfasc \
    --Hosts xxx.test.com \
    --ServerCertInfo.0.CertId EO-sddafcasf
```

Output: 
```
{
    "Response": {
        "RequestId": "084d5612-67a7-4aca-aac9-827aa3662b2d"
    }
}
```


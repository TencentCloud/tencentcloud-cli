**Example 1: 配置 SSL 证书**

针对站点（ZoneId 为 zone-2fgd17m17xw）下的域名（abc.test.com）配置 SSL 证书（CertId 为 J2JqATrt）。

Input: 

```
tccli teo ModifyHostsCertificate --cli-unfold-argument  \
    --ZoneId zone-2fgd17m17xw \
    --Hosts abc.test.com \
    --Mode sslcert \
    --ServerCertInfo.0.CertId J2JqATrt
```

Output: 
```
{
    "Response": {
        "RequestId": "5e5a0d0f-52f3-4bad-9bd3-dcf1d5c954e7"
    }
}
```

**Example 2: 配置免费证书**

针对站点（ZoneId 为 zone-2fgd17m17xw）下的域名（abc.test.com）配置免费证书。

Input: 

```
tccli teo ModifyHostsCertificate --cli-unfold-argument  \
    --ZoneId zone-2fgd17m17xw \
    --Hosts abc.test.com \
    --Mode eofreecert
```

Output: 
```
{
    "Response": {
        "RequestId": "084d5612-67a7-4aca-aac9-827aa3662b2d"
    }
}
```

**Example 3: 配置边缘双向认证**

针对站点（ZoneId 为 zone-2fgd17m17xw）下的域名（abc.test.com）配置 边缘双向认证（CertId 为 J2JqATrt）。

Input: 

```
tccli teo ModifyHostsCertificate --cli-unfold-argument  \
    --ZoneId zone-2fgd17m17xw \
    --Hosts abc.test.com \
    --ClientCertInfo.Switch on \
    --ClientCertInfo.CertInfos.0.CertId J2JqATrt
```

Output: 
```
{
    "Response": {
        "RequestId": "5e5a0d0f-52f3-4bad-9bd3-dcf1d5c954e7"
    }
}
```


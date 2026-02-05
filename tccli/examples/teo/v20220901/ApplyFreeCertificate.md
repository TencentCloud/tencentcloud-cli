**Example 1: 使用 HTTP 访问文件验证方式申请免费证书**

站点（ZoneId 为 zone-2fgd17m17xw）下的域名（abc.test.com）使用 HTTP 访问文件验证方式申请免费证书。

Input: 

```
tccli teo ApplyFreeCertificate --cli-unfold-argument  \
    --ZoneId zone-2fgd17m17xw \
    --Domain abc.test.com \
    --VerificationMethod http_challenge
```

Output: 
```
{
    "Response": {
        "RequestId": "064a8c04-2d3e-4c9d-9473-39a8f76276ea",
        "FileVerification": {
            "Content": "9i8vhsvt9y8y3sx1s2d",
            "Path": "/.well-known/teo-verification/yvnu7sesms"
        }
    }
}
```

**Example 2: 使用 DNS 委派验证方式申请免费证书**

站点（ZoneId 为 zone-2fgd17m17xw）下的域名（qwe.test.com） 使用 DNS 委派验证方式申请免费证书。

Input: 

```
tccli teo ApplyFreeCertificate --cli-unfold-argument  \
    --ZoneId zone-2fgd17m17xw \
    --Domain qwe.test.com \
    --VerificationMethod dns_challenge
```

Output: 
```
{
    "Response": {
        "RequestId": "064a8c04-2d3e-4c9d-9473-39a8f76276ea",
        "DnsVerification": {
            "RecordType": "CNAME",
            "RecordValue": "_acme-challenge",
            "Subdomain": "www.example.com.edgeone.com"
        }
    }
}
```


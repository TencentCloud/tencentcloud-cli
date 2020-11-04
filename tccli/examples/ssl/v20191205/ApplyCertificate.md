**Example 1: 免费证书申请**



Input: 

```
tccli ssl ApplyCertificate --cli-unfold-argument  \
    --DomainName wgc.red\
    --DvAuthMethod DNS_AUTO
```

Output: 
```
{
    "Response": {
        "CertificateId": "a9TsmZkL",
        "RequestId": "0b39eaa4-f938-476d-9b26-19fb07b80936"
    }
}
```


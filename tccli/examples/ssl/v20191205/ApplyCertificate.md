**Example 1: 免费证书申请**

免费证书申请

Input: 

```
tccli ssl ApplyCertificate --cli-unfold-argument  \
    --DvAuthMethod DNS_AUTO \
    --DomainName wgc.red
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


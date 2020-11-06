**Example 1: 创建证书**

购买付费证书

Input: 

```
tccli ssl CreateCertificate --cli-unfold-argument  \
    --ProductId 25 \
    --DomainNum 1 \
    --TimeSpan 1
```

Output: 
```
{
    "Response": {
        "CertificateIds": [
            "gf16kv3A"
        ],
        "DealIds": [
            "20200923877000003022941"
        ],
        "RequestId": "5a3d8310-3d7e-42d3-923a-b81407fe495e"
    }
}
```


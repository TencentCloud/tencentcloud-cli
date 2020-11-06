**Example 1: Reissuing a certificate**



Input: 

```
tccli ssl ReplaceCertificate --cli-unfold-argument  \
    --CertificateId a91hoLqi \
    --ValidType DNS
```

Output: 
```
{
    "Response": {
        "CertificateId": "a91hoLqo",
        "RequestId": "91afa3b6-5b67-43e1-b312-9d3b9bf0f410"
    }
}
```


**Example 1: 修改证书所属项目**



Input: 

```
tccli ssl ModifyCertificateProject --cli-unfold-argument  \
    --CertificateIdList 8ea2a8ee 4084da1d e45e529f \
    --ProjectId 673782
```

Output: 
```
{
    "Response": {
        "FailCertificates": [],
        "SuccessCertificates": [
            "8ea2a8ee",
            "4084da1d",
            "e45e529f"
        ],
        "RequestId": "95adbcc1-a0bb-4b9c-acf6-5c4e514b945f"
    }
}
```


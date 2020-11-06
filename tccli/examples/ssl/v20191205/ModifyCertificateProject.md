**Example 1: 修改证书所属项目**



Input: 

```
tccli ssl ModifyCertificateProject --cli-unfold-argument  \
    --CertificateIdList ABCD1234 ABCD1235 ABCD1236 \
    --ProjectId 12345
```

Output: 
```
{
    "Response": {
        "FailCertificates": [],
        "SuccessCertificates": [
            "ABCD1234",
            "ABCD1235",
            "ABCD1236"
        ],
        "RequestId": "95adbcc1-a0bb-4b9c-acf6-5c4e514b945f"
    }
}
```


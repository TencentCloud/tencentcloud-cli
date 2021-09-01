**Example 1: 添加证书**



Input: 

```
tccli live CreateLiveCert --cli-unfold-argument  \
    --CertType 0 \
    --CertName name-crt \
    --HttpsCrt XXXXX \
    --HttpsKey YYYYYY \
    --Description detail
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "CertId": 17
    }
}
```


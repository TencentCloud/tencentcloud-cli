**Example 1: 修改证书**



Input: 

```
tccli live ModifyLiveCert --cli-unfold-argument  \
    --CertId 1000 \
    --CertType 1 \
    --CertName name-crt \
    --HttpsCrt XXXXX \
    --HttpsKey YYYYYY \
    --Description detail
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```


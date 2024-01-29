**Example 1: 删除证书**



Input: 

```
tccli ssl DeleteCertificate --cli-unfold-argument  \
    --CertificateId CertificateId
```

Output: 
```
{
    "Response": {
        "DeleteResult": true,
        "RequestId": "0b39eaa4-f938-476d-9b26-19fb07b80936"
    }
}
```

**Example 2: 异步删除**



Input: 

```
tccli ssl DeleteCertificate --cli-unfold-argument  \
    --CertificateId abc \
    --IsCheckResource True
```

Output: 
```
{
    "Response": {
        "DeleteResult": false,
        "TaskId": "1251261",
        "RequestId": "abc"
    }
}
```


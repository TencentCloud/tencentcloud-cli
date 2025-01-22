**Example 1: 查询证书内容是否存在**



Input: 

```
tccli ssl CheckCertificateExist --cli-unfold-argument  \
    --CertificatePublicKey abc
```

Output: 
```
{
    "Response": {
        "RepeatCertId": "abc",
        "RequestId": "abc"
    }
}
```


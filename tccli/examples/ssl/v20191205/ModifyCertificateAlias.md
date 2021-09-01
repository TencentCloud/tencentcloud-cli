**Example 1: 修改证书备注**



Input: 

```
tccli ssl ModifyCertificateAlias --cli-unfold-argument  \
    --CertificateId abcb1234 \
    --Alias others
```

Output: 
```
{
    "Response": {
        "CertificateId": "abcb1234",
        "RequestId": "9b397ac6-7d01-4fbc-8acc-52dd6ff0877b"
    }
}
```


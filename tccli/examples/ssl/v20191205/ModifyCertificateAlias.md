**Example 1: 修改证书备注**



Input: 

```
tccli ssl ModifyCertificateAlias --cli-unfold-argument  \
    --CertificateId hehx***hshj \
    --Alias others
```

Output: 
```
{
    "Response": {
        "CertificateId": "hehx***hshj",
        "RequestId": "9b397ac6-7d01-4fbc-8acc-52dd6ff0877b"
    }
}
```


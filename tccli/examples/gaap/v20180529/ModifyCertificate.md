**Example 1: 修改域名对应的证书**



Input: 

```
tccli gaap ModifyCertificate --cli-unfold-argument  \
    --ListenerId listener-xxx\
    --Domain www.test.com\
    --CertificateId cert-12345678\
    --ClientCertificateId cert-abcdefgh
```

Output: 
```
{
    "Response": {
        "RequestId": "c7bfcad5-3f20-472f-9afc-13a66faebad8"
    }
}
```


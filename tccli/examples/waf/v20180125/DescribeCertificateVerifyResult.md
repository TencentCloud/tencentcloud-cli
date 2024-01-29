**Example 1: 获取证书校验结果**



Input: 

```
tccli waf DescribeCertificateVerifyResult --cli-unfold-argument  \
    --Domain test1.testwaf.com \
    --CertType 1 \
    --CertID D3a93
```

Output: 
```
{
    "Response": {
        "Changed": 0,
        "Detail": [
            "x509: certificate is valid for *.testwaf.com, testwaf.com, not test.qcloudwaf.com"
        ],
        "NotAfter": "2024-04-05 23:59:59",
        "RequestId": "a4824af0-ae9c-470e-b6c3-8d2a3bf89a18",
        "Status": 310
    }
}
```


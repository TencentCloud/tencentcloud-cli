**Example 1: 获取证书校验结果**



Input: 

```
tccli waf DescribeCertificateVerifyResult --cli-unfold-argument  \
    --Domain test1.qcloud.com \
    --CertType 1 \
    --CertID D3a93
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "Changed": 0,
        "Detail": [
            "xx"
        ],
        "RequestId": "xx",
        "NotAfter": "xx"
    }
}
```


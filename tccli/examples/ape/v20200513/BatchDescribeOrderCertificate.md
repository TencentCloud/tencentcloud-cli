**Example 1: 获取授权书的下载地址**



Input: 

```
tccli ape BatchDescribeOrderCertificate --cli-unfold-argument  \
    --OrderIds apod-bt0i48tz
```

Output: 
```
{
    "Response": {
        "RequestId": "s1589773775497713697",
        "CertificateUrls": [
            "http://demo.jpg"
        ]
    }
}
```


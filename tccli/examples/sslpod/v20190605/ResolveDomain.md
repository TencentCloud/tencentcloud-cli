**Example 1: 解析域名获得多个IP地址**



Input: 

```
tccli sslpod ResolveDomain --cli-unfold-argument  \
    --Domain cloud.tencent.com
```

Output: 
```
{
    "Response": {
        "Data": [
            "1.1.1.1"
        ],
        "RequestId": "a52e2d64-e2c3-44a5-9cc6-4dacd1a484b5"
    }
}
```


**Example 1: 查询SSL状态实例**



Input: 

```
tccli redis DescribeSSLStatus --cli-unfold-argument  \
    --InstanceId crs-2btr9ryn
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "FeatureSupport": false,
        "UrlExpiredTime": "xx",
        "RequestId": "xx",
        "CertDownloadUrl": "xx",
        "SSLConfig": true
    }
}
```


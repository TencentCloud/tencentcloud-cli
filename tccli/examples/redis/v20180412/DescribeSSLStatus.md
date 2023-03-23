**Example 1: 示例1**

查询实例 SSL 认证信息

Input: 

```
tccli redis DescribeSSLStatus --cli-unfold-argument  \
    --InstanceId crs-2btr9ryn
```

Output: 
```
{
    "Response": {
        "CertDownloadUrl": "abc",
        "UrlExpiredTime": "abc",
        "SSLConfig": true,
        "FeatureSupport": true,
        "Status": 0,
        "RequestId": "abc"
    }
}
```


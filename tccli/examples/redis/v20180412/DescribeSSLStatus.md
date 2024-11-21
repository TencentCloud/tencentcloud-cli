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
        "CertDownloadUrl": "https://tencentdb-user-crt-12XXXXXXX.cos.ap-nanjing.myqcloud.com/TencentDB-SSL-CA.zip",
        "FeatureSupport": true,
        "RequestId": "eda7856c-9985-4d11-b5b0-48f703XXXXXX",
        "SSLConfig": false,
        "Status": 2,
        "UrlExpiredTime": "2042-06-16 20:29:32"
    }
}
```


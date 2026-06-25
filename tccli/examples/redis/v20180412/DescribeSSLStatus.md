**Example 1: 示例**



Input: 

```
tccli redis DescribeSSLStatus --cli-unfold-argument  \
    --InstanceId crs-81zzc9hn
```

Output: 
```
{
    "Response": {
        "AddressType": -1,
        "CertDownloadUrl": "https://tencentdb-user-crt-1256375829.cos.ap-nanjing.myqcloud.com/TencentDB-SSL-CA.zip",
        "EncryptAddress": "",
        "FeatureSupport": true,
        "SSLConfig": false,
        "Status": 2,
        "UrlExpiredTime": "2042-06-16 20:29:32",
        "RequestId": "56dff940-433e-49df-b975-d97425cb6c33"
    }
}
```


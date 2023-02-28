**Example 1: 获取ipv4地理位置库下载链接**

获取ipv4地理位置库下载链接。

Input: 

```
tccli vpc DescribeIpGeolocationDatabaseUrl --cli-unfold-argument  \
    --Type ipv4
```

Output: 
```
{
    "Response": {
        "DownLoadUrl": "https://ip-address-repo-1255852779.cos.ap-guangzhou.myqcloud.com/tencent_ipv4_repo.tgz?q-sign-algorithm=sha1&q-ak=AKIDb5RbYFe5PcrwtkazVpxqX2MQIRM2xfy4&q-sign-time=1578970542;1579057002&q-key-time=1578970542;1579057002&q-header-list=&q-url-param-list=&q-signature=00f8d6ad0252822e17cca6450ebcd626eadc8405",
        "ExpiredAt": "2020-01-15T10:56:42+00:00",
        "RequestId": "21b41e67-8c0f-48cf-8af3-de0b6e1f4a4b"
    }
}
```


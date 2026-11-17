**Example 1: 实例SSL处于关闭状态**

查询结果显示实例SSL关闭，无下载链接及保护地址信息

Input: 

```
tccli postgres DescribeDBInstanceSSLConfig --cli-unfold-argument  \
    --DBInstanceId postgres-6bwgamo3
```

Output: 
```
{
    "Response": {
        "CAUrl": "",
        "ConnectAddress": "",
        "RequestId": "042e21a5-14b2-4b41-8dd4-4cf870ae10bf",
        "SSLEnabled": false
    }
}
```

**Example 2: 实例SSL处于开启云端证书状态**

查询结果显示实例SSL信息

Input: 

```
tccli postgres DescribeDBInstanceSSLConfig --cli-unfold-argument  \
    --DBInstanceId postgres-hf8jo5pr
```

Output: 
```
{
    "Response": {
        "RequestId": "25cc2555-14a2-454f-af08-6bd691315335",
        "SSLEnabled": true,
        "CAUrl": "http://testdownload.url",
        "ConnectAddress": "10.0.0.4"
    }
}
```

**Example 3: 实例SSL处于开启自定义证书状态**

查询结果显示实例SSL信息

Input: 

```
tccli postgres DescribeDBInstanceSSLConfig --cli-unfold-argument  \
    --DBInstanceId postgres-26abphtv
```

Output: 
```
{
    "Response": {
        "CAUrl": "https://testdownload.url",
        "ConnectAddress": "10.0.0.4",
        "RequestId": "903ad55a-257f-41fa-923c-649e5e7ac6ce",
        "SSLEnabled": true
    }
}
```


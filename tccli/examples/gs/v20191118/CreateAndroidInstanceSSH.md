**Example 1: 创建安卓实例 SSH 连接**



Input: 

```
tccli gs CreateAndroidInstanceSSH --cli-unfold-argument  \
    --AndroidInstanceId cai-123456-abc \
    --ExpiredTime 2021-05-04T11:00:00Z
```

Output: 
```
{
    "Response": {
        "ConnectCommand": "ssh -i private_key.pem -p 12222 root@10.0.0.1",
        "PrivateKey": "private-key",
        "UserName": "root",
        "HostName": "10.0.0.1",
        "Port": 12222,
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```


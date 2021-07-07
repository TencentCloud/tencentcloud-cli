**Example 1: 创建COS上传密钥**



Input: 

```
tccli iotvideo CreateCOSCredentials --cli-unfold-argument  \
    --DeviceName device \
    --ProductId test
```

Output: 
```
{
    "Response": {
        "StoragePath": "path",
        "SecretKey": "key",
        "Token": "token",
        "ExpiredTime": 1625556088,
        "StorageBucket": "bucket",
        "RequestId": "xx",
        "SecretID": "id",
        "StorageRegion": "gz"
    }
}
```


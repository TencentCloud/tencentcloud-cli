**Example 1: 获取备份加密配置**



Input: 

```
tccli redis DescribeBackupEncryptConfig --cli-unfold-argument  \
    --InstanceId crs-lpj0rplv
```

Output: 
```
{
    "Response": {
        "BackupEncrypt": true,
        "EncryptKeyType": 0,
        "KmsKeyId": "b2f531ee-59a6-11f1-b8b2-5254008764f7",
        "KmsRegion": "ap-guangzhou",
        "RequestId": "e15c50dc-2147-4c6d-adb1-6a3d7c3cf9dc"
    }
}
```


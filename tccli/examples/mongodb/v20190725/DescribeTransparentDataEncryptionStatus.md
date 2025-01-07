**Example 1: 获取当前实例是否已开启数据加密**



Input: 

```
tccli mongodb DescribeTransparentDataEncryptionStatus --cli-unfold-argument  \
    --InstanceId cmgo-igjy****
```

Output: 
```
{
    "Response": {
        "TransparentDataEncryptionStatus": "open",
        "KeyInfoList": [
            {
                "KeyId": "65362a4b-5ec4-11ef-8467-**********",
                "KeyName": "myKey",
                "CreateTime": "2021-10-10 19:55:12",
                "Status": "Enabled",
                "KeyUsage": "TENCENT_KMS",
                "KeyOrigin": "TENCENT_KMS"
            }
        ],
        "RequestId": "59b477da-6473-4ea8-85b3-7f4473744981"
    }
}
```


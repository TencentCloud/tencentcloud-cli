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
        "KeyInfoList": [
            {
                "CreateTime": "2025-08-01 11:22:18",
                "KeyId": "***********************************",
                "KeyName": "******_test",
                "KeyOrigin": "******_KMS",
                "KeyUsage": "ENCRYPT_DECRYPT",
                "KmsRegion": "ap-guangzhou",
                "Status": "Enabled"
            }
        ],
        "RequestId": "38cac06f-7c6e-4596-9bd1-64eba8ed3e36",
        "TransparentDataEncryptionStatus": "open"
    }
}
```


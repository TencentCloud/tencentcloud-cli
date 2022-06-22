**Example 1: DescribeEncryptionKeys**

获取实例的密钥信息列表。

Input: 

```
tccli postgres DescribeEncryptionKeys --cli-unfold-argument  \
    --DBInstanceId  postgres-abcdefg
```

Output: 
```
{
    "Response": {
        "EncryptionKeys": [
            {
                "CreateTime": "2022-03-24 10:39:14",
                "DEKCipherTextBlob": "xxxxxxxxxxx",
                "IsEnabled": 1,
                "KeyAlias": "PGSQL-KMS",
                "KeyId": " f4d88aa7-ae72-11ec-9fcc-5254007ffd46",
                "KeyRegion": "ap-guangzhou"
            }
        ],
        "RequestId": "xxxxxxxx"
    }
}
```


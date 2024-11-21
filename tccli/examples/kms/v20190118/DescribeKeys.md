**Example 1: 获取多个主密钥属性**

获取多个主密钥属性。

Input: 

```
tccli kms DescribeKeys --cli-unfold-argument  \
    --KeyIds 87ff856e-973c-11ef-947b-525400d834e5 93866e69-9755-11ef-8e65-52540089bc41
```

Output: 
```
{
    "Response": {
        "KeyMetadatas": [
            {
                "Alias": "test8-lzc",
                "CreateTime": 1730347170,
                "CreatorUin": 700001224419,
                "DeletionDate": 0,
                "Description": "test描述",
                "HsmClusterId": "cls-hsm-3dflmo9g",
                "KeyId": "87ff856e-973c-11ef-947b-525400d834e5",
                "KeyRotationEnabled": false,
                "KeyState": "Enabled",
                "KeyUsage": "ENCRYPT_DECRYPT",
                "NextRotateTime": 1761883170,
                "Origin": "TENCENT_KMS",
                "Owner": "user",
                "ResourceId": "creatorUin/700001224419/87ff856e-973c-11ef-947b-525400d834e5",
                "Type": 4,
                "ValidTo": 0
            },
            {
                "Alias": "test11-lzc",
                "CreateTime": 1730357927,
                "CreatorUin": 700001224419,
                "DeletionDate": 0,
                "Description": "倒入外部密钥",
                "HsmClusterId": "cls-hsm-3dflmo9g",
                "KeyId": "93866e69-9755-11ef-8e65-52540089bc41",
                "KeyRotationEnabled": false,
                "KeyState": "Enabled",
                "KeyUsage": "ENCRYPT_DECRYPT",
                "NextRotateTime": 1761893927,
                "Origin": "EXTERNAL",
                "Owner": "user",
                "ResourceId": "creatorUin/700001224419/93866e69-9755-11ef-8e65-52540089bc41",
                "Type": 4,
                "ValidTo": 0
            }
        ],
        "RequestId": "05278c40-eb6c-473d-a1e6-00a8177f9c6a"
    }
}
```


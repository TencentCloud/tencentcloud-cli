**Example 1: 获取主密钥属性示例**

获取指定CMK的属性详情信息。

Input: 

```
tccli kms DescribeKey --cli-unfold-argument  \
    --KeyId 93866e69-9755-11ef-8e65-52540089bc41
```

Output: 
```
{
    "Response": {
        "KeyMetadata": {
            "Alias": "test11-lzc",
            "CreateTime": 1730357927,
            "CreatorUin": 700001224419,
            "DeletionDate": 0,
            "Description": "导入外部密钥",
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
        },
        "RequestId": "5575a949-8eda-497f-bee3-9d8a07763747"
    }
}
```


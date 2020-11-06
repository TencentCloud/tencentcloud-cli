**Example 1: 获取主密钥属性示例**

获取指定CMK的属性详情信息。

Input: 

```
tccli kms DescribeKey --cli-unfold-argument  \
    --KeyId 23e80852-1e38-11e9-b129-5cb9019b4b01
```

Output: 
```
{
    "Response": {
        "KeyMetadata": {
            "KeyId": "23e80852-1e38-11e9-b129-5cb9019b4b01",
            "Alias": "myalias",
            "CreateTime": 1548210729,
            "Description": "test cmk",
            "KeyState": "Enabled",
            "KeyUsage": "ENCRYPT_DECRYPT",
            "Type": 1,
            "CreatorUin": 1001,
            "KeyRotationEnabled": true,
            "Owner": "user",
            "NextRotateTime": 1553151489,
            "DeletionDate": 0,
            "Origin": "TENCENT_KMS",
            "ValidTo": 0
        },
        "RequestId": "1b580852-1e38-11e9-b129-5cb9019b4b00"
    }
}
```

**Example 2: 获取被计划删除主密钥属性示例**

此CMK被计划删除

Input: 

```
tccli kms DescribeKey --cli-unfold-argument  \
    --KeyId 23e80852-1e38-11e9-b129-5cb9019b4b02
```

Output: 
```
{
    "Response": {
        "KeyMetadata": {
            "KeyId": "23e80852-1e38-11e9-b129-5cb9019b4b02",
            "Alias": "myalias",
            "CreateTime": 1548210729,
            "Description": "test cmk",
            "KeyState": "PendingDelete",
            "KeyUsage": "ENCRYPT_DECRYPT",
            "Type": 1,
            "CreatorUin": 1001,
            "KeyRotationEnabled": true,
            "Owner": "user",
            "NextRotateTime": 1553151489,
            "DeletionDate": 1560580015,
            "Origin": "TENCENT_KMS",
            "ValidTo": 0
        },
        "RequestId": "1b580852-1e38-11e9-b129-5cb9019b4b00"
    }
}
```


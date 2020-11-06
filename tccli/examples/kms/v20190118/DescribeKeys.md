**Example 1: 获取多个主密钥属性**

获取多个主密钥属性。

Input: 

```
tccli kms DescribeKeys --cli-unfold-argument  \
    --KeyIds 23e80852-1e38-11e9-b129-5cb9019b4b01 23e80852-1e38-11e9-b129-5cb9019b4b02 23e80852-1e38-11e9-b129-5cb9019b4b03
```

Output: 
```
{
    "Response": {
        "KeyMetadatas": [
            {
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
            {
                "KeyId": "23e80852-1e38-11e9-b129-5cb9019b4b02",
                "Alias": "testalias",
                "CreateTime": 1548210730,
                "Description": "test cmk",
                "KeyState": "Disabled",
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
            {
                "KeyId": "23e80852-1e38-11e9-b129-5cb9019b4b03",
                "Alias": "testalias3",
                "CreateTime": 1548210730,
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
            }
        ],
        "RequestId": "1b580852-1e38-11e9-b129-5cb9019b4b00"
    }
}
```


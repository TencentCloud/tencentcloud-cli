**Example 1: Getting CMK attributes**

This example shows you how to get the attribute details of a specified CMK.

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

**Example 2: Getting the attributes of a CMK scheduled for deletion**

This example shows you how to get the attributes of a CMK scheduled for deletion.

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


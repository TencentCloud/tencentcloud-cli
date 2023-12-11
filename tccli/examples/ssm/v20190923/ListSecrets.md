**Example 1: 获取凭据详细信息列表**



Input: 

```
tccli ssm ListSecrets --cli-unfold-argument  \
    --Limit 2 \
    --SecretType 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "SecretMetadatas": [
            {
                "SecretName": "abc",
                "Description": "abc",
                "KmsKeyId": "abc",
                "CreateUin": 1,
                "Status": "abc",
                "DeleteTime": 1,
                "CreateTime": 1,
                "KmsKeyType": "abc",
                "RotationStatus": 0,
                "NextRotationTime": 1,
                "SecretType": 0,
                "ProductName": "abc",
                "ResourceName": "abc",
                "ProjectID": 0,
                "AssociatedInstanceIDs": [
                    "abc"
                ],
                "TargetUin": 1,
                "RotationFrequency": 0,
                "ResourceID": "abc",
                "RotationBeginTime": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```


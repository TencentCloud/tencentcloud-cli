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
                "Status": "xx",
                "Description": "xx",
                "AssociatedInstanceIDs": [
                    "xx"
                ],
                "CreateUin": 1,
                "ProjectID": 0,
                "ProductName": "xx",
                "RotationStatus": 0,
                "SecretType": 0,
                "KmsKeyId": "xx",
                "KmsKeyType": "xx",
                "SecretName": "xx",
                "ResourceName": "xx",
                "DeleteTime": 1,
                "CreateTime": 1,
                "NextRotationTime": 1,
                "TargetUin": 0
            },
            {
                "Status": "xx",
                "Description": "xx",
                "AssociatedInstanceIDs": [
                    "xx"
                ],
                "CreateUin": 1,
                "SecretName": "xx",
                "KmsKeyType": "xx",
                "ProductName": "xx",
                "SecretType": 0,
                "KmsKeyId": "xx",
                "RotationStatus": 0,
                "ProjectID": 0,
                "ResourceName": "xx",
                "DeleteTime": 1,
                "CreateTime": 1,
                "NextRotationTime": 1,
                "TargetUin": 0
            }
        ],
        "RequestId": "xx"
    }
}
```


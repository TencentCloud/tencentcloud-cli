**Example 1: 获取凭据详情信息**

获取凭据详情信息

Input: 

```
tccli ssm DescribeSecret --cli-unfold-argument  \
    --SecretName test
```

Output: 
```
{
    "Response": {
        "Status": "Enabled",
        "Description": "hello",
        "CreateUin": 1,
        "ResourceID": "inst-1",
        "ProductName": "redis",
        "RotationStatus": true,
        "KmsKeyId": "abc-ddd",
        "RequestId": "abc-hhm",
        "SecretType": 0,
        "SecretName": "secret-a",
        "RotationFrequency": 1,
        "DeleteTime": 1,
        "CreateTime": 1,
        "ResourceName": "db-user1",
        "ProjectID": 1,
        "AssociatedInstanceIDs": [
            "inst-1"
        ],
        "TargetUin": 12345,
        "AdditionalConfig": "{}"
    }
}
```


**Example 1: 根据过滤条件获取凭据列表信息**



Input: 

```
tccli ssm ListSecrets --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "SecretMetadatas": [
            {
                "AssociatedInstanceIDs": [],
                "CreateTime": 1784724042,
                "CreateUin": 700000579952,
                "CreateUinString": "700000579952",
                "DeleteTime": 0,
                "Description": "",
                "EncryptSwitching": false,
                "EncryptType": 0,
                "KmsKeyId": "31da3478-85b2-11f1-9b54-525400f44230",
                "KmsKeyType": "CUSTOMER",
                "NextRotationTime": 0,
                "ProductName": "default",
                "ProjectID": 0,
                "ResourceID": "251237300_700000579952_customize_1784724042855182311_RcI",
                "ResourceName": "",
                "RotationBeginTime": "",
                "RotationFrequency": 0,
                "RotationStatus": 0,
                "SecretName": "x1_003",
                "SecretType": 0,
                "Status": "Enabled",
                "TargetUin": 0,
                "TargetUinString": "0"
            }
        ],
        "TotalCount": 3,
        "RequestId": "2b80ea44-668c-456f-b298-2bdef4374efc"
    }
}
```


**Example 1: 获取凭据详细信息列表**



Input: 

```
tccli ssm ListSecrets --cli-unfold-argument  \
    --Offset 0 \
    --Limit 2 \
    --OrderType 1 \
    --State 1 \
    --SearchSecretName weijiali \
    --TagFilters.0.TagKey env \
    --TagFilters.0.TagValue dev \
    --SecretType 1 \
    --ProductName Mysql
```

Output: 
```
{
    "Response": {
        "RequestId": "c5ff5231-33e1-44cb-9b77-4d8972bd28ac",
        "SecretMetadatas": [
            {
                "AssociatedInstanceIDs": [
                    "ins-abfa"
                ],
                "CreateTime": 1724816350,
                "CreateUin": 700001028674,
                "DeleteTime": 0,
                "Description": "Weijiali_test_80008",
                "KmsKeyId": "9e46705b-8a1f-11ec-b941-5254008ad78d",
                "KmsKeyType": "DEFAULT",
                "NextRotationTime": 1732796420,
                "ProductName": "Mysql",
                "ProjectID": 0,
                "ResourceID": "cdb-mrhoqymb",
                "ResourceName": "testname",
                "RotationBeginTime": "2024-08-30 20:20:20",
                "RotationFrequency": 30,
                "RotationStatus": 1,
                "SecretName": "weijiali_test_00009",
                "SecretType": 1,
                "Status": "Enabled",
                "TargetUin": 0
            },
            {
                "AssociatedInstanceIDs": [
                    "ins-affe"
                ],
                "CreateTime": 1728713584,
                "CreateUin": 700001028674,
                "DeleteTime": 0,
                "Description": "yajiada_test_01",
                "KmsKeyId": "9e46705b-8a1f-11ec-b941-5254008ad78d",
                "KmsKeyType": "DEFAULT",
                "NextRotationTime": 1731305122,
                "ProductName": "Mysql",
                "ProjectID": 0,
                "ResourceID": "cdb-j6amb083",
                "ResourceName": "testName2",
                "RotationBeginTime": "2024-10-12 14:05:22",
                "RotationFrequency": 30,
                "RotationStatus": 1,
                "SecretName": "yajiada_test_01",
                "SecretType": 1,
                "Status": "Enabled",
                "TargetUin": 0
            }
        ],
        "TotalCount": 4
    }
}
```


**Example 1: 获取凭据详情信息**

获取凭据详情信息

Input: 

```
tccli ssm DescribeSecret --cli-unfold-argument  \
    --SecretName test3-db-secret
```

Output: 
```
{
    "Response": {
        "AdditionalConfig": "key1",
        "AssociatedInstanceIDs": [
            "cvm-test"
        ],
        "CreateTime": 1730272571,
        "CreateUin": 700001224419,
        "DeleteTime": 0,
        "Description": "测试数据库凭据创建",
        "KmsKeyId": "6abd1fdb-86d4-11ef-b72d-52540089bc41",
        "ProductName": "Mysql",
        "ProjectID": 0,
        "RequestId": "deb31013-2d0d-4b0c-a9dd-b62d8c3b2465",
        "ResourceID": "cdb-n4j3y33j",
        "ResourceName": "testresource",
        "RotationFrequency": 30,
        "RotationStatus": true,
        "SecretName": "test3-db-secret",
        "SecretType": 1,
        "Status": "Enabled",
        "TargetUin": 0
    }
}
```


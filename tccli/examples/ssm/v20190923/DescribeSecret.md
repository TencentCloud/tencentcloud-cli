**Example 1: 获取凭据详情信息**



Input: 

```
tccli ssm DescribeSecret --cli-unfold-argument  \
    --SecretName test
```

Output: 
```
{
    "Response": {
        "Status": "xx",
        "Description": "xx",
        "CreateUin": 1,
        "ResourceID": "xx",
        "ProductName": "xx",
        "RotationStatus": true,
        "KmsKeyId": "xx",
        "RequestId": "xx",
        "SecretType": 0,
        "SecretName": "xx",
        "RotationFrequency": 1,
        "DeleteTime": 1,
        "CreateTime": 1,
        "ResourceName": "xxx",
        "ProjectID": 1,
        "AssociatedInstanceIDs": [
            "xxx"
        ]
    }
}
```


**Example 1: 获取凭据详细信息列表**



Input: 

```
tccli ssm ListSecrets --cli-unfold-argument  \
    --Limit 2
```

Output: 
```
{
    "Response": {
        "RequestId": "3586bdc7-c8a5-4ccd-883f-9f256a96533a",
        "TotalCount": 8,
        "SecretMetadatas": [
            {
                "SecretName": "test",
                "Description": "test version 1.0",
                "KmsKeyId": "13437ab9-e002-11e9-9936-5254006d0810",
                "KmsKeyType": "DEFAULT",
                "CreateUin": 3350000000,
                "Status": "Enabled",
                "DeleteTime": 0,
                "CreateTime": 1574160561
            },
            {
                "SecretName": "test2",
                "Description": "test desc 2",
                "KmsKeyId": "13437ab9-e002-11e9-9936-5254006d0810",
                "KmsKeyType": "DEFAULT",
                "CreateUin": 3350000000,
                "Status": "Enabled",
                "DeleteTime": 0,
                "CreateTime": 1574067178
            }
        ]
    }
}
```


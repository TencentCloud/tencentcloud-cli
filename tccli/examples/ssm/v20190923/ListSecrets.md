**Example 1: 获取凭据详细信息列表**



Input: 

```
tccli ssm ListSecrets --cli-unfold-argument  \
    --Limit 2 \
    --SecretType 1
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
                "CreateUin": 1,
                "ProductName": "xx",
                "SecretType": 0,
                "KmsKeyId": "xx",
                "KmsKeyType": "xx",
                "SecretName": "xx",
                "DeleteTime": 1,
                "CreateTime": 1,
                "NextRotationTime": 1
            },
            {
                "Status": "xx",
                "Description": "xx",
                "CreateUin": 1,
                "KmsKeyType": "xx",
                "ProductName": "xx",
                "KmsKeyId": "xx",
                "SecretType": 0,
                "SecretName": "xx",
                "DeleteTime": 1,
                "CreateTime": 1,
                "NextRotationTime": 1
            }
        ],
        "RequestId": "xx"
    }
}
```


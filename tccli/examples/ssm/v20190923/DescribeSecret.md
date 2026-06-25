**Example 1: 获取凭据详细信息**

获取凭据详细信息

Input: 

```
tccli ssm DescribeSecret --cli-unfold-argument  \
    --SecretName SSM-OIDC-Weijiali_test_20260622004
```

Output: 
```
{
    "Response": {
        "AdditionalConfig": "",
        "AssociatedInstanceIDs": [],
        "CreateTime": 1782100116,
        "CreateUin": 100044683131,
        "CreateUinString": "100044683131",
        "DeleteTime": 0,
        "Description": "",
        "EncryptSwitching": false,
        "EncryptType": 0,
        "KmsKeyId": "fd950ef7-1ff5-11ea-90c1-525400ce83fb",
        "ProductName": "default",
        "ProjectID": 0,
        "ResourceID": "1258641191_100044683131_customize_1782100116409066358_fy2",
        "ResourceName": "",
        "RotationFrequency": 0,
        "RotationStatus": false,
        "SecretName": "SSM-OIDC-Weijiali_test_20260622004",
        "SecretType": 0,
        "Status": "Enabled",
        "TargetUin": 0,
        "TargetUinString": "0",
        "RequestId": "a8917cfc-d66b-4389-8c75-ae2697c3ca41"
    }
}
```


**Example 1: 获取凭据详细信息**



Input: 

```
tccli ssm DescribeSecret --cli-unfold-argument  \
    --SecretName prepaid-quota-gz-1779881924-003
```

Output: 
```
{
    "Response": {
        "AdditionalConfig": "",
        "AssociatedInstanceIDs": [],
        "CreateTime": 1779881929,
        "CreateUin": 700002670817,
        "CreateUinString": "700002670817",
        "DeleteTime": 0,
        "Description": "",
        "EncryptSwitching": false,
        "EncryptType": 1,
        "KmsKeyId": "",
        "ProductName": "default",
        "ProjectID": 0,
        "ResourceID": "260201473_700002670817_customize_1779881929918436370_W4H",
        "ResourceName": "",
        "RotationFrequency": 0,
        "RotationStatus": false,
        "SecretName": "prepaid-quota-gz-1779881924-003",
        "SecretType": 0,
        "Status": "Enabled",
        "TargetUin": 0,
        "TargetUinString": "0",
        "RequestId": "cd63cc40-4d71-4b1d-b571-bcd38be27787"
    }
}
```


**Example 1: 查询凭证列表**



Input: 

```
tccli csip DescribeKeySandboxCredentialList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "CreateTime": "2026-03-23T23:27:35.595Z",
                "CredentialEffectScope": {
                    "Exclude": 1,
                    "Instances": []
                },
                "CredentialId": "crd-923a222b",
                "CredentialName": "test1234",
                "CredentialType": "sts",
                "UpdateTime": "2026-03-23T23:27:35.595Z"
            }
        ],
        "TotalCount": 26,
        "RequestId": "9859afca-3e75-425b-9685-db32b0564d4a"
    }
}
```


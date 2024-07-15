**Example 1: 通过运行时roleId查询对应的软件 LICENSE**



Input: 

```
tccli cloudapp VerifyLicense --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "License": {
            "LicenseId": "abc",
            "LicenseMode": "abc",
            "LicenseStatus": "abc",
            "ProviderId": 1,
            "SoftwarePackageId": "abc",
            "SoftwarePackageVersion": "abc",
            "AuthorizedUserUin": "abc",
            "AuthorizedCloudappId": "abc",
            "AuthorizedCloudappRoleId": "abc",
            "AuthorizedSpecification": [
                {
                    "ParamKey": "abc",
                    "ParamValue": "abc",
                    "ParamKeyName": "abc",
                    "ParamValueName": "abc"
                }
            ],
            "BillingMode": 0,
            "LifeSpan": 0,
            "IssueDate": "2020-09-22T00:00:00+00:00",
            "ActivationDate": "2020-09-22T00:00:00+00:00",
            "ExpirationDate": "2020-09-22T00:00:00+00:00",
            "LifeSpanUnit": "abc"
        },
        "RequestId": "abc"
    }
}
```


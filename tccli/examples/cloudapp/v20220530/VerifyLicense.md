**Example 1: 通过运行时roleId查询对应的软件 LICENSE**



Input: 

```
tccli cloudapp VerifyLicense --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "License": {
            "LicenseId": "LICENSE_CLOUDAPP_A95275D8",
            "LicenseMode": "Subscription",
            "LicenseStatus": "Active",
            "ProviderId": 1,
            "SoftwarePackageId": "pkg-kby01bv4",
            "SoftwarePackageVersion": "1.0.0",
            "AuthorizedUserUin": "100008888888",
            "AuthorizedCloudappId": "cloudapp",
            "AuthorizedCloudappRoleId": "4000008000060000",
            "AuthorizedSpecification": [
                {
                    "ParamKey": "user_scale",
                    "ParamValue": "100",
                    "ParamKeyName": "用户规模",
                    "ParamValueName": "100人"
                }
            ],
            "BillingMode": 1,
            "LifeSpan": 1,
            "IssueDate": "2020-09-22T00:00:00+00:00",
            "ActivationDate": "2020-09-22T00:00:00+00:00",
            "ExpirationDate": "2020-09-23T00:00:00+00:00",
            "LifeSpanUnit": "D"
        },
        "RequestId": "abc"
    }
}
```


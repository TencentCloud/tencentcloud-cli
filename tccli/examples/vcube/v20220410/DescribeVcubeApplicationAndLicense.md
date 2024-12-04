**Example 1: 查询应用及其license**

查询应用及其license

Input: 

```
tccli vcube DescribeVcubeApplicationAndLicense --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ApplicationInfoList": [
            {
                "AppName": "abc",
                "BundleId": "abc",
                "AppType": "abc",
                "Licenses": [
                    {
                        "Type": "abc",
                        "Remark": "abc",
                        "StartTime": "abc",
                        "EndTime": "abc",
                        "FeatureId": 1,
                        "LicenseType": "abc",
                        "Renewal": true,
                        "LicenseId": 1,
                        "Name": "abc",
                        "Update": true,
                        "OldLicenseUrl": "abc",
                        "Group": 1,
                        "Expired": true,
                        "RestTime": 1,
                        "CreatedAt": "abc",
                        "UpdatedAt": "abc"
                    }
                ],
                "LicenseKey": "abc",
                "PackageName": "abc",
                "CreatedAt": "abc",
                "UpdatedAt": "abc",
                "ApplicationId": 1,
                "LicenseUrl": "abc",
                "XMagics": [
                    {
                        "Id": 1,
                        "CompanyName": "abc",
                        "CompanyPermit": "abc",
                        "CompanyType": "abc",
                        "Plan": "abc",
                        "LicenseType": "abc",
                        "Status": 1,
                        "Update": true,
                        "StartTime": "abc",
                        "EndTime": "abc",
                        "RenewalCount": 1,
                        "Reply": [
                            "abc"
                        ],
                        "CreatedAt": "abc",
                        "UpdatedAt": "abc",
                        "UpdateTime": "abc",
                        "Expired": true,
                        "RestTime": 1,
                        "XMagicType": "abc",
                        "Name": "abc"
                    }
                ],
                "MacBundleId": "abc",
                "WinProcessName": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```


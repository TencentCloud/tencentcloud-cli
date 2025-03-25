**Example 1: 查询视立方应用及优图license**

查询视立方应用及优图license

Input: 

```
tccli vcube DescribeVcubeApplicationAndXMagicList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ApplicationInfoList": [
            {
                "AppId": "1324373818_1",
                "AppName": "nengc",
                "AppType": "test",
                "ApplicationId": 1279,
                "BundleId": "nengc",
                "CreatedAt": "2024-05-28T10:56:07+08:00",
                "DomainList": null,
                "LicenseKey": "364d********580f",
                "LicenseUrl": "https://license.vod-pro.com/license/v2/1324373818_1/v_cube.license",
                "Licenses": [],
                "MacBundleId": null,
                "PackageName": "nengc",
                "UpdatedAt": "2024-09-05T16:32:57+08:00",
                "WinProcessName": null,
                "XMagics": [
                    {
                        "CompanyName": null,
                        "CompanyPermit": null,
                        "CompanyType": null,
                        "CreatedAt": "2024-05-28T10:56:07+08:00",
                        "EndTime": "2024-06-11T10:56:07+08:00",
                        "Expired": true,
                        "Id": 548,
                        "IsVest": false,
                        "LicenseType": "test",
                        "Name": "原子能力X1-03",
                        "Plan": "X1-03",
                        "RenewalCount": 1,
                        "Reply": [],
                        "Resource": null,
                        "RestTime": 0,
                        "StartTime": "2024-05-28T10:56:07+08:00",
                        "Status": 1,
                        "Update": null,
                        "UpdateTime": "2024-05-28T10:56:07+08:00",
                        "UpdatedAt": "2024-05-28T10:56:07+08:00",
                        "XMagicType": "single"
                    }
                ]
            }
        ],
        "RequestId": "cd1a74a4-5d28-4f92-809d-aa9780cf2dd8"
    }
}
```


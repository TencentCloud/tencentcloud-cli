**Example 1: 查询视立方应用及播放类license**

查询视立方应用及播放类license

Input: 

```
tccli vcube DescribeVcubeApplicationAndPlayList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ApplicationInfoList": [
            {
                "AppId": "132672799",
                "AppName": "腾讯云播放器license",
                "AppType": "formal",
                "ApplicationId": 1254,
                "BundleId": null,
                "CreatedAt": "2024-05-21T20:14:27+08:00",
                "DomainList": [
                    "dntest.nengchegn.com",
                    "pull.nengchegn.nengchegn.com"
                ],
                "LicenseKey": "8b53********7c3d",
                "LicenseUrl": "https://license.vod-pro.com/license/v2/132672799_1/v_cube.license",
                "Licenses": [
                    {
                        "CreatedAt": "2024-05-21T20:14:27+08:00",
                        "EndTime": "2025-05-22T00:00:00+08:00",
                        "Expired": false,
                        "FeatureId": 10000000,
                        "Group": 1,
                        "IsVest": false,
                        "LicenseId": 516,
                        "LicenseType": "formal",
                        "Name": "播放器 Web 端基础版",
                        "OldLicenseUrl": null,
                        "Remark": null,
                        "Renewal": false,
                        "Resource": null,
                        "RestTime": 12751397,
                        "StartTime": "2024-05-21T20:14:27+08:00",
                        "Type": "播放器基础版",
                        "Update": false,
                        "UpdatedAt": "2024-05-21T20:14:29+08:00"
                    }
                ],
                "MacBundleId": null,
                "PackageName": null,
                "UpdatedAt": "2024-10-31T15:25:49+08:00",
                "WinProcessName": null,
                "XMagics": null
            }
        ],
        "RequestId": "7c9a1888-32ea-4ee5-b3be-fe414aeed11d"
    }
}
```


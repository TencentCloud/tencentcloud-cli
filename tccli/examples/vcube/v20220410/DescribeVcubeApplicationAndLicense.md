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
                "AppId": "1252161597",
                "AppName": "能成",
                "AppType": "formal",
                "ApplicationId": 44167,
                "BundleId": "com.ningyuan.nengcheng",
                "CreatedAt": "2023-09-21T17:02:59+08:00",
                "DomainList": null,
                "LicenseKey": "84e0********5ade",
                "LicenseUrl": "https://license.vod2.myqcloud.com/license/v2/1252161597_1/v_cube.license",
                "Licenses": [
                    {
                        "CreatedAt": "2023-09-21T17:02:59+08:00",
                        "EndTime": "2025-04-08T00:00:00+08:00",
                        "Expired": false,
                        "FeatureId": 3,
                        "Group": 1,
                        "IsVest": false,
                        "LicenseId": 13237,
                        "LicenseType": "formal",
                        "Name": "短视频基础版",
                        "OldLicenseUrl": null,
                        "Remark": null,
                        "Renewal": false,
                        "Resource": null,
                        "RestTime": 8948754,
                        "StartTime": "2024-04-07T00:00:00+08:00",
                        "Type": "短视频制作基础版+视频播放",
                        "Update": false,
                        "UpdatedAt": "2024-04-07T09:54:50+08:00"
                    }
                ],
                "MacBundleId": null,
                "PackageName": "com.ny.jiuyi160_doctor",
                "UpdatedAt": "2024-09-05T16:49:01+08:00",
                "WinProcessName": null,
                "XMagics": null
            },
            {
                "AppId": "1252161497",
                "AppName": "健康160短视频",
                "AppType": "test",
                "ApplicationId": 32936,
                "BundleId": "com.nengcheng.pushapp",
                "CreatedAt": "2022-06-06T20:24:05+08:00",
                "DomainList": null,
                "LicenseKey": "84e1********5ade",
                "LicenseUrl": "https://license.vod2.myqcloud.com/license/v2/1252161597_1/v_cube.license",
                "Licenses": [
                    {
                        "CreatedAt": "2022-06-06T20:24:05+08:00",
                        "EndTime": "2022-06-21T00:00:00+08:00",
                        "Expired": true,
                        "FeatureId": 3,
                        "Group": 1,
                        "LicenseId": 27814,
                        "LicenseType": "test",
                        "Name": "短视频基础版",
                        "OldLicenseUrl": null,
                        "Remark": null,
                        "Renewal": true,
                        "Resource": null,
                        "RestTime": 0,
                        "StartTime": "2022-06-06T20:24:05+08:00",
                        "Type": "短视频制作基础版+视频播放",
                        "Update": false,
                        "UpdatedAt": "2022-06-06T20:24:06+08:00"
                    }
                ],
                "MacBundleId": null,
                "PackageName": "com.nengcheng.pushapp",
                "UpdatedAt": "2024-09-05T16:49:01+08:00",
                "WinProcessName": null,
                "XMagics": null
            },
            {
                "AppId": "1252161497",
                "AppName": "健康160",
                "AppType": "formal",
                "ApplicationId": 23940,
                "BundleId": "com.nengcheng.pushapp",
                "CreatedAt": "2021-08-09T12:08:15+08:00",
                "DomainList": null,
                "LicenseKey": "84e1********5ade",
                "LicenseUrl": "https://license.vod2.myqcloud.com/license/v2/1252161597_1/v_cube.license",
                "Licenses": [
                    {
                        "CreatedAt": "2021-08-09T12:08:15+08:00",
                        "EndTime": "2025-12-26T00:00:00+08:00",
                        "Expired": false,
                        "FeatureId": 3,
                        "Group": 1,
                        "IsVest": false,
                        "LicenseId": 6135,
                        "LicenseType": "formal",
                        "Name": "短视频基础版",
                        "OldLicenseUrl": "https://license.vod2.myqcloud.com/license/v1/f66e7b0c4c0631c10adeaee4b9611b/TXUgcSDK.licence",
                        "Remark": "原短视频基础版",
                        "Renewal": false,
                        "Resource": null,
                        "RestTime": 31585554,
                        "StartTime": "2024-12-25T00:00:00+08:00",
                        "Type": "短视频制作基础版+视频播放",
                        "Update": false,
                        "UpdatedAt": "2024-12-25T10:14:00+08:00"
                    }
                ],
                "MacBundleId": null,
                "PackageName": "cn.kidyn.nengcheng",
                "UpdatedAt": "2024-09-05T16:49:01+08:00",
                "WinProcessName": null,
                "XMagics": null
            }
        ],
        "RequestId": "a0612d8f-e8f6-43b9-b56c-b86bbc5ef051"
    }
}
```


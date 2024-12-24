**Example 1: 添加查询云应用列表请求**

查询应用列表

Input: 

```
tccli car DescribeApplicationList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20 \
    --Filters.0.Name ApplicationId \
    --Filters.0.Values app-6get57ac \
    --ApplicationCategory MOBILE
```

Output: 
```
{
    "Response": {
        "UserApplicationList": [
            {
                "ApplicationId": "app-6get57ac",
                "ApplicationName": "app_name",
                "ApplicationType": "Application3D",
                "ApplicationExePath": "CloudXR\\test.exe",
                "ApplicationInterList": "test_inter.exe",
                "ApplicationParams": "-param 123",
                "ApplicationCreateTime": "2021-08-29T08:00:30Z",
                "ApplicationRunStatus": "ApplicationRunning",
                "ApplicationUpdateStatus": "ApplicationUpdateNormal",
                "ApplicationUpdateProgress": 100,
                "ApplicationVersions": [
                    {
                        "ApplicationVersionId": "ver-gq4c5eq",
                        "ApplicationVersionSize": 1024,
                        "ApplicationVersionStatus": "Usable",
                        "ApplicationVersionName": "version_name",
                        "ApplicationVersionRegions": [
                            "ap-chinese-mainland",
                            "na-north-america-fusion"
                        ],
                        "ApplicationVersionUpdateMode": "FULL",
                        "CreateTime": "2021-08-29T08:00:30Z"
                    }
                ],
                "ApplicationBaseInfo": {
                    "WindowUseType": "ApplicationWindow",
                    "WindowName": "window _name",
                    "WindowClassName": "class_name",
                    "WindowCaptureMode": "HOOK"
                },
                "ApplicationNature": "PUBLIC",
                "ApplicationStores": [
                    {
                        "CosBucket": "bucket-123456",
                        "CosRegion": "ap-guangzhou",
                        "StoreType": "LOG",
                        "StoreState": "ON",
                        "StorePath": "CloudXR\\log"
                    },
                    {
                        "CosBucket": "bucket-123456",
                        "CosRegion": "ap-guangzhou",
                        "StoreType": "ARCHIVE",
                        "StoreState": "OFF",
                        "StorePath": "CloudXR\\archive"
                    }
                ]
            }
        ],
        "UserMobileApplicationList": [
            {
                "ApplicationId": "app-a1b2c3",
                "ApplicationName": "app_name",
                "ApplicationType": "ApplicationAPK",
                "ApplicationRunStatus": "ApplicationRunning",
                "ApplicationUpdateStatus": "ApplicationUpdateCreating",
                "ApplicationCreateTime": "2020-09-22T00:00:00+00:00",
                "ApplicationVersions": [
                    {
                        "ApplicationVersionId": "ver-a1b2c3",
                        "ApplicationVersionStatus": "Uploading",
                        "ApplicationVersionName": "version_name",
                        "CreateTime": "2020-09-22T00:00:00+00:00",
                        "ApplicationVersionRegions": [],
                        "ApplicationVersionUpdateMode": "",
                        "ApplicationVersionSize": 0
                    }
                ],
                "ApplicationNature": "PUBLIC"
            }
        ],
        "ApplicationTotal": 100,
        "RequestId": "4eb17e58-68da-4e9a-b298-0894723c9022"
    }
}
```


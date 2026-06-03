**Example 1: 查询功能列表**

查询功能列表

Input: 

```
tccli vcube DescribeLicenseList --cli-unfold-argument  \
    --PageNumber 0 \
    --PageSize 10 \
    --Platform pc
```

Output: 
```
{
    "Response": {
        "Count": 1,
        "LicenseList": [
            {
                "Application": {
                    "AppName": "鸿蒙测试",
                    "BundleId": null,
                    "DomainList": null,
                    "Id": 56322,
                    "MacBundleId": null,
                    "PackageName": null,
                    "WinProcessName": null
                },
                "CreatedAt": "2024-12-19T19:22:54+08:00",
                "EndTime": "2025-01-20T00:00:00+08:00",
                "FeatureId": 1536,
                "LicenseId": 19679,
                "LicenseType": "formal",
                "Name": "播放器移动端高级版",
                "Plan": null,
                "RestTime": 2291330,
                "StartTime": "2024-12-19T00:00:00+08:00",
                "Type": "播放器高级版",
                "UpdatedAt": "2024-12-19T19:22:56+08:00"
            }
        ],
        "Overview": {
            "Expired": 0,
            "Near": 1,
            "Valid": 1
        },
        "RequestId": "7fcb8013-76e0-4d1c-8d93-bb75d94868cc",
        "TrialOverview": {
            "Expired": 0,
            "Near": 0,
            "Valid": 0
        }
    }
}
```


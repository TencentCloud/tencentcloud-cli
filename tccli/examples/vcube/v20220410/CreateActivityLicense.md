**Example 1: 创建活动license**

推广活动创建的license

Input: 

```
tccli vcube CreateActivityLicense --cli-unfold-argument  \
    --Activity 872644585
```

Output: 
```
{
    "Response": {
        "AppId": "1329836514",
        "AppName": "连麦测试License",
        "BundleId": "com.tencent.mlvb.apiexample",
        "Duration": 14,
        "EndTime": "2024-12-25 00:00:00",
        "LicenseKey": "30c9********2ebc",
        "LicenseUrl": "https://license.vod2.myqcloud.com/license/v2/1329836514_1/v_cube.license",
        "PackageName": "com.tencent.mlvb.apiexample",
        "RequestId": "15d3f555-0d09-4bd0-9f6b-51e8148d881b",
        "Residue": 1261307,
        "ResidueDay": 14,
        "StartTime": "2024-12-10 09:21:30"
    }
}
```


**Example 1: 获取优图资源列表**

视立方获取资源列表

Input: 

```
tccli vcube DescribeXMagicResourceList --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 1
```

Output: 
```
{
    "Response": {
        "Count": 1,
        "RequestId": "094a3e49-200a-4841-8d29-849763a6e6a4",
        "Resources": [
            {
                "AppId": "1317625488",
                "Application": {
                    "AppId": "1317625488",
                    "AppName": "nengc.app",
                    "AppType": "formal",
                    "BundleId": "com.nengc.app",
                    "CreatedAt": "2023-02-13T06:44:23.605Z",
                    "DomainList": [
                        "tencet.com"
                    ],
                    "Id": 412,
                    "MacBundleId": "com.nengc",
                    "PackageName": "com.nengc.app",
                    "UpdatedAt": "2024-09-05T08:32:57.951Z",
                    "WinProcessName": "com.nengc"
                },
                "AutoRenewFlag": 1,
                "Operation": [
                    "negnc"
                ],
                "BizType": "xmagic",
                "CreatedAt": "2024-04-12T04:13:33.438Z",
                "Duration": "1",
                "EndTime": "2025-04-12T12:13:33+08:00",
                "Id": 79,
                "IsUse": false,
                "Name": "Advanced S101",
                "Plan": "S1-01",
                "ResourceId": "xmc11671a6134d082bf79",
                "StartTime": "2024-04-12T12:13:33+08:00",
                "Status": 2,
                "UpdatedAt": "2024-04-12T04:18:17.000Z",
                "XMagic": {
                    "Id": 301,
                    "Status": 1
                },
                "XMagicType": "combined"
            }
        ]
    }
}
```


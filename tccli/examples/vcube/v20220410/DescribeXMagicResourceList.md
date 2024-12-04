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
        "Resources": [
            {
                "Id": 1,
                "AppId": "abc",
                "Plan": "abc",
                "Duration": "abc",
                "CreatedAt": "abc",
                "UpdatedAt": "abc",
                "StartTime": "abc",
                "EndTime": "abc",
                "Application": {
                    "Id": 1,
                    "AppId": "abc",
                    "AppName": "abc",
                    "BundleId": "abc",
                    "PackageName": "abc",
                    "AppType": "abc",
                    "CreatedAt": "abc",
                    "UpdatedAt": "abc",
                    "MacBundleId": "abc",
                    "WinProcessName": "abc"
                },
                "XMagic": {
                    "Id": 1,
                    "Status": 1
                },
                "Status": 1,
                "Operation": [
                    "abc"
                ],
                "IsUse": true,
                "XMagicType": "abc",
                "Name": "abc",
                "BizType": "abc",
                "ResourceId": "abc"
            }
        ],
        "Count": 1,
        "RequestId": "abc"
    }
}
```


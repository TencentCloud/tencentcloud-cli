**Example 1: 查询视立方 license 资源列表**

查询视立方 license 资源列表

Input: 

```
tccli vcube DescribeVcubeResourcesList --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 1
```

Output: 
```
{
    "Response": {
        "ResourceList": [
            {
                "Id": 1,
                "AppId": "abc",
                "Duration": "abc",
                "FeatureId": 1,
                "StartTime": "abc",
                "EndTime": "abc",
                "CreatedAt": "abc",
                "UpdatedAt": "abc",
                "IsUse": true,
                "Status": 1,
                "IsolatedTimestamp": "abc",
                "Name": "abc",
                "Type": "abc",
                "Package": {
                    "Id": 0,
                    "BizResourceId": "abc",
                    "Site": "abc",
                    "StartTime": "abc",
                    "EndTime": "abc",
                    "RefundTime": "abc",
                    "Name": "abc",
                    "Type": "abc"
                },
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
                    "WinProcessName": "abc",
                    "DomainList": [
                        "abc"
                    ]
                },
                "ResourceId": "abc",
                "AutoRenewFlag": 1
            }
        ],
        "TotalCount": 1,
        "RequestId": "abc"
    }
}
```


**Example 1: 查询视立方 license 资源列表**

查询视立方 license 资源列表

Input: 

```
tccli vcube DescribeVcubeResourcesList --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "RequestId": "d80c068d-72b8-47b1-9188-abe5da6fc2f2",
        "ResourceList": [
            {
                "AppId": "12524561497",
                "Application": null,
                "AutoRenewFlag": 0,
                "CreatedAt": "2023-01-11T06:57:09.396Z",
                "Duration": null,
                "EndTime": "2024-01-12T00:00:00+08:00",
                "FeatureId": 3,
                "Id": 51566,
                "IsUse": false,
                "IsolatedTimestamp": null,
                "Name": "短视频基础版",
                "Package": {
                    "BizResourceId": "159230",
                    "EndTime": "2024-01-10 23:59:59",
                    "Id": 57715,
                    "Name": "50TB点播流量包",
                    "RefundTime": null,
                    "Site": "China",
                    "StartTime": "2023-01-11 00:00:00",
                    "Type": "20016"
                },
                "ResourceId": "51386",
                "StartTime": "2023-01-11T00:00:00+08:00",
                "Status": 3,
                "Type": "短视频制作基础版+视频播放",
                "UpdatedAt": "2024-01-13T08:48:08.000Z"
            }
        ],
        "TotalCount": 1
    }
}
```


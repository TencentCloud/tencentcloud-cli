**Example 1: 查询视立方 license 资源**

查询视立方 license 资源

Input: 

```
tccli vcube DescribeVcubeResources --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "5e6142f1-0917-4b8c-9698-0ca4e3c481aa",
        "ResourceList": [
            {
                "AppId": "12521345497",
                "AutoRenewFlag": 0,
                "CreatedAt": "2024-12-25T02:13:43.013Z",
                "Duration": null,
                "EndTime": "2025-12-26T00:00:00+08:00",
                "FeatureId": 3,
                "Id": 110944,
                "IsUse": true,
                "IsolatedTimestamp": null,
                "Name": "短视频基础版",
                "Package": {
                    "BizResourceId": "247536",
                    "EndTime": "2025-12-24 23:59:59",
                    "Id": 116009,
                    "Name": "50TB点播流量包",
                    "RefundTime": null,
                    "Site": "China",
                    "StartTime": "2024-12-25 00:00:00",
                    "Type": "20016"
                },
                "ResourceId": "luvc3696195679763e4",
                "StartTime": "2024-12-25T00:00:00+08:00",
                "Status": 1,
                "Type": "短视频制作基础版+视频播放",
                "UpdatedAt": "2024-12-25T02:13:43.013Z"
            }
        ]
    }
}
```


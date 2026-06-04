**Example 1: DescribeAppSummaryList**

查询应用列表

Input: 

```
tccli adp DescribeAppSummaryList --cli-unfold-argument  \
    --SpaceId default_space \
    --FilterList.0.Name AppStatus \
    --FilterList.0.ValueList 1 \
    --PageNumber 0 \
    --PageSize 10 \
    --Query 信息
```

Output: 
```
{
    "Response": {
        "AppSummaryList": [
            {
                "AppId": "206*************320",
                "AppMode": 2,
                "Avatar": "https://cdn.xiaowei.qq.com/static/adp/app-default-avatar.png",
                "Name": "测试的应用信息",
                "OperationInfo": {
                    "Creator": "wu******g",
                    "CreatorUin": "700****06554",
                    "CreatorUserAccount": "",
                    "UpdateTime": "1780042649",
                    "Updater": "wu******g",
                    "UpdaterUin": "700000306554"
                },
                "PermissionIdList": [
                    "adpAppEdit"
                ],
                "Status": {
                    "Status": 1,
                    "StatusDescription": "未上线"
                },
                "SubStatus": null
            }
        ],
        "TotalCount": 1,
        "RequestId": "5163c167-3c4e-487d-9c1d-b42896dc1c8e"
    }
}
```


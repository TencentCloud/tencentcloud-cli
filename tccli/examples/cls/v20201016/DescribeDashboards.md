**Example 1: 获取仪表盘**



Input: 

```
tccli cls DescribeDashboards --cli-unfold-argument  \
    --Limit 0 \
    --Filters.0.Values xx \
    --Filters.0.Key xx \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "DashboardInfos": [
            {
                "UpdateTime": "xx",
                "Tags": [
                    {
                        "Value": "xx",
                        "Key": "xx"
                    }
                ],
                "DashboardName": "xx",
                "DashboardRegion": "xx",
                "AssumerName": "xx",
                "DashboardId": "xx",
                "RoleName": "xx",
                "Data": "xx",
                "CreateTime": "xx",
                "AssumerUin": 1,
                "DashboardTopicInfos": [
                    {
                        "TopicId": "xx",
                        "Region": "xx"
                    }
                ]
            }
        ],
        "RequestId": "xx"
    }
}
```


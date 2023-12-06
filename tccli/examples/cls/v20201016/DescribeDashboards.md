**Example 1: 获取仪表盘**

获取仪表盘

Input: 

```
tccli cls DescribeDashboards --cli-unfold-argument  \
    --Limit 1 \
    --Filters.0.Values dashboard-7ff51cf1-bff9-49f7-9fbb-6a9743225f92 \
    --Filters.0.Key dashboardId \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "DashboardInfos": [
            {
                "AssumerName": "",
                "AssumerUin": 0,
                "CreateTime": "2023-12-01 15:53:29",
                "DashboardId": "dashboard-7ff51cf1-bff9-49f7-9fbb-6a9743225f92",
                "DashboardName": "E32E23",
                "DashboardRegion": "",
                "DashboardTopicInfos": [],
                "Data": "",
                "RoleName": "",
                "Tags": [
                    {
                        "Key": "team",
                        "Value": "test"
                    }
                ],
                "UpdateTime": "2023-12-01 15:53:29"
            }
        ],
        "RequestId": "56c8e3f5-2b05-419d-acd0-8d2062df093f",
        "TotalCount": 1
    }
}
```


**Example 1: 通过tag:key获取仪表盘**

通过tag:key获取仪表盘

Input: 

```
tccli cls DescribeDashboards --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20 \
    --Filters.0.Key tag:bowww-tag-key \
    --Filters.0.Values bowww-tag-value
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "DashboardInfos": [
            {
                "DashboardId": "dashboard-47bf0f13-279c-461f-bb78-5b60229177ea",
                "DashboardName": "API-TEST2",
                "Data": "",
                "CreateTime": "2023-07-05 20:46:25",
                "UpdateTime": "2023-08-25 11:18:18",
                "DashboardRegion": "",
                "DashboardTopicInfos": [],
                "AssumerUin": 0,
                "RoleName": "",
                "AssumerName": "",
                "Tags": [
                    {
                        "Key": "bowww-tag-key",
                        "Value": "bowww-tag-value"
                    },
                    {
                        "Key": "bowww-tag-key1",
                        "Value": "bowww-tag-value1"
                    }
                ]
            }
        ],
        "RequestId": "6bf3355c-3c88-4566-89c8-76c3ca37bae9"
    }
}
```

**Example 2: 通过dashboardId获取仪表盘**

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


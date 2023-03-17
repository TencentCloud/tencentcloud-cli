**Example 1: 查询全地域实例概览**



Input: 

```
tccli lighthouse DescribeAllInstancesOverview --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AllInstancesOverview": {
            "ExpiringCount": 100,
            "RunningCount": 10,
            "ShutdownCount": 20,
            "TotalCount": 100
        },
        "InstancesDetailSet": [
            {
                "InstancesOverview": {
                    "ExpiringCount": 10,
                    "RunningCount": 1,
                    "ShutdownCount": 2,
                    "TotalCount": 10
                },
                "QuotaOverview": {
                    "Available": 6,
                    "Total": 10
                },
                "Region": "eu-moscow"
            },
            {
                "InstancesOverview": {
                    "ExpiringCount": 10,
                    "RunningCount": 1,
                    "ShutdownCount": 2,
                    "TotalCount": 10
                },
                "QuotaOverview": {
                    "Available": 6,
                    "Total": 10
                },
                "Region": "ap-shanghai"
            },
            {
                "InstancesOverview": {
                    "ExpiringCount": 10,
                    "RunningCount": 1,
                    "ShutdownCount": 2,
                    "TotalCount": 10
                },
                "QuotaOverview": {
                    "Available": 6,
                    "Total": 10
                },
                "Region": "ap-singapore"
            },
            {
                "InstancesOverview": {
                    "ExpiringCount": 10,
                    "RunningCount": 1,
                    "ShutdownCount": 2,
                    "TotalCount": 10
                },
                "QuotaOverview": {
                    "Available": 6,
                    "Total": 10
                },
                "Region": "ap-nanjing"
            },
            {
                "InstancesOverview": {
                    "ExpiringCount": 10,
                    "RunningCount": 1,
                    "ShutdownCount": 2,
                    "TotalCount": 10
                },
                "QuotaOverview": {
                    "Available": 6,
                    "Total": 10
                },
                "Region": "ap-guangzhou"
            },
            {
                "InstancesOverview": {
                    "ExpiringCount": 10,
                    "RunningCount": 1,
                    "ShutdownCount": 2,
                    "TotalCount": 10
                },
                "QuotaOverview": {
                    "Available": 6,
                    "Total": 10
                },
                "Region": "na-siliconvalley"
            },
            {
                "InstancesOverview": {
                    "ExpiringCount": 10,
                    "RunningCount": 1,
                    "ShutdownCount": 2,
                    "TotalCount": 10
                },
                "QuotaOverview": {
                    "Available": 6,
                    "Total": 10
                },
                "Region": "ap-hongkong"
            },
            {
                "InstancesOverview": {
                    "ExpiringCount": 10,
                    "RunningCount": 1,
                    "ShutdownCount": 2,
                    "TotalCount": 10
                },
                "QuotaOverview": {
                    "Available": 6,
                    "Total": 10
                },
                "Region": "ap-tokyo"
            },
            {
                "InstancesOverview": {
                    "ExpiringCount": 10,
                    "RunningCount": 1,
                    "ShutdownCount": 2,
                    "TotalCount": 10
                },
                "QuotaOverview": {
                    "Available": 6,
                    "Total": 10
                },
                "Region": "ap-beijing"
            },
            {
                "InstancesOverview": {
                    "ExpiringCount": 10,
                    "RunningCount": 1,
                    "ShutdownCount": 2,
                    "TotalCount": 10
                },
                "QuotaOverview": {
                    "Available": 6,
                    "Total": 10
                },
                "Region": "ap-chengdu"
            }
        ],
        "RequestId": "cff0ed47-ed04-4656-a517-d642967040ff"
    }
}
```


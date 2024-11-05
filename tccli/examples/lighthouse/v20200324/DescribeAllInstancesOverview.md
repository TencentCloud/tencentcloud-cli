**Example 1: 查询全地域实例概览**



Input: 

```
tccli lighthouse DescribeAllInstancesOverview --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "14e4cb2b-cf4a-4d8b-a0d5-44341cf97f34",
        "AllInstancesOverview": {
            "TotalCount": 6672,
            "RunningCount": 5856,
            "ShutdownCount": 64,
            "ExpiringCount": 0,
            "ExpiredCount": 6624
        },
        "InstancesDetailSet": [
            {
                "Region": "ap-guangzhou",
                "InstancesOverview": {
                    "TotalCount": 417,
                    "RunningCount": 366,
                    "ShutdownCount": 4,
                    "ExpiringCount": 0,
                    "ExpiredCount": 414
                },
                "QuotaOverview": {
                    "Total": 100,
                    "Available": 18
                },
                "ErrorCode": ""
            },
            {
                "Region": "ap-shanghai",
                "InstancesOverview": {
                    "TotalCount": 417,
                    "RunningCount": 366,
                    "ShutdownCount": 4,
                    "ExpiringCount": 0,
                    "ExpiredCount": 414
                },
                "QuotaOverview": {
                    "Total": 100,
                    "Available": 18
                },
                "ErrorCode": ""
            },
            {
                "Region": "ap-hongkong",
                "InstancesOverview": {
                    "TotalCount": 417,
                    "RunningCount": 366,
                    "ShutdownCount": 4,
                    "ExpiringCount": 0,
                    "ExpiredCount": 414
                },
                "QuotaOverview": {
                    "Total": 100,
                    "Available": 18
                },
                "ErrorCode": ""
            },
            {
                "Region": "ap-beijing",
                "InstancesOverview": {
                    "TotalCount": 417,
                    "RunningCount": 366,
                    "ShutdownCount": 4,
                    "ExpiringCount": 0,
                    "ExpiredCount": 414
                },
                "QuotaOverview": {
                    "Total": 100,
                    "Available": 18
                },
                "ErrorCode": ""
            },
            {
                "Region": "ap-singapore",
                "InstancesOverview": {
                    "TotalCount": 417,
                    "RunningCount": 366,
                    "ShutdownCount": 4,
                    "ExpiringCount": 0,
                    "ExpiredCount": 414
                },
                "QuotaOverview": {
                    "Total": 100,
                    "Available": 18
                },
                "ErrorCode": ""
            },
            {
                "Region": "na-siliconvalley",
                "InstancesOverview": {
                    "TotalCount": 417,
                    "RunningCount": 366,
                    "ShutdownCount": 4,
                    "ExpiringCount": 0,
                    "ExpiredCount": 414
                },
                "QuotaOverview": {
                    "Total": 100,
                    "Available": 18
                },
                "ErrorCode": ""
            },
            {
                "Region": "ap-chengdu",
                "InstancesOverview": {
                    "TotalCount": 417,
                    "RunningCount": 366,
                    "ShutdownCount": 4,
                    "ExpiringCount": 0,
                    "ExpiredCount": 414
                },
                "QuotaOverview": {
                    "Total": 100,
                    "Available": 18
                },
                "ErrorCode": ""
            },
            {
                "Region": "ap-tokyo",
                "InstancesOverview": {
                    "TotalCount": 417,
                    "RunningCount": 366,
                    "ShutdownCount": 4,
                    "ExpiringCount": 0,
                    "ExpiredCount": 414
                },
                "QuotaOverview": {
                    "Total": 100,
                    "Available": 18
                },
                "ErrorCode": ""
            },
            {
                "Region": "ap-nanjing",
                "InstancesOverview": {
                    "TotalCount": 417,
                    "RunningCount": 366,
                    "ShutdownCount": 4,
                    "ExpiringCount": 0,
                    "ExpiredCount": 414
                },
                "QuotaOverview": {
                    "Total": 100,
                    "Available": 18
                },
                "ErrorCode": ""
            },
            {
                "Region": "ap-mumbai",
                "InstancesOverview": {
                    "TotalCount": 417,
                    "RunningCount": 366,
                    "ShutdownCount": 4,
                    "ExpiringCount": 0,
                    "ExpiredCount": 414
                },
                "QuotaOverview": {
                    "Total": 100,
                    "Available": 18
                },
                "ErrorCode": ""
            },
            {
                "Region": "eu-frankfurt",
                "InstancesOverview": {
                    "TotalCount": 417,
                    "RunningCount": 366,
                    "ShutdownCount": 4,
                    "ExpiringCount": 0,
                    "ExpiredCount": 414
                },
                "QuotaOverview": {
                    "Total": 100,
                    "Available": 18
                },
                "ErrorCode": ""
            },
            {
                "Region": "ap-seoul",
                "InstancesOverview": {
                    "TotalCount": 417,
                    "RunningCount": 366,
                    "ShutdownCount": 4,
                    "ExpiringCount": 0,
                    "ExpiredCount": 414
                },
                "QuotaOverview": {
                    "Total": 100,
                    "Available": 18
                },
                "ErrorCode": ""
            },
            {
                "Region": "ap-jakarta",
                "InstancesOverview": {
                    "TotalCount": 417,
                    "RunningCount": 366,
                    "ShutdownCount": 4,
                    "ExpiringCount": 0,
                    "ExpiredCount": 414
                },
                "QuotaOverview": {
                    "Total": 100,
                    "Available": 18
                },
                "ErrorCode": ""
            },
            {
                "Region": "sa-saopaulo",
                "InstancesOverview": {
                    "TotalCount": 417,
                    "RunningCount": 366,
                    "ShutdownCount": 4,
                    "ExpiringCount": 0,
                    "ExpiredCount": 414
                },
                "QuotaOverview": {
                    "Total": 100,
                    "Available": 18
                },
                "ErrorCode": ""
            },
            {
                "Region": "ap-bangkok",
                "InstancesOverview": {
                    "TotalCount": 417,
                    "RunningCount": 366,
                    "ShutdownCount": 4,
                    "ExpiringCount": 0,
                    "ExpiredCount": 414
                },
                "QuotaOverview": {
                    "Total": 100,
                    "Available": 18
                },
                "ErrorCode": ""
            },
            {
                "Region": "na-ashburn",
                "InstancesOverview": {
                    "TotalCount": 417,
                    "RunningCount": 366,
                    "ShutdownCount": 4,
                    "ExpiringCount": 0,
                    "ExpiredCount": 414
                },
                "QuotaOverview": {
                    "Total": 100,
                    "Available": 18
                },
                "ErrorCode": ""
            }
        ]
    }
}
```


**Example 1: 查询全地域云硬盘备份点概览**



Input: 

```
tccli lighthouse DescribeAllDiskBackupsOverview --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "5116bf04-9e01-49fc-9f80-2688b947e00d",
        "AllDiskBackupsOverview": {
            "TotalCount": 13,
            "NormalCount": 0
        },
        "DiskBackupsDetailSet": [
            {
                "Region": "ap-chengdu",
                "DiskBackupsOverview": {
                    "TotalCount": 1,
                    "NormalCount": 0
                }
            },
            {
                "Region": "eu-moscow",
                "DiskBackupsOverview": {
                    "TotalCount": 1,
                    "NormalCount": 0
                }
            },
            {
                "Region": "na-toronto",
                "DiskBackupsOverview": {
                    "TotalCount": 1,
                    "NormalCount": 0
                }
            },
            {
                "Region": "ap-hongkong",
                "DiskBackupsOverview": {
                    "TotalCount": 1,
                    "NormalCount": 0
                }
            },
            {
                "Region": "na-siliconvalley",
                "DiskBackupsOverview": {
                    "TotalCount": 1,
                    "NormalCount": 0
                }
            },
            {
                "Region": "ap-tokyo",
                "DiskBackupsOverview": {
                    "TotalCount": 1,
                    "NormalCount": 0
                }
            },
            {
                "Region": "ap-beijing",
                "DiskBackupsOverview": {
                    "TotalCount": 1,
                    "NormalCount": 0
                }
            },
            {
                "Region": "ap-singapore",
                "DiskBackupsOverview": {
                    "TotalCount": 1,
                    "NormalCount": 0
                }
            },
            {
                "Region": "ap-guangzhou",
                "DiskBackupsOverview": {
                    "TotalCount": 1,
                    "NormalCount": 0
                }
            },
            {
                "Region": "ap-shanghai",
                "DiskBackupsOverview": {
                    "TotalCount": 1,
                    "NormalCount": 0
                }
            },
            {
                "Region": "ap-mumbai",
                "DiskBackupsOverview": {
                    "TotalCount": 1,
                    "NormalCount": 0
                }
            },
            {
                "Region": "ap-nanjing",
                "DiskBackupsOverview": {
                    "TotalCount": 1,
                    "NormalCount": 0
                }
            },
            {
                "Region": "eu-frankfurt",
                "DiskBackupsOverview": {
                    "TotalCount": 1,
                    "NormalCount": 0
                }
            }
        ]
    }
}
```


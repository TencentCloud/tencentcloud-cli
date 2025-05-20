**Example 1: 查询全地域磁盘概览**



Input: 

```
tccli lighthouse DescribeAllDisksOverview --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AllDataDisksOverview": {
            "ExpiringCount": 25,
            "ShutdownCount": 1,
            "TotalCount": 57
        },
        "AllSystemDisksOverview": {
            "TotalCount": 170
        },
        "DisksDetailSet": [
            {
                "DataDisksOverview": {
                    "ExpiringCount": 3,
                    "ShutdownCount": 1,
                    "TotalCount": 4
                },
                "ErrorCode": "",
                "Region": "ap-guangzhou",
                "SystemDisksOverview": {
                    "TotalCount": 8
                }
            },
            {
                "DataDisksOverview": {
                    "ExpiringCount": 1,
                    "ShutdownCount": 0,
                    "TotalCount": 3
                },
                "ErrorCode": "",
                "Region": "ap-shanghai",
                "SystemDisksOverview": {
                    "TotalCount": 5
                }
            },
            {
                "DataDisksOverview": {
                    "ExpiringCount": 0,
                    "ShutdownCount": 0,
                    "TotalCount": 0
                },
                "ErrorCode": "",
                "Region": "ap-hongkong",
                "SystemDisksOverview": {
                    "TotalCount": 3
                }
            },
            {
                "DataDisksOverview": {
                    "ExpiringCount": 2,
                    "ShutdownCount": 0,
                    "TotalCount": 3
                },
                "ErrorCode": "",
                "Region": "ap-beijing",
                "SystemDisksOverview": {
                    "TotalCount": 35
                }
            },
            {
                "DataDisksOverview": {
                    "ExpiringCount": 0,
                    "ShutdownCount": 0,
                    "TotalCount": 2
                },
                "ErrorCode": "",
                "Region": "ap-singapore",
                "SystemDisksOverview": {
                    "TotalCount": 6
                }
            },
            {
                "DataDisksOverview": {
                    "ExpiringCount": 4,
                    "ShutdownCount": 0,
                    "TotalCount": 6
                },
                "ErrorCode": "",
                "Region": "na-siliconvalley",
                "SystemDisksOverview": {
                    "TotalCount": 1
                }
            },
            {
                "DataDisksOverview": {
                    "ExpiringCount": 1,
                    "ShutdownCount": 0,
                    "TotalCount": 4
                },
                "ErrorCode": "",
                "Region": "ap-chengdu",
                "SystemDisksOverview": {
                    "TotalCount": 3
                }
            },
            {
                "DataDisksOverview": {
                    "ExpiringCount": 3,
                    "ShutdownCount": 0,
                    "TotalCount": 4
                },
                "ErrorCode": "",
                "Region": "ap-tokyo",
                "SystemDisksOverview": {
                    "TotalCount": 1
                }
            },
            {
                "DataDisksOverview": {
                    "ExpiringCount": 0,
                    "ShutdownCount": 0,
                    "TotalCount": 4
                },
                "ErrorCode": "",
                "Region": "ap-nanjing",
                "SystemDisksOverview": {
                    "TotalCount": 3
                }
            },
            {
                "DataDisksOverview": {
                    "ExpiringCount": 2,
                    "ShutdownCount": 0,
                    "TotalCount": 2
                },
                "ErrorCode": "",
                "Region": "ap-mumbai",
                "SystemDisksOverview": {
                    "TotalCount": 2
                }
            },
            {
                "DataDisksOverview": {
                    "ExpiringCount": 5,
                    "ShutdownCount": 0,
                    "TotalCount": 7
                },
                "ErrorCode": "",
                "Region": "eu-frankfurt",
                "SystemDisksOverview": {
                    "TotalCount": 1
                }
            },
            {
                "DataDisksOverview": {
                    "ExpiringCount": 0,
                    "ShutdownCount": 0,
                    "TotalCount": 2
                },
                "ErrorCode": "",
                "Region": "na-toronto",
                "SystemDisksOverview": {
                    "TotalCount": 0
                }
            },
            {
                "DataDisksOverview": {
                    "ExpiringCount": 1,
                    "ShutdownCount": 0,
                    "TotalCount": 11
                },
                "ErrorCode": "",
                "Region": "ap-seoul",
                "SystemDisksOverview": {
                    "TotalCount": 101
                }
            },
            {
                "DataDisksOverview": {
                    "ExpiringCount": 2,
                    "ShutdownCount": 0,
                    "TotalCount": 2
                },
                "ErrorCode": "",
                "Region": "ap-jakarta",
                "SystemDisksOverview": {
                    "TotalCount": 1
                }
            },
            {
                "DataDisksOverview": {
                    "ExpiringCount": 1,
                    "ShutdownCount": 0,
                    "TotalCount": 3
                },
                "ErrorCode": "",
                "Region": "sa-saopaulo",
                "SystemDisksOverview": {
                    "TotalCount": 0
                }
            }
        ],
        "RequestId": "10264b2f-6998-4e43-9e1d-bd3b06e5a0ce"
    }
}
```


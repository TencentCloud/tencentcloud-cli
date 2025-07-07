**Example 1: 租户日志存储统计**

租户日志存储统计

Input: 

```
tccli cfw DescribeLogStorageStatistic --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "ec88a398-f7cf-4cbb-9e23-6b49236dd0f6",
        "AclSize": 5521145584,
        "ArrearsStopWriting": 0,
        "IdsSize": 13442776032,
        "LeftSize": 925046202861,
        "NetFlowSize": 125879823723,
        "OperateSize": 3851875800,
        "PayMode": 1,
        "ReturnCode": 0,
        "ReturnMsg": "success",
        "StorageDay": 60,
        "TimeHistogram": [
            {
                "NetFlowSize": 232850065,
                "OperateSize": 59072400,
                "IdsSize": 584894,
                "AclSize": 22095186,
                "Time": "2024-10-25 00:00:00"
            },
            {
                "NetFlowSize": 226512606,
                "OperateSize": 1822500,
                "IdsSize": 308073,
                "AclSize": 56409259,
                "Time": "2024-10-26 00:00:00"
            },
            {
                "NetFlowSize": 312016348,
                "OperateSize": 1591200,
                "IdsSize": 1136827,
                "AclSize": 89038893,
                "Time": "2024-10-27 00:00:00"
            },
            {
                "NetFlowSize": 263122695,
                "OperateSize": 1791000,
                "IdsSize": 1633817,
                "AclSize": 112221690,
                "Time": "2024-10-28 00:00:00"
            },
            {
                "NetFlowSize": 314737760,
                "OperateSize": 4045500,
                "IdsSize": 11400888,
                "AclSize": 58205747,
                "Time": "2024-10-29 00:00:00"
            },
            {
                "NetFlowSize": 1000469317,
                "OperateSize": 3949200,
                "IdsSize": 69040,
                "AclSize": 51893,
                "Time": "2024-10-30 00:00:00"
            },
            {
                "NetFlowSize": 17837072505,
                "OperateSize": 1984500,
                "IdsSize": 5723094,
                "AclSize": 4378551511,
                "Time": "2024-10-31 00:00:00"
            }
        ],
        "TimeHistogramShow": {
            "StorageType": [
                "访问控制日志",
                "入侵防御日志",
                "流量日志",
                "操作日志"
            ],
            "Dates": [
                "10-25",
                "10-26",
                "10-27",
                "10-28",
                "10-29",
                "10-30",
                "10-31"
            ],
            "Data": [
                {
                    "List": [
                        22095186,
                        56409259,
                        89038893,
                        112221690,
                        58205747,
                        51893,
                        4378551511
                    ]
                },
                {
                    "List": [
                        584894,
                        308073,
                        1136827,
                        1633817,
                        11400888,
                        69040,
                        5723094
                    ]
                },
                {
                    "List": [
                        232850065,
                        226512606,
                        312016348,
                        263122695,
                        314737760,
                        1000469317,
                        17837072505
                    ]
                },
                {
                    "List": [
                        59072400,
                        1822500,
                        1591200,
                        1791000,
                        4045500,
                        3949200,
                        1984500
                    ]
                }
            ]
        },
        "TotalSize": 1073741824000,
        "UsedSize": 148695621139
    }
}
```


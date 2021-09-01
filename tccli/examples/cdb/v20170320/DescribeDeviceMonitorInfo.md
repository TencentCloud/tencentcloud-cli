**Example 1: 获取实例所在物理机的监控信息**



Input: 

```
tccli cdb DescribeDeviceMonitorInfo --cli-unfold-argument  \
    --InstanceId cdb-uns231ns \
    --Count 2
```

Output: 
```
{
    "Response": {
        "Cpu": {
            "Load": [
                174,
                169
            ],
            "Rate": [
                {
                    "CpuCore": 0,
                    "Rate": [
                        4,
                        5
                    ]
                },
                {
                    "CpuCore": 0,
                    "Rate": [
                        7,
                        7
                    ]
                },
                {
                    "CpuCore": 1,
                    "Rate": [
                        15,
                        7
                    ]
                },
                {
                    "CpuCore": 2,
                    "Rate": [
                        7,
                        7
                    ]
                },
                {
                    "CpuCore": 3,
                    "Rate": [
                        6,
                        5
                    ]
                },
                {
                    "CpuCore": 4,
                    "Rate": [
                        4,
                        2
                    ]
                },
                {
                    "CpuCore": 5,
                    "Rate": [
                        4,
                        5
                    ]
                },
                {
                    "CpuCore": 6,
                    "Rate": [
                        7,
                        5
                    ]
                },
                {
                    "CpuCore": 7,
                    "Rate": [
                        7,
                        9
                    ]
                },
                {
                    "CpuCore": 8,
                    "Rate": [
                        8,
                        8
                    ]
                },
                {
                    "CpuCore": 9,
                    "Rate": [
                        6,
                        4
                    ]
                },
                {
                    "CpuCore": 10,
                    "Rate": [
                        4,
                        14
                    ]
                },
                {
                    "CpuCore": 11,
                    "Rate": [
                        2,
                        2
                    ]
                },
                {
                    "CpuCore": 12,
                    "Rate": [
                        6,
                        3
                    ]
                },
                {
                    "CpuCore": 13,
                    "Rate": [
                        10,
                        14
                    ]
                },
                {
                    "CpuCore": 14,
                    "Rate": [
                        12,
                        6
                    ]
                },
                {
                    "CpuCore": 15,
                    "Rate": [
                        5,
                        2
                    ]
                },
                {
                    "CpuCore": 16,
                    "Rate": [
                        4,
                        2
                    ]
                },
                {
                    "CpuCore": 17,
                    "Rate": [
                        2,
                        4
                    ]
                },
                {
                    "CpuCore": 18,
                    "Rate": [
                        4,
                        6
                    ]
                },
                {
                    "CpuCore": 19,
                    "Rate": [
                        14,
                        9
                    ]
                },
                {
                    "CpuCore": 20,
                    "Rate": [
                        6,
                        6
                    ]
                },
                {
                    "CpuCore": 21,
                    "Rate": [
                        5,
                        5
                    ]
                },
                {
                    "CpuCore": 22,
                    "Rate": [
                        3,
                        12
                    ]
                },
                {
                    "CpuCore": 23,
                    "Rate": [
                        2,
                        2
                    ]
                }
            ]
        },
        "Mem": {
            "Total": [
                65716676,
                65716676
            ],
            "Used": [
                57163160,
                57158148
            ]
        },
        "Net": {
            "Conn": [
                133,
                130
            ],
            "PackageIn": [
                960,
                960
            ],
            "PackageOut": [],
            "FlowIn": [
                150,
                112
            ],
            "FlowOut": [
                1342,
                1260
            ]
        },
        "Disk": {
            "CapacityRatio": [
                5433344,
                49153024,
                0,
                40931328,
                1024,
                40946688,
                272384,
                40945664,
                0,
                40945664,
                123813888,
                195940352,
                12439552,
                587817984
            ],
            "Read": [
                0,
                0
            ],
            "Write": [
                740,
                797
            ],
            "IoRatioPerSec": [
                0,
                0
            ],
            "IoWaitTime": [
                61,
                65
            ]
        },
        "RequestId": "85b295bb-8f43-ce01-e35f-5a02e2beeeac"
    }
}
```


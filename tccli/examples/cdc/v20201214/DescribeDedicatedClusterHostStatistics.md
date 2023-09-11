**Example 1: 查询专用集群内宿主机的信息**

查询专用集群内宿主机的信息

Input: 

```
tccli cdc DescribeDedicatedClusterHostStatistics --cli-unfold-argument  \
    --DedicatedClusterId cluster-gbo27yc4
```

Output: 
```
{
    "Response": {
        "HostStatisticSet": [
            {
                "HostType": "S5.21XLARGE320",
                "HostFamily": "S5",
                "Cpu": 84,
                "Memory": 320,
                "Count": 240,
                "CpuAverage": 50,
                "MemAverage": 50,
                "NetAverage": 100,
                "CpuDetailData": {
                    "Timestamps": [
                        1693274400
                    ],
                    "Values": [
                        0
                    ]
                },
                "MemDetailData": {
                    "Timestamps": [
                        1693274400
                    ],
                    "Values": [
                        0
                    ]
                },
                "NetRateDetailData": {
                    "Timestamps": [
                        1693274400
                    ],
                    "Values": [
                        0
                    ]
                },
                "NetPacketDetailData": {
                    "Timestamps": [
                        1693274400
                    ],
                    "Values": [
                        0
                    ]
                }
            }
        ],
        "RequestId": "41aa48c2-477b-43c0-9d93-04ef3f529e5f"
    }
}
```


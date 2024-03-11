**Example 1: 查询本地专用集群云硬盘信息**

查询本地专用集群云硬盘信息

Input: 

```
tccli cdc DescribeDedicatedClusterCbsStatistics --cli-unfold-argument  \
    --DedicatedClusterId cluster-gbo27yc4
```

Output: 
```
{
    "Response": {
        "SetList": [
            {
                "SetId": "set-xxxxxxxxx",
                "SetName": "set1",
                "SetType": "ssd",
                "SetSize": 40,
                "SetStatus": "RUNNING",
                "CreateTime": "2023-01-01 12:00:00",
                "ReadTraffic": {
                    "Timestamps": [
                        0
                    ],
                    "Values": [
                        0
                    ]
                },
                "WriteTraffic": {
                    "Timestamps": [
                        0
                    ],
                    "Values": [
                        0
                    ]
                },
                "ReadIO": {
                    "Timestamps": [
                        0
                    ],
                    "Values": [
                        0
                    ]
                }
            }
        ],
        "TotalCount": 1,
        "RequestId": "abc"
    }
}
```


**Example 1: 获取执行机指标**



Input: 

```
tccli wedata GetResourceGroupMetrics --cli-unfold-argument  \
    --ResourceGroupId 20240401132517098618 \
    --StartTime None \
    --EndTime None \
    --MetricType None \
    --Granularity None
```

Output: 
```
{
    "Response": {
        "Data": {
            "CpuNum": null,
            "DiskVolume": null,
            "LifeCycle": 0,
            "MaximumConcurrency": null,
            "MemSize": 0,
            "MetricSnapshots": [
                {
                    "MetricName": "CpuCoreUsage",
                    "SnapshotValue": 0,
                    "TrendList": [
                        {
                            "Timestamp": 1757392500000,
                            "Value": 0
                        },
                        {
                            "Timestamp": 1757392800000,
                            "Value": 0
                        },
                        {
                            "Timestamp": 1757393100000,
                            "Value": 0
                        },
                        {
                            "Timestamp": 1757393400000,
                            "Value": 0
                        },
                        {
                            "Timestamp": 1757393700000,
                            "Value": 0
                        },
                        {
                            "Timestamp": 1757394000000,
                            "Value": 0
                        },
                        {
                            "Timestamp": 1757394300000,
                            "Value": 0
                        },
                        {
                            "Timestamp": 1757394600000,
                            "Value": 0
                        },
                        {
                            "Timestamp": 1757394900000,
                            "Value": 0
                        },
                        {
                            "Timestamp": 1757395200000,
                            "Value": 0
                        },
                        {
                            "Timestamp": 1757395500000,
                            "Value": 0
                        },
                        {
                            "Timestamp": 1757395800000,
                            "Value": 0
                        }
                    ]
                },
                {
                    "MetricName": "MemoryLoad",
                    "SnapshotValue": 0,
                    "TrendList": []
                },
                {
                    "MetricName": "CpuLoad",
                    "SnapshotValue": 0,
                    "TrendList": []
                },
                {
                    "MetricName": "DiskUsage",
                    "SnapshotValue": 0,
                    "TrendList": [
                        {
                            "Timestamp": 1757392500000,
                            "Value": 0
                        },
                        {
                            "Timestamp": 1757392800000,
                            "Value": 0
                        },
                        {
                            "Timestamp": 1757393100000,
                            "Value": 0
                        },
                        {
                            "Timestamp": 1757393400000,
                            "Value": 0
                        },
                        {
                            "Timestamp": 1757393700000,
                            "Value": 0
                        },
                        {
                            "Timestamp": 1757394000000,
                            "Value": 0
                        },
                        {
                            "Timestamp": 1757394300000,
                            "Value": 0
                        },
                        {
                            "Timestamp": 1757394600000,
                            "Value": 0
                        },
                        {
                            "Timestamp": 1757394900000,
                            "Value": 0
                        },
                        {
                            "Timestamp": 1757395200000,
                            "Value": 0
                        },
                        {
                            "Timestamp": 1757395500000,
                            "Value": 0
                        },
                        {
                            "Timestamp": 1757395800000,
                            "Value": 0
                        }
                    ]
                },
                {
                    "MetricName": "MemoryUsage",
                    "SnapshotValue": 0,
                    "TrendList": [
                        {
                            "Timestamp": 1757392500000,
                            "Value": 0
                        },
                        {
                            "Timestamp": 1757392800000,
                            "Value": 0
                        },
                        {
                            "Timestamp": 1757393100000,
                            "Value": 0
                        },
                        {
                            "Timestamp": 1757393400000,
                            "Value": 0
                        },
                        {
                            "Timestamp": 1757393700000,
                            "Value": 0
                        },
                        {
                            "Timestamp": 1757394000000,
                            "Value": 0
                        },
                        {
                            "Timestamp": 1757394300000,
                            "Value": 0
                        },
                        {
                            "Timestamp": 1757394600000,
                            "Value": 0
                        },
                        {
                            "Timestamp": 1757394900000,
                            "Value": 0
                        },
                        {
                            "Timestamp": 1757395200000,
                            "Value": 0
                        },
                        {
                            "Timestamp": 1757395500000,
                            "Value": 0
                        },
                        {
                            "Timestamp": 1757395800000,
                            "Value": 0
                        }
                    ]
                },
                {
                    "MetricName": "DiskUsed",
                    "SnapshotValue": 0,
                    "TrendList": [
                        {
                            "Timestamp": 1757392500000,
                            "Value": 0
                        },
                        {
                            "Timestamp": 1757392800000,
                            "Value": 0
                        },
                        {
                            "Timestamp": 1757393100000,
                            "Value": 0
                        },
                        {
                            "Timestamp": 1757393400000,
                            "Value": 0
                        },
                        {
                            "Timestamp": 1757393700000,
                            "Value": 0
                        },
                        {
                            "Timestamp": 1757394000000,
                            "Value": 0
                        },
                        {
                            "Timestamp": 1757394300000,
                            "Value": 0
                        },
                        {
                            "Timestamp": 1757394600000,
                            "Value": 0
                        },
                        {
                            "Timestamp": 1757394900000,
                            "Value": 0
                        },
                        {
                            "Timestamp": 1757395200000,
                            "Value": 0
                        },
                        {
                            "Timestamp": 1757395500000,
                            "Value": 0
                        },
                        {
                            "Timestamp": 1757395800000,
                            "Value": 0
                        }
                    ]
                }
            ],
            "Status": 1
        },
        "RequestId": "550b8107-ad28-4b6d-b1dc-7de4a0d4adb4"
    }
}
```


**Example 1: 查看实例资源使用详情**



Input: 

```
tccli mariadb DescribeDBResourceUsageDetails --cli-unfold-argument  \
    --InstanceId tdsql-ige1a5k3 \
    --StartTime 2018-03-19 \
    --EndTime 2018-03-19
```

Output: 
```
{
    "Response": {
        "Slave1": {
            "MemAvailable": {
                "EndTime": "2020-09-22 00:00:00",
                "Data": [
                    1,
                    1,
                    1
                ],
                "StartTime": "2020-09-22 00:00:00"
            },
            "CpuUsageRate": {
                "EndTime": "2020-09-22 00:00:00",
                "Data": [
                    1,
                    1,
                    1
                ],
                "StartTime": "2020-09-22 00:00:00"
            },
            "BinlogDiskAvailable": {
                "EndTime": "2020-09-22 00:00:00",
                "Data": [
                    1,
                    1,
                    1
                ],
                "StartTime": "2020-09-22 00:00:00"
            },
            "DataDiskAvailable": {
                "EndTime": "2020-09-22 00:00:00",
                "Data": [
                    1,
                    1,
                    1
                ],
                "StartTime": "2020-09-22 00:00:00"
            }
        },
        "Master": {
            "MemAvailable": {
                "EndTime": "2020-09-22 00:00:00",
                "Data": [
                    1,
                    1,
                    1
                ],
                "StartTime": "2020-09-22 00:00:00"
            },
            "CpuUsageRate": {
                "EndTime": "2020-09-22 00:00:00",
                "Data": [
                    1,
                    1,
                    1
                ],
                "StartTime": "2020-09-22 00:00:00"
            },
            "BinlogDiskAvailable": {
                "EndTime": "2020-09-22 00:00:00",
                "Data": [
                    1,
                    1,
                    1
                ],
                "StartTime": "2020-09-22 00:00:00"
            },
            "DataDiskAvailable": {
                "EndTime": "2020-09-22 00:00:00",
                "Data": [
                    1,
                    1,
                    1
                ],
                "StartTime": "2020-09-22 00:00:00"
            }
        },
        "RequestId": "xx",
        "Slave2": {
            "MemAvailable": {
                "EndTime": "2020-09-22 00:00:00",
                "Data": [
                    0.0
                ],
                "StartTime": "2020-09-22 00:00:00"
            },
            "CpuUsageRate": {
                "EndTime": "2020-09-22 00:00:00",
                "Data": [
                    0.0
                ],
                "StartTime": "2020-09-22 00:00:00"
            },
            "BinlogDiskAvailable": {
                "EndTime": "2020-09-22 00:00:00",
                "Data": [
                    0.0
                ],
                "StartTime": "2020-09-22 00:00:00"
            },
            "DataDiskAvailable": {
                "EndTime": "2020-09-22 00:00:00",
                "Data": [
                    0.0
                ],
                "StartTime": "2020-09-22 00:00:00"
            }
        }
    }
}
```


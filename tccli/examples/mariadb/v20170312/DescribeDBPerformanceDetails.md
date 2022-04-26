**Example 1: 查看实例性能数据详情**



Input: 

```
tccli mariadb DescribeDBPerformanceDetails --cli-unfold-argument  \
    --InstanceId tdsql-ige1a5k3 \
    --StartTime 2018-03-19 \
    --EndTime 2018-03-19
```

Output: 
```
{
    "Response": {
        "Slave1": {
            "UpdateTotal": {
                "EndTime": "2020-09-22 00:00:00",
                "Data": [
                    0.0
                ],
                "StartTime": "2020-09-22 00:00:00"
            },
            "DiskIops": {
                "EndTime": "2020-09-22 00:00:00",
                "Data": [
                    0.0
                ],
                "StartTime": "2020-09-22 00:00:00"
            },
            "ConnActive": {
                "EndTime": "2020-09-22 00:00:00",
                "Data": [
                    0.0
                ],
                "StartTime": "2020-09-22 00:00:00"
            },
            "MemHitRate": {
                "EndTime": "2020-09-22 00:00:00",
                "Data": [
                    0.0
                ],
                "StartTime": "2020-09-22 00:00:00"
            },
            "SlaveDelay": {
                "EndTime": "2020-09-22 00:00:00",
                "Data": [
                    0.0
                ],
                "StartTime": "2020-09-22 00:00:00"
            },
            "SelectTotal": {
                "EndTime": "2020-09-22 00:00:00",
                "Data": [
                    0.0
                ],
                "StartTime": "2020-09-22 00:00:00"
            },
            "LongQuery": {
                "EndTime": "2020-09-22 00:00:00",
                "Data": [
                    1,
                    1,
                    1
                ],
                "StartTime": "2020-09-22 00:00:00"
            },
            "DeleteTotal": {
                "EndTime": "2020-09-22 00:00:00",
                "Data": [
                    0.0
                ],
                "StartTime": "2020-09-22 00:00:00"
            },
            "InsertTotal": {
                "EndTime": "2020-09-22 00:00:00",
                "Data": [
                    0.0
                ],
                "StartTime": "2020-09-22 00:00:00"
            },
            "IsMasterSwitched": {
                "EndTime": "2020-09-22 00:00:00",
                "Data": [
                    0.0
                ],
                "StartTime": "2020-09-22 00:00:00"
            }
        },
        "Master": {
            "UpdateTotal": {
                "EndTime": "2020-09-22 00:00:00",
                "Data": [
                    0.0
                ],
                "StartTime": "2020-09-22 00:00:00"
            },
            "DiskIops": {
                "EndTime": "2020-09-22 00:00:00",
                "Data": [
                    0.0
                ],
                "StartTime": "2020-09-22 00:00:00"
            },
            "ConnActive": {
                "EndTime": "2020-09-22 00:00:00",
                "Data": [
                    0.0
                ],
                "StartTime": "2020-09-22 00:00:00"
            },
            "MemHitRate": {
                "EndTime": "2020-09-22 00:00:00",
                "Data": [
                    0.0
                ],
                "StartTime": "2020-09-22 00:00:00"
            },
            "SlaveDelay": {
                "EndTime": "2020-09-22 00:00:00",
                "Data": [
                    0.0
                ],
                "StartTime": "2020-09-22 00:00:00"
            },
            "SelectTotal": {
                "EndTime": "2020-09-22 00:00:00",
                "Data": [
                    0.0
                ],
                "StartTime": "2020-09-22 00:00:00"
            },
            "LongQuery": {
                "EndTime": "2020-09-22 00:00:00",
                "Data": [
                    1,
                    1,
                    1
                ],
                "StartTime": "2020-09-22 00:00:00"
            },
            "DeleteTotal": {
                "EndTime": "2020-09-22 00:00:00",
                "Data": [
                    0.0
                ],
                "StartTime": "2020-09-22 00:00:00"
            },
            "InsertTotal": {
                "EndTime": "2020-09-22 00:00:00",
                "Data": [
                    0.0
                ],
                "StartTime": "2020-09-22 00:00:00"
            },
            "IsMasterSwitched": {
                "EndTime": "2020-09-22 00:00:00",
                "Data": [
                    0.0
                ],
                "StartTime": "2020-09-22 00:00:00"
            }
        },
        "RequestId": "xx",
        "Slave2": {
            "UpdateTotal": {
                "EndTime": "2020-09-22 00:00:00",
                "Data": [
                    0.0
                ],
                "StartTime": "2020-09-22 00:00:00"
            },
            "DiskIops": {
                "EndTime": "2020-09-22 00:00:00",
                "Data": [
                    0.0
                ],
                "StartTime": "2020-09-22 00:00:00"
            },
            "ConnActive": {
                "EndTime": "2020-09-22 00:00:00",
                "Data": [
                    0.0
                ],
                "StartTime": "2020-09-22 00:00:00"
            },
            "MemHitRate": {
                "EndTime": "2020-09-22 00:00:00",
                "Data": [
                    0.0
                ],
                "StartTime": "2020-09-22 00:00:00"
            },
            "SlaveDelay": {
                "EndTime": "2020-09-22 00:00:00",
                "Data": [
                    0.0
                ],
                "StartTime": "2020-09-22 00:00:00"
            },
            "SelectTotal": {
                "EndTime": "2020-09-22 00:00:00",
                "Data": [
                    0.0
                ],
                "StartTime": "2020-09-22 00:00:00"
            },
            "LongQuery": {
                "EndTime": "2020-09-22 00:00:00",
                "Data": [
                    1,
                    1,
                    1
                ],
                "StartTime": "2020-09-22 00:00:00"
            },
            "DeleteTotal": {
                "EndTime": "2020-09-22 00:00:00",
                "Data": [
                    0.0
                ],
                "StartTime": "2020-09-22 00:00:00"
            },
            "InsertTotal": {
                "EndTime": "2020-09-22 00:00:00",
                "Data": [
                    0.0
                ],
                "StartTime": "2020-09-22 00:00:00"
            },
            "IsMasterSwitched": {
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


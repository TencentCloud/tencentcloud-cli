**Example 1: Viewing instance resource usage details**



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
            "BinlogDiskAvailable": {
                "EndTime": "2018-03-24 23:59:59",
                "Data": [
                    1,
                    1,
                    1
                ],
                "StartTime": "2018-03-24 00:00:00"
            },
            "CpuUsageRate": {
                "EndTime": "2018-03-24 23:59:59",
                "Data": [
                    1,
                    1,
                    1
                ],
                "StartTime": "2018-03-24 00:00:00"
            },
            "MemAvailable": {
                "EndTime": "2018-03-24 23:59:59",
                "Data": [
                    1,
                    1,
                    1
                ],
                "StartTime": "2018-03-24 00:00:00"
            },
            "MemHitRate": {
                "EndTime": "2018-03-24 23:59:59",
                "Data": [
                    1,
                    1,
                    1
                ],
                "StartTime": "2018-03-24 00:00:00"
            },
            "DataDiskAvailable": {
                "EndTime": "2018-03-24 23:59:59",
                "Data": [
                    1,
                    1,
                    1
                ],
                "StartTime": "2018-03-24 00:00:00"
            }
        },
        "Master": {
            "BinlogDiskAvailable": {
                "EndTime": "2018-03-24 23:59:59",
                "Data": [
                    1,
                    1,
                    1
                ],
                "StartTime": "2018-03-24 00:00:00"
            },
            "CpuUsageRate": {
                "EndTime": "2018-03-24 23:59:59",
                "Data": [
                    1,
                    1,
                    1
                ],
                "StartTime": "2018-03-24 00:00:00"
            },
            "MemAvailable": {
                "EndTime": "2018-03-24 23:59:59",
                "Data": [
                    1,
                    1,
                    1
                ],
                "StartTime": "2018-03-24 00:00:00"
            },
            "MemHitRate": {
                "EndTime": "2018-03-24 23:59:59",
                "Data": [
                    1,
                    1,
                    1
                ],
                "StartTime": "2018-03-24 00:00:00"
            },
            "DataDiskAvailable": {
                "EndTime": "2018-03-24 23:59:59",
                "Data": [
                    1,
                    1,
                    1
                ],
                "StartTime": "2018-03-24 00:00:00"
            }
        },
        "RequestId": "6ce468ba-206a-4ad1-a1e6-7f2194657649"
    }
}
```


**Example 1: 查看实例资源使用情况**



Input: 

```
tccli mariadb DescribeDBResourceUsage --cli-unfold-argument  \
    --InstanceId tdsql-ige1a5k3 \
    --StartTime 2018-03-19 \
    --EndTime 2018-03-19
```

Output: 
```
{
    "Response": {
        "MemAvailable": {
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
        "RequestId": "32a93b23-cbd8-48a9-a75a-2274625099ca",
        "BinlogDiskAvailable": {
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
    }
}
```


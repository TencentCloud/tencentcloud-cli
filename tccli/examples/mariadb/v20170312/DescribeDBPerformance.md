**Example 1: 查看实例性能数据**



Input: 

```
tccli mariadb DescribeDBPerformance --cli-unfold-argument  \
    --InstanceId tdsql-ige1a5k3 \
    --StartTime 2018-03-19 \
    --EndTime 2018-03-19
```

Output: 
```
{
    "Response": {
        "UpdateTotal": {
            "EndTime": "2018-03-24 23:59:59",
            "Data": [
                1,
                1,
                1
            ],
            "StartTime": "2018-03-24 00:00:00"
        },
        "DiskIops": {
            "EndTime": "2018-03-24 23:59:59",
            "Data": [
                1,
                1,
                1
            ],
            "StartTime": "2018-03-24 00:00:00"
        },
        "ConnActive": {
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
        "SelectTotal": {
            "EndTime": "2018-03-24 23:59:59",
            "Data": [
                1,
                1,
                1
            ],
            "StartTime": "2018-03-24 00:00:00"
        },
        "LongQuery": {
            "EndTime": "2018-03-24 23:59:59",
            "Data": [
                1,
                1,
                1
            ],
            "StartTime": "2018-03-24 00:00:00"
        },
        "DeleteTotal": {
            "EndTime": "2018-03-24 23:59:59",
            "Data": [
                1,
                1,
                1
            ],
            "StartTime": "2018-03-24 00:00:00"
        },
        "InsertTotal": {
            "EndTime": "2018-03-24 23:59:59",
            "Data": [
                1,
                1,
                1
            ],
            "StartTime": "2018-03-24 00:00:00"
        },
        "RequestId": "124581ec-1937-4847-bdea-1a2949e4af9b",
        "IsMasterSwitched": {
            "EndTime": "2018-03-24 23:59:59",
            "Data": [
                1,
                1,
                1
            ],
            "StartTime": "2018-03-24 00:00:00"
        },
        "SlaveDelay": {
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


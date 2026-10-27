**Example 1: 查询实例磁盘分区数据**



Input: 

```
tccli cvd DescribeInstanceGraphData --cli-unfold-argument  \
    --InstanceId cdi-l0c69nmim85j8t1 \
    --StartTime 2025-06-16T16:10:39+08:00 \
    --EndTime 2025-06-16T17:10:39+08:00
```

Output: 
```
{
    "Response": {
        "EndTime": "2025-06-16T17:10:39+08:00",
        "MetricName": "disk_usage",
        "Partitions": [
            {
                "Name": "vda2",
                "Total": 49.11,
                "Usage": 16.15
            }
        ],
        "Period": 0,
        "RequestId": "825576a2-9356-444c-b15c-35e1b5a02c81",
        "StartTime": "2025-06-16T16:10:39+08:00"
    }
}
```


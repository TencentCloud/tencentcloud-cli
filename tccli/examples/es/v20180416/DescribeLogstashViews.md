**Example 1: 查询Logstash集群视图**



Input: 

```
tccli es DescribeLogstashViews --cli-unfold-argument  \
    --LogstashInstanceId test2
```

Output: 
```
{
    "Response": {
        "NodesView": [
            {
                "NodeId": "test1",
                "NodeIp": "test1",
                "NodeHttpIp": "st",
                "Zone": "test1",
                "DiskSize": 0,
                "DiskUsage": 0,
                "MemSize": 0,
                "MemUsage": 0,
                "JvmMemUsage": 0,
                "CpuNum": 0,
                "CpuUsage": 0
            }
        ],
        "RequestId": "test1"
    }
}
```


**Example 1: 查询集群视图**



Input: 

```
tccli es DescribeViews --cli-unfold-argument  \
    --InstanceId es-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "NodesView": [
            {
                "CpuNum": 0,
                "MemUsage": 0.0,
                "NodeId": "xx",
                "CpuUsage": 0.0,
                "Break": 0.0,
                "Visible": 0.0,
                "DiskSize": 0,
                "MemSize": 0,
                "NodeIp": "xx",
                "DiskUsage": 0.0
            }
        ],
        "ClusterView": {
            "TargetNodeTypes": [
                "xx"
            ],
            "AvgCpuUsage": 0.0,
            "AvgMemUsage": 0.0,
            "Break": 0.0,
            "Visible": 0.0,
            "AvgDiskUsage": 0.0,
            "Health": 0.0,
            "TotalDiskSize": 1
        },
        "RequestId": "xx",
        "KibanasView": [
            {
                "MemUsage": 0.0,
                "Ip": "xx",
                "CpuUsage": 0.0,
                "CpuNum": 0,
                "DiskSize": 0,
                "MemSize": 0,
                "DiskUsage": 0.0
            }
        ]
    }
}
```


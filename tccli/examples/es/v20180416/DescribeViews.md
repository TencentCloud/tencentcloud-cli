**Example 1: 查询集群视图**

查询集群视图

Input: 

```
tccli es DescribeViews --cli-unfold-argument  \
    --InstanceId es-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "ClusterView": {
            "Health": 0,
            "Visible": 0,
            "Break": 0,
            "AvgDiskUsage": 0,
            "AvgMemUsage": 0,
            "AvgCpuUsage": 0,
            "TotalDiskSize": 1,
            "TargetNodeTypes": [
                "abc"
            ],
            "NodeNum": 0,
            "TotalNodeNum": 0,
            "DataNodeNum": 0,
            "IndexNum": 0,
            "DocNum": 0,
            "DiskUsedInBytes": 0,
            "ShardNum": 0,
            "PrimaryShardNum": 0,
            "RelocatingShardNum": 0,
            "InitializingShardNum": 0,
            "UnassignedShardNum": 0,
            "TotalCosStorage": 0,
            "SearchableSnapshotCosBucket": "abc",
            "SearchableSnapshotCosAppId": "abc"
        },
        "NodesView": [
            {
                "NodeId": "abc",
                "NodeIp": "abc",
                "Visible": 0,
                "Break": 0,
                "DiskSize": 0,
                "DiskUsage": 0,
                "MemSize": 0,
                "MemUsage": 0,
                "CpuNum": 0,
                "CpuUsage": 0,
                "Zone": "abc",
                "NodeRole": "abc",
                "NodeHttpIp": "abc",
                "JvmMemUsage": 0,
                "ShardNum": 0,
                "DiskIds": [
                    "abc"
                ],
                "Hidden": true,
                "IsCoordinationNode": true
            }
        ],
        "KibanasView": [
            {
                "Ip": "abc",
                "DiskSize": 0,
                "DiskUsage": 0,
                "MemSize": 0,
                "MemUsage": 0,
                "CpuNum": 0,
                "CpuUsage": 0,
                "Zone": "abc",
                "NodeId": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```


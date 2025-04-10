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
        "RequestId": "6127baed-bc4c-4c0d-b52d-6463a722795b",
        "ClusterView": {
            "Health": 0,
            "NodeNum": 3,
            "TotalNodeNum": 3,
            "DataNodeNum": 3,
            "IndexNum": 121,
            "DocNum": 68195345,
            "DiskUsedInBytes": 27909384217,
            "ShardNum": 1033,
            "PrimaryShardNum": 516,
            "RelocatingShardNum": 0,
            "InitializingShardNum": 0,
            "UnassignedShardNum": 0,
            "Visible": 1,
            "Break": 0,
            "AvgDiskUsage": 0.075802238966579,
            "AvgMemUsage": 0.82355177962355,
            "AvgCpuUsage": 0.0097774027927309,
            "TotalDiskSize": 600,
            "TotalCosStorage": 0,
            "SearchableSnapshotCosBucket": "",
            "SearchableSnapshotCosAppId": "",
            "TargetNodeTypes": [
                "data"
            ]
        },
        "NodesView": [
            {
                "NodeId": "1739331190000739932",
                "NodeIp": "9.29.48.61",
                "NodeHttpIp": "9.29.48.61",
                "Zone": "ap-hongkong-3",
                "Hidden": false,
                "NodeRole": "hotData",
                "Visible": 1,
                "Break": 0,
                "DiskSize": 200,
                "DiskUsage": 0.075739699850416,
                "MemSize": 8,
                "MemUsage": 0.82319480451571,
                "JvmMemUsage": 0.6,
                "CpuNum": 4,
                "CpuUsage": 0.0048451231329569,
                "ShardNum": 345,
                "DiskIds": [
                    "disk-6eur8xxx"
                ],
                "IsCoordinationNode": true,
                "CVMStatus": "RUNNING",
                "CVMDisasterRecoverGroupId": "",
                "CVMDisasterRecoverGroupStatus": 0
            },
            {
                "NodeId": "1739331190000740032",
                "NodeIp": "9.29.50.27",
                "NodeHttpIp": "9.29.50.27",
                "Zone": "ap-hongkong-3",
                "Hidden": false,
                "NodeRole": "hotData",
                "Visible": 1,
                "Break": 0,
                "DiskSize": 200,
                "DiskUsage": 0.076343043587719,
                "MemSize": 8,
                "MemUsage": 0.82361871962329,
                "JvmMemUsage": 0.34,
                "CpuNum": 4,
                "CpuUsage": 0.0048869730840559,
                "ShardNum": 344,
                "DiskIds": [
                    "disk-0pwecycm"
                ],
                "IsCoordinationNode": true,
                "CVMStatus": "RUNNING",
                "CVMDisasterRecoverGroupId": "",
                "CVMDisasterRecoverGroupStatus": 0
            },
            {
                "NodeId": "1739331190000739832",
                "NodeIp": "9.29.51.17",
                "NodeHttpIp": "9.29.51.17",
                "Zone": "ap-hongkong-3",
                "Hidden": false,
                "NodeRole": "hotData",
                "Visible": 1,
                "Break": 0,
                "DiskSize": 200,
                "DiskUsage": 0.07533630210082,
                "MemSize": 8,
                "MemUsage": 0.8215642493271,
                "JvmMemUsage": 0.62,
                "CpuNum": 4,
                "CpuUsage": 0.0041350619841615,
                "ShardNum": 344,
                "DiskIds": [
                    "disk-2xtqdaju"
                ],
                "IsCoordinationNode": true,
                "CVMStatus": "RUNNING",
                "CVMDisasterRecoverGroupId": "",
                "CVMDisasterRecoverGroupStatus": 0
            }
        ],
        "KibanasView": [
            {
                "Ip": "9.29.49.38",
                "NodeId": "1739331190000739832",
                "Zone": "ap-hongkong-3",
                "DiskSize": 50,
                "DiskUsage": 0.19899999999999998,
                "MemSize": 2,
                "MemUsage": 0.76055485347424,
                "CpuNum": 1,
                "CpuUsage": 0.029833333333333
            }
        ]
    }
}
```


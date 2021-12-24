**Example 1: 查询边缘单元Pod**



Input: 

```
tccli iecp DescribeEdgePod --cli-unfold-argument  \
    --EdgeUnitId 1 \
    --Name aaa-apex \
    --Namespace default
```

Output: 
```
{
    "Response": {
        "RequestId": "cfcaee48-cac8-43e0-8dfe-fa3d5a38809f",
        "Pod": {
            "Name": "aaa-apex",
            "Status": "Running",
            "NodeIp": "10.0.0.0",
            "Ip": "172.0.0.1",
            "CpuRequest": "250m",
            "MemoryRequest": "256Mi",
            "Namespace": "default",
            "WorkloadType": "ReplicaSet",
            "WorkloadName": "aaa-apex",
            "StartTime": "2021-01-01 00:00:00",
            "RestartCount": 0,
            "ClusterID": "cls-xxxxxx"
        }
    }
}
```


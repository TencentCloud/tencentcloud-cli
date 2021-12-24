**Example 1: 查询节点Pod列表**



Input: 

```
tccli iecp DescribeEdgeNodePods --cli-unfold-argument  \
    --EdgeUnitId 1 \
    --NodeId 1 \
    --Namespace default
```

Output: 
```
{
    "Response": {
        "RequestId": "5ebf13a2-f925-4ba7-adff-ddbc21d355e3",
        "PodSet": [
            {
                "Name": "aaa-aaa",
                "Status": "Running",
                "NodeIp": "1.2.3.4",
                "Ip": "1.2.3.5",
                "CpuRequest": "250m",
                "MemoryRequest": "512Mi",
                "WorkloadType": "Deployment",
                "WorkloadName": "aaa",
                "StartTime": "2020-01-01 00:00:00",
                "RestartCount": 0,
                "ClusterID": "cls-xxxxx"
            }
        ]
    }
}
```


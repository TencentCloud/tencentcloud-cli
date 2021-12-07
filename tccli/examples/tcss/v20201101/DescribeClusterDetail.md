**Example 1: 查询单个集群的详细信息示例**



Input: 

```
tccli tcss DescribeClusterDetail --cli-unfold-argument  \
    --ClusterId cls-0zmsjvko
```

Output: 
```
{
    "Response": {
        "RequestId": "8a360c7e-22d3-421d-8cf9-f5f6af91a8d8",
        "ClusterId": "cls-0zmsjvko",
        "ClusterName": "wk独立集群",
        "ScanTaskProgress": 100,
        "ClusterVersion": "1.18.4",
        "ContainerRuntime": "docker",
        "ClusterNodeNum": 2,
        "ClusterStatus": "Running",
        "DefenderStatus": "Defender_Normal",
        "ClusterType": "INDEPENDENT_CLUSTER",
        "Region": "ap-guangzhou",
        "SeriousRiskCount": 1,
        "HighRiskCount": 5,
        "MiddleRiskCount": 8,
        "HintRiskCount": 4,
        "CheckStatus": "HasRisk",
        "TaskCreateTime": "2021-11-16 10:13:42"
    }
}
```


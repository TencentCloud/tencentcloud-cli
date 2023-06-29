**Example 1: 查询结果**



Input: 

```
tccli tcss DescribeUserCluster --cli-unfold-argument  \
    --Limit 2 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "a6405e01-bf4f-4044-abe9-4458783a3066",
        "TotalCount": 9,
        "ClusterInfoList": [
            {
                "ClusterId": "cls-0zmsjvko",
                "ClusterName": "wk独立集群",
                "ClusterVersion": "1.18.4",
                "ClusterOs": "tlinux2.4x86_64",
                "ClusterType": "INDEPENDENT_CLUSTER",
                "ClusterNodeNum": 2,
                "Region": "ap-guangzhou",
                "DefenderStatus": "Defender_Normal",
                "ClusterStatus": "Running",
                "ClusterCheckMode": "Cluster_Normal",
                "ClusterAutoCheck": true,
                "DefenderErrorReason": "",
                "UnreadyNodeNum": 0,
                "SeriousRiskCount": 1,
                "HighRiskCount": 5,
                "MiddleRiskCount": 8,
                "HintRiskCount": 4,
                "CheckFailReason": "",
                "CheckStatus": "HasRisk",
                "TaskCreateTime": "2021-11-16 02:01:36"
            },
            {
                "ClusterId": "cls-94d14s7x",
                "ClusterName": "jgl-独立",
                "ClusterVersion": "1.20.6",
                "ClusterOs": "tlinux2.4x86_64",
                "ClusterType": "INDEPENDENT_CLUSTER",
                "ClusterNodeNum": 2,
                "Region": "ap-beijing",
                "DefenderStatus": "Defender_Normal",
                "ClusterStatus": "Running",
                "ClusterCheckMode": "Cluster_Normal",
                "ClusterAutoCheck": false,
                "DefenderErrorReason": "",
                "UnreadyNodeNum": 0,
                "SeriousRiskCount": 0,
                "HighRiskCount": 1,
                "MiddleRiskCount": 7,
                "HintRiskCount": 3,
                "CheckFailReason": "",
                "CheckStatus": "HasRisk",
                "TaskCreateTime": "2021-11-15 11:57:24"
            }
        ]
    }
}
```


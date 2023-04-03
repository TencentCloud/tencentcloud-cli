**Example 1: 查询集群详情**

查询集群的详细信息

Input: 

```
tccli tcss DescribeClusterDetail --cli-unfold-argument  \
    --ClusterId b6ebf065d08563396da66bf0950cba8c
```

Output: 
```
{
    "Response": {
        "RequestId": "6c4a3216-1849-48d1-b02c-bb83801044b6",
        "ClusterId": "b6ebf065d08563396da66bf0950cba8c",
        "ClusterName": "wk-usercluster-test",
        "ScanTaskProgress": 0,
        "ClusterVersion": "v1.20.6-tke.12",
        "ContainerRuntime": "docker://19.3.9",
        "ClusterNodeNum": 4,
        "ClusterStatus": "Running",
        "DefenderStatus": "Defender_Normal",
        "ClusterType": "Kubernetes",
        "Region": "ap-guangzhou",
        "SeriousRiskCount": 0,
        "HighRiskCount": 0,
        "MiddleRiskCount": 0,
        "HintRiskCount": 0,
        "CheckStatus": "Task_Running",
        "TaskCreateTime": "2022-05-06 11:03:19",
        "NetworkType": "PublicNetwork",
        "ApiServerAddress": "https://xxxx:60002",
        "NodeCount": 4,
        "NamespaceCount": 0,
        "WorkloadCount": 0,
        "PodCount": 0,
        "ServiceCount": 0,
        "IngressCount": 0,
        "MasterIps": "127.0.0.1;127.0.0.2;"
    }
}
```


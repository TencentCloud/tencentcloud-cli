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
        "ApiServerAddress": "",
        "CheckStatus": "HasRisk",
        "ClusterId": "57153b3ea9483f46f5dd9a0052cad265",
        "ClusterName": "benben-tcss",
        "ClusterNodeNum": 1,
        "ClusterStatus": "CSR_RUNNING",
        "ClusterSubStatus": "",
        "ClusterType": "USER_CREATE_CLUSTER",
        "ClusterVersion": "v1.25.13",
        "ContainerRuntime": "docker://26.1.4",
        "DefenderStatus": "",
        "HighRiskCount": 8,
        "HintRiskCount": 3,
        "IngressCount": 0,
        "MasterIps": "172.16.64.12;",
        "MiddleRiskCount": 9,
        "NamespaceCount": 7,
        "NetworkType": "",
        "NodeCount": 1,
        "PodCount": 15,
        "Region": "ap-guangzhou",
        "RequestId": "7d65a8f8-2a92-4291-9e18-10a9d6a31382",
        "ScanTaskProgress": 100,
        "SeriousRiskCount": 0,
        "ServiceCount": 2,
        "TaskCreateTime": "2024-10-29 12:59:55",
        "WorkloadCount": 10
    }
}
```


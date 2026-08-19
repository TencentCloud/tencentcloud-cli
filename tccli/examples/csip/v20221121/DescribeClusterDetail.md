**Example 1: 调用示例**



Input: 

```
tccli csip DescribeClusterDetail --cli-unfold-argument  \
    --ClusterAssetId 86693c5bf9e9fbdce993d557b1038fd8
```

Output: 
```
{
    "Response": {
        "ClusterBaseInfo": {
            "AlarmEventCriticalCount": 0,
            "AlarmEventHighCount": 0,
            "AlarmEventLowCount": 0,
            "AlarmEventMiddleCount": 0,
            "AppID": 260083796,
            "AssetId": "86693c5bf9e9fbdce993d557b1038fd8",
            "AuditLogSwitchStatus": 0,
            "ClusterId": "cls-pde9e0s0",
            "ClusterName": "yancyw-标准集群",
            "ClusterType": "TKE_MANAGED_CLUSTER",
            "DefendCoresCount": 0,
            "DefendStatus": "AccessedInstalled",
            "FailMessage": "",
            "LastAssetSyncTime": "2026-03-18T07:31:26Z",
            "LastRiskCheckTime": "2026-03-18T08:20:20Z",
            "NodeCount": 0,
            "OfflineNodeCount": 0,
            "OwnerName": "",
            "Region": "ap-guangzhou",
            "RiskEventCriticalCount": 0,
            "RiskEventHighCount": 0,
            "RiskEventLowCount": 0,
            "RiskEventMiddleCount": 0,
            "RiskStatus": "failed",
            "RunStatus": "Running",
            "Tags": [],
            "TotalCoresCount": 0,
            "UninstallNodeCount": 0,
            "Version": "1.30.0"
        },
        "ContainerCount": 0,
        "ImageCount": 0,
        "IngressCount": 0,
        "MasterIP": "",
        "NamespaceCount": 7,
        "NodeCount": 0,
        "PodCount": 0,
        "RuntimeComponent": "containerd",
        "ServiceCount": 0,
        "RequestId": "7da09158-1246-473d-852d-0b873a7b0900"
    }
}
```


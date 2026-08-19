**Example 1: 调用示例**



Input: 

```
tccli csip DescribeClusterListV2 --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
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
                "FailMessage": "资产同步失败",
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
            }
        ],
        "TotalCount": 5,
        "RequestId": "cb1451b7-b9b9-4521-8097-e4c391b48ad7"
    }
}
```


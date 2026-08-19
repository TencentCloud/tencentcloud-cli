**Example 1: 示例**



Input: 

```
tccli csip DescribeClusterAssetList --cli-unfold-argument  \
    --MemberId mem-123abc
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "AccessFailedMessage": "roles.rbac.authorization.k8s.io \"tcss-admin\" is forbidden: unable to create new content in namespace tcss because it is being terminated",
                "AccessedStatus": "AccessedInstalled",
                "AccessedSubStatus": "AccessedSubNone",
                "AlarmEventCriticalCount": 0,
                "AlarmEventHighCount": 0,
                "AlarmEventLowCount": 0,
                "AlarmEventMiddleCount": 0,
                "AppID": 260083796,
                "AssetId": "",
                "AssetSyncStatus": "AssetCheckFinished",
                "AuditLogSwitchStatus": 0,
                "ClusterCaMD5": "814fe1612b3df5b197bf9129471e26ae",
                "ClusterId": "cls-pde9e0s0",
                "ClusterName": "yancyw-标准集群",
                "ClusterType": "TKE_MANAGED_CLUSTER",
                "DefendCoresCount": 0,
                "DefendStatus": "Disabled",
                "FailMessage": "",
                "LastAssetSyncTime": "2026-06-30T15:14:14Z",
                "LastRiskCheckTime": "1970-01-01T00:00:00Z",
                "NodeCount": 2,
                "OfflineNodeCount": 1,
                "OwnerName": "",
                "Region": "ap-guangzhou",
                "RiskConfigCount": 0,
                "RiskEventCriticalCount": 0,
                "RiskEventHighCount": 0,
                "RiskEventLowCount": 0,
                "RiskEventMiddleCount": 0,
                "RiskStatus": "undetect",
                "RunStatus": "Running",
                "RunSubStatus": "",
                "Tags": [],
                "TotalCoresCount": 0,
                "UninstallNodeCount": 1,
                "Version": "1.30.0"
            }
        ],
        "TotalCount": 7,
        "RequestId": "89d78276-5250-4875-acaa-020142801e9d"
    }
}
```


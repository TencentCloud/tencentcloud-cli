**Example 1: 查询配置发布历史**



Input: 

```
tccli tsf DescribeConfigReleaseLogs --cli-unfold-argument  \
    --GroupId group-zvwbbnxv \
    --ApplicationId application-ov6ml25a
```

Output: 
```
{
    "Response": {
        "RequestId": "6566f040-7ad3-4608-8be4-aa20e84cfdbf",
        "Result": {
            "Content": [
                {
                    "ClusterId": "cluster-jqv3mda7",
                    "ClusterName": "jolyonzheng-vm-cluster",
                    "ConfigId": "dcfg-nyg99e5a",
                    "ConfigName": "gw_opensource_api",
                    "ConfigReleaseLogId": "dcfgrl-4y4rxnba",
                    "ConfigVersion": "2",
                    "GroupId": "group-zvwbbnxv",
                    "GroupName": "group-msgw-mock1",
                    "LastConfigId": "dcfg-qv3rrn6v",
                    "LastConfigName": "gw_opensource_api",
                    "LastConfigVersion": "1",
                    "NamespaceId": "namespace-9ynzz64y",
                    "NamespaceName": "mock-service-ns",
                    "ReleaseDesc": "this is desc",
                    "ReleaseStatus": "RS",
                    "ReleaseTime": "2025-08-07 11:34:36",
                    "ReleasedConfigCenter": "SHARE",
                    "RollbackFlag": false
                },
                {
                    "ClusterId": "cluster-jqv3mda7",
                    "ClusterName": "jolyonzheng-vm-cluster",
                    "ConfigId": "dcfg-qv3rrn6v",
                    "ConfigName": "gw_opensource_api",
                    "ConfigReleaseLogId": "dcfgrl-qabpxw9v",
                    "ConfigVersion": "1",
                    "GroupId": "group-zvwbbnxv",
                    "GroupName": "group-msgw-mock1",
                    "LastConfigId": "dcfg-nyg99e5a",
                    "LastConfigName": "gw_opensource_api",
                    "LastConfigVersion": "2",
                    "NamespaceId": "namespace-9ynzz64y",
                    "NamespaceName": "mock-service-ns",
                    "ReleaseDesc": null,
                    "ReleaseStatus": "S",
                    "ReleaseTime": "2025-08-07 11:30:25",
                    "ReleasedConfigCenter": "SHARE",
                    "RollbackFlag": true
                },
                {
                    "ClusterId": "cluster-jqv3mda7",
                    "ClusterName": "jolyonzheng-vm-cluster",
                    "ConfigId": "dcfg-nyg99e5a",
                    "ConfigName": "gw_opensource_api",
                    "ConfigReleaseLogId": "dcfgrl-6yoxb8ny",
                    "ConfigVersion": "2",
                    "GroupId": "group-zvwbbnxv",
                    "GroupName": "group-msgw-mock1",
                    "LastConfigId": null,
                    "LastConfigName": null,
                    "LastConfigVersion": null,
                    "NamespaceId": "namespace-9ynzz64y",
                    "NamespaceName": "mock-service-ns",
                    "ReleaseDesc": null,
                    "ReleaseStatus": "S",
                    "ReleaseTime": "2024-11-28 17:01:08",
                    "ReleasedConfigCenter": "SHARE",
                    "RollbackFlag": false
                }
            ],
            "TotalCount": 3
        }
    }
}
```


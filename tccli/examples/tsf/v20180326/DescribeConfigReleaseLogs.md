**Example 1: 查询配置发布历史**



Input: 

```
tccli tsf DescribeConfigReleaseLogs --cli-unfold-argument  \
    --GroupId group-aln2284v \
    --Offset 0 \
    --Limit 10 \
    --NamespaceId namespace-vj3z3zgy \
    --ClusterId cluster-yne99jdy
```

Output: 
```
{
    "Response": {
        "RequestId": "66410802-5243-4b39-8823-21843a2bf669",
        "Result": {
            "Content": [
                {
                    "ClusterId": "cluster-yne99jdy",
                    "ClusterName": "cluster-app",
                    "ConfigId": "dcfg-yo82mmra",
                    "ConfigName": "app-config",
                    "ConfigReleaseLogId": "dcfgrl-yq75nn3a",
                    "ConfigVersion": "v3",
                    "GroupId": "group-aln2284v",
                    "GroupName": "group-provider-1",
                    "LastConfigId": "dcfg-yo82mmra",
                    "LastConfigName": "config_app",
                    "LastConfigVersion": "v1",
                    "NamespaceId": "namespace-vw8oox6v",
                    "NamespaceName": "cluster-jolyonzheng_default",
                    "ReleaseDesc": "This is desc",
                    "ReleaseStatus": "S",
                    "ReleaseTime": "2024-12-24 15:57:15",
                    "ReleasedConfigCenter": "SHARE",
                    "RollbackFlag": false
                }
            ],
            "TotalCount": 6
        }
    }
}
```


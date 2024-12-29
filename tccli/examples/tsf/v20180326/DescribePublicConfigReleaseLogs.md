**Example 1: 查询公共配置发布历史**



Input: 

```
tccli tsf DescribePublicConfigReleaseLogs --cli-unfold-argument  \
    --NamespaceId namespace-vj3z3zgy \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "168aec4c-c3fe-4abd-911b-ca9634e137dd",
        "Result": {
            "Content": [
                {
                    "ClusterId": null,
                    "ClusterName": null,
                    "ConfigId": "dcfg-p-vzk36rov",
                    "ConfigName": "[配置项已被删除]",
                    "ConfigReleaseLogId": "dcfgrl-yrm5jx9v",
                    "ConfigVersion": "[配置项已被删除]",
                    "GroupId": null,
                    "GroupName": null,
                    "LastConfigId": "dcfg-p-vzk36rov",
                    "LastConfigName": "[配置项已被删除]",
                    "LastConfigVersion": "[配置项已被删除]",
                    "NamespaceId": "namespace-vj3z3zgy",
                    "NamespaceName": "ns_default",
                    "ReleaseDesc": "删除配置项",
                    "ReleaseStatus": "DS",
                    "ReleaseTime": "2024-12-24 20:30:37",
                    "RollbackFlag": false
                },
                {
                    "ClusterId": null,
                    "ClusterName": null,
                    "ConfigId": "dcfg-p-vzk36rov",
                    "ConfigName": "[配置项已被删除]",
                    "ConfigReleaseLogId": "dcfgrl-vw83po6v",
                    "ConfigVersion": "[配置项已被删除]",
                    "GroupId": null,
                    "GroupName": null,
                    "LastConfigId": null,
                    "LastConfigName": null,
                    "LastConfigVersion": null,
                    "NamespaceId": "namespace-vj3z3zgy",
                    "NamespaceName": "ns_default",
                    "ReleaseDesc": null,
                    "ReleaseStatus": "S",
                    "ReleaseTime": "2024-12-24 18:36:54",
                    "RollbackFlag": false
                }
            ],
            "TotalCount": 2
        }
    }
}
```


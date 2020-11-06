**Example 1: 查询配置发布历史**



Input: 

```
tccli tsf DescribeConfigReleaseLogs --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "RequestId": "cd8be98a-c557-43ef-bece-069f014bb2dd",
        "Result": {
            "TotalCount": 3,
            "Content": [
                {
                    "ConfigReleaseLogId": "dcfgrl-6ymq4b5v",
                    "ConfigId": "dcfg-6a79x94v",
                    "ConfigName": "[配置项已被删除]",
                    "ConfigVersion": "[配置项已被删除]",
                    "GroupId": "group-mae5orra",
                    "GroupName": "[部署组已被删除]",
                    "NamespaceId": null,
                    "NamespaceName": null,
                    "ClusterId": null,
                    "ClusterName": null,
                    "ReleaseTime": "2019-05-28 09:41:40",
                    "ReleaseDesc": null,
                    "ReleaseStatus": "S",
                    "LastConfigId": null,
                    "LastConfigName": null,
                    "LastConfigVersion": null,
                    "RollbackFlag": false
                },
                {
                    "ConfigReleaseLogId": "dcfgrl-ba228ppa",
                    "ConfigId": "dcfg-6a79x94v",
                    "ConfigName": "[配置项已被删除]",
                    "ConfigVersion": "[配置项已被删除]",
                    "GroupId": "group-mae5orra",
                    "GroupName": "[部署组已被删除]",
                    "NamespaceId": null,
                    "NamespaceName": null,
                    "ClusterId": null,
                    "ClusterName": null,
                    "ReleaseTime": "2019-05-28 09:36:52",
                    "ReleaseDesc": "删除配置项",
                    "ReleaseStatus": "DS",
                    "LastConfigId": "dcfg-6a79x94v",
                    "LastConfigName": "[配置项已被删除]",
                    "LastConfigVersion": "[配置项已被删除]",
                    "RollbackFlag": false
                },
                {
                    "ConfigReleaseLogId": "dcfgrl-evjjbjlv",
                    "ConfigId": "dcfg-6a79x94v",
                    "ConfigName": "[配置项已被删除]",
                    "ConfigVersion": "[配置项已被删除]",
                    "GroupId": "group-mae5orra",
                    "GroupName": "[部署组已被删除]",
                    "NamespaceId": null,
                    "NamespaceName": null,
                    "ClusterId": null,
                    "ClusterName": null,
                    "ReleaseTime": "2019-05-28 09:30:55",
                    "ReleaseDesc": null,
                    "ReleaseStatus": "S",
                    "LastConfigId": null,
                    "LastConfigName": null,
                    "LastConfigVersion": null,
                    "RollbackFlag": false
                }
            ]
        }
    }
}
```


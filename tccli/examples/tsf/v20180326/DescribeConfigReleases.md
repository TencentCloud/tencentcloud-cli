**Example 1: 查询配置发布信息**



Input: 

```
tccli tsf DescribeConfigReleases --cli-unfold-argument  \
    --ConfigName app-config \
    --GroupId group-aln2284v \
    --NamespaceId namespace-vw8oox6v \
    --ClusterId cluster-yne99jdy \
    --Limit 10 \
    --Offset 0 \
    --ConfigId dcfg-yo82mmra \
    --ApplicationId application-a7rwwz4v
```

Output: 
```
{
    "Response": {
        "RequestId": "16fa1e0b-d3e8-4b1f-b15f-e1d01966acb7",
        "Result": {
            "Content": [
                {
                    "ApplicationId": "application-a7rwwz4v",
                    "ClusterId": "cluster-yne99jdy",
                    "ClusterName": "cluster-app",
                    "ConfigCenters": [
                        {
                            "ConfigCenterInstanceId": null,
                            "ConfigCenterInstanceName": null,
                            "ConfigType": "SHARE",
                            "CurrentVersion": null,
                            "RegionId": null,
                            "TargetVersion": null
                        }
                    ],
                    "ConfigId": "dcfg-yo82mmra",
                    "ConfigName": "app-config",
                    "ConfigReleaseId": "dcfgr-yxd366ov",
                    "ConfigVersion": "v3",
                    "GroupId": "group-aln2284v",
                    "GroupName": "group-provider",
                    "NamespaceId": "namespace-vw8oox6v",
                    "NamespaceName": "cluster-app_default",
                    "ReleaseDesc": "This is desc",
                    "ReleaseTime": "2024-12-24 15:57:15"
                }
            ],
            "TotalCount": 1
        }
    }
}
```


**Example 1: 查询公共配置发布信息**



Input: 

```
tccli tsf DescribePublicConfigReleases --cli-unfold-argument  \
    --ConfigName configName \
    --NamespaceId namespace-yxoqm4ky \
    --Limit 10 \
    --Offset 0 \
    --ConfigId dcfg-p-v6kxdlpy
```

Output: 
```
{
    "Response": {
        "RequestId": "2435f045-963a-43da-a29b-581eb28069c0",
        "Result": {
            "Content": [
                {
                    "ApplicationId": null,
                    "ClusterId": null,
                    "ClusterName": null,
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
                    "ConfigId": "dcfg-p-v6kxdlpy",
                    "ConfigName": "configName",
                    "ConfigReleaseId": "dcfgr-y446nlby",
                    "ConfigVersion": "1",
                    "GroupId": null,
                    "GroupName": null,
                    "NamespaceId": "namespace-yxoqm4ky",
                    "NamespaceName": "ns_default",
                    "ReleaseDesc": null,
                    "ReleaseTime": "2024-09-11 17:27:59"
                }
            ],
            "TotalCount": 1
        }
    }
}
```


**Example 1: 发布配置，并且返回配置ID。**

将一个应用配置项发布到指定的应用部署组

Input: 

```
tccli tsf ReleaseConfigWithDetailResp --cli-unfold-argument  \
    --ConfigId dcfg-yo82mmra \
    --GroupId group-aln2284v \
    --ReleaseDesc This is desc
```

Output: 
```
{
    "Response": {
        "RequestId": "1892e2c1-9223-4979-bf25-1935c7eeed12",
        "Result": {
            "ApplicationId": null,
            "ClusterId": null,
            "ClusterName": null,
            "ConfigCenters": null,
            "ConfigId": null,
            "ConfigName": null,
            "ConfigReleaseId": "dcfgr-yxd366ov",
            "ConfigVersion": null,
            "GroupId": null,
            "GroupName": null,
            "NamespaceId": null,
            "NamespaceName": null,
            "ReleaseDesc": null,
            "ReleaseTime": null
        }
    }
}
```


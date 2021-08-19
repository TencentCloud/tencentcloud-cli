**Example 1: 查询部署组发布的相关信息**



Input: 

```
tccli tsf DescribeGroupRelease --cli-unfold-argument  \
    --GroupId group-xxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "c033faca-041a-4357-a96d-xxxxxxxx",
        "Result": {
            "PackageName": "consumer-demo-1.25.0-Greenwich-SNAPSHOT.jar",
            "PackageVersion": "xxxxxx",
            "PackageId": "pkg-xxxxxx",
            "PublicConfigReleaseList": [
                {
                    "ConfigReleaseId": "dcfgr-xxxxxx",
                    "ConfigId": "dcfg-p-xxxxxx",
                    "ConfigName": "n1",
                    "ConfigVersion": "v1",
                    "ReleaseTime": "2021-08-10 10:xx:xx",
                    "GroupId": null,
                    "GroupName": null,
                    "NamespaceId": "namespace-xxxxxxxx",
                    "NamespaceName": "xxxxxx",
                    "ClusterId": null,
                    "ClusterName": null,
                    "ReleaseDesc": null,
                    "ApplicationId": null
                }
            ]
        }
    }
}
```


**Example 1: 查询部署组发布的相关信息**



Input: 

```
tccli tsf DescribeGroupRelease --cli-unfold-argument  \
    --GroupId group-v6q747py
```

Output: 
```
{
    "Response": {
        "RequestId": "81d75b7e-8bec-47fd-bc65-c99bb24f569e",
        "Result": {
            "ConfigReleaseList": [
                {
                    "ApplicationId": "application-vzoebl8a",
                    "ClusterId": "cls-i3v5y09e",
                    "ClusterName": "cls-app",
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
                    "ConfigId": "dcfg-a7rl7w4v",
                    "ConfigName": "conf-app",
                    "ConfigReleaseId": "dcfgr-ymw5965v",
                    "ConfigVersion": "v1",
                    "GroupId": "group-v6q747py",
                    "GroupName": "cloud-provider",
                    "NamespaceId": "namespace-vj3z3zgy",
                    "NamespaceName": "ns_default",
                    "ReleaseDesc": null,
                    "ReleaseTime": "2024-12-24 18:36:03"
                }
            ],
            "FileConfigReleaseList": [
                {
                    "ClusterId": "cls-i3v5y09e",
                    "ClusterName": "cls-app",
                    "ConfigId": "dcfg-f-aeonjd6y",
                    "ConfigName": "config_app",
                    "ConfigReleaseId": "dcfgr-f-y84omela",
                    "ConfigVersion": "v1",
                    "GroupId": "group-v6q747py",
                    "GroupName": "cloud-provider",
                    "NamespaceId": "namespace-vj3z3zgy",
                    "NamespaceName": "ns_default",
                    "ReleaseDesc": null,
                    "ReleaseTime": "2024-12-24 18:37:50"
                }
            ],
            "PackageId": "pkg-9198307d",
            "PackageName": "msgw-zuul1-1.29.20-Hoxton-Higher-RELEASE.jar",
            "PackageVersion": "20241223010307",
            "PublicConfigReleaseList": [
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
                    "ConfigId": "dcfg-p-vzk36rov",
                    "ConfigName": "config_pub_app",
                    "ConfigReleaseId": "dcfgr-yne579dy",
                    "ConfigVersion": "v1",
                    "GroupId": null,
                    "GroupName": null,
                    "NamespaceId": "namespace-vj3z3zgy",
                    "NamespaceName": "ns_default",
                    "ReleaseDesc": null,
                    "ReleaseTime": "2024-12-24 18:36:54"
                }
            ],
            "RepoName": "tsf_100011910000/app-provider",
            "TagName": "20241212161801"
        }
    }
}
```


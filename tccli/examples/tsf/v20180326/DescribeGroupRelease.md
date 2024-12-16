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
            "PackageVersion": "1.25.0",
            "PackageId": "pkg-xxxxxx",
            "PublicConfigReleaseList": [
                {
                    "ConfigReleaseId": "dcfgr-xxxxxx",
                    "ConfigId": "dcfg-p-xxxxxx",
                    "ConfigName": "n1",
                    "ConfigVersion": "v1",
                    "ReleaseTime": "2021-08-10 10:xx:xx",
                    "GroupId": "group-6a79x94v",
                    "GroupName": "group-mock",
                    "NamespaceId": "namespace-xxxxxxxx",
                    "NamespaceName": "default",
                    "ClusterId": "cls-6a79x94v",
                    "ClusterName": "cls-mock",
                    "ReleaseDesc": "this is a desc",
                    "ApplicationId": "application-6a79x94v"
                }
            ]
        }
    }
}
```


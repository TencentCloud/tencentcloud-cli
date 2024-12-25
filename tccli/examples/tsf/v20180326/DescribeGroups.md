**Example 1: 获取虚拟机部署组列表**



Input: 

```
tccli tsf DescribeGroups --cli-unfold-argument  \
    --Limit 2
```

Output: 
```
{
    "Response": {
        "RequestId": "b1128c11-9b6d-4d06-814d-c3c561b79f6c",
        "Result": {
            "Content": [
                {
                    "Alias": "",
                    "ApplicationId": "application-ydopqnxa",
                    "ApplicationName": "shedfree-gw",
                    "ApplicationType": "V",
                    "ClusterId": "cluster-2vz3nd3a",
                    "ClusterName": "shedfree",
                    "CreateTime": "2024-12-23 16:27:02",
                    "DeployDesc": null,
                    "GroupDesc": null,
                    "GroupId": "group-y4dz9x6y",
                    "GroupName": "shed-scg-2021",
                    "GroupResourceType": "DEF",
                    "MicroserviceType": "G",
                    "NamespaceId": "namespace-qab7bq9v",
                    "NamespaceName": "shedfree_default",
                    "StartupParameters": "-Xms1024m -Xmx4096m -XX:MetaspaceSize=1024m -XX:MaxMetaspaceSize=1024m -Dlogging.level.com.tencent.tsf.msgw.scg.filter=error -Dreactor.netty.pool.leasingStrategy=lifo  -Dkona.fiber.enabled=true",
                    "UpdateTime": "2024-12-24 09:21:23",
                    "UpdatedTime": 1735003283000
                },
                {
                    "Alias": "",
                    "ApplicationId": "application-ydopqnxa",
                    "ApplicationName": "shedfree-gw",
                    "ApplicationType": "V",
                    "ClusterId": "cluster-2vz3nd3a",
                    "ClusterName": "shedfree",
                    "CreateTime": "2024-12-23 01:15:31",
                    "DeployDesc": null,
                    "GroupDesc": null,
                    "GroupId": "group-yq9d6wev",
                    "GroupName": "shed-zuul-3",
                    "GroupResourceType": "DEF",
                    "MicroserviceType": "G",
                    "NamespaceId": "namespace-qab7bq9v",
                    "NamespaceName": "shedfree_default",
                    "StartupParameters": "-Xms1024m -Xmx4096m -XX:MetaspaceSize=1024m -XX:MaxMetaspaceSize=1024m",
                    "UpdateTime": "2024-12-23 01:30:25",
                    "UpdatedTime": 1734888625000
                }
            ],
            "TotalCount": 660
        }
    }
}
```


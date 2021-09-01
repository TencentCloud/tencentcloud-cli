**Example 1: 查询虚拟机部署组详情**



Input: 

```
tccli tsf DescribeGroup --cli-unfold-argument  \
    --GroupId group-oydzed8v
```

Output: 
```
{
    "Response": {
        "RequestId": "d303489f-e1a0-41d4-8044-dc8cd42a3ae6",
        "Result": {
            "ApplicationType": "V",
            "MicroserviceType": "N",
            "GroupId": "group-oydzed8v",
            "ClusterId": "cluster-by8n8rmy",
            "StartupParameters": "-Xms128m -Xmx512m -XX:MetaspaceSize=128m -XX:MaxMetaspaceSize=512m",
            "ClusterName": "test",
            "PackageName": "travel-passenger-api-1.0-SNAPSHOT.jar",
            "RunInstanceCount": 1,
            "ApplicationName": "ruqitest_travel_clientapi",
            "NamespaceName": "test-connection-group",
            "GroupDesc": null,
            "PackageId": "pkg-b430b6a2",
            "UpdateTime": "2019-03-11 16:52:15",
            "PackageVersion": "20190529173949",
            "GroupStatus": "Updating",
            "GroupName": "ruqitest-clientapi-dep",
            "CreateTime": "2019-03-11 16:52:15",
            "NamespaceId": "namespace-6yogoqdv",
            "InstanceCount": 1,
            "ApplicationId": "application-6a7eog6y",
            "OffInstanceCount": 0,
            "UpdateType": 1,
            "DeployBetaEnable": false,
            "DeployBatch": [
                0.2,
                0.8
            ],
            "DeployExeMode": "auto/manual",
            "DeployWaitTime": 0,
            "DeployDesc": "desc",
            "GroupResourceType": "DEF",
            "UpdatedTime": 1602770765000
        }
    }
}
```


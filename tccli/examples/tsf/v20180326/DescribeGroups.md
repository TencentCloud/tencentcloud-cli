**Example 1: 获取虚拟机部署组列表**



Input: 

```
tccli tsf DescribeGroups --cli-unfold-argument  \
    --ApplicationId application-xxxxxxx \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "4bf8bc01-2786-4341-be2b-c6610556026e",
        "Result": {
            "TotalCount": 1,
            "Content": [
                {
                    "ApplicationType": "V",
                    "MicroserviceType": "N",
                    "GroupId": "group-6a79x94v",
                    "ClusterId": "cluster-6a79x94v",
                    "StartupParameters": "-Xms128m -Xmx512m -XX:MetaspaceSize=128m -XX:MaxMetaspaceSize=512m",
                    "ClusterName": "cls-mock",
                    "ApplicationName": "app-mock",
                    "NamespaceName": "default",
                    "GroupDesc": "this is a desc",
                    "UpdateTime": "2019-03-11 16:51:55",
                    "GroupName": "group-mock",
                    "Alias": "group-alias",
                    "DeployDesc": "描述",
                    "NamespaceId": "namespace-6a79x94v",
                    "GroupResourceType": "DEF",
                    "CreateTime": "2019-03-11 16:51:55",
                    "UpdatedTime": "17623946749",
                    "ApplicationId": "application-6a79x94v"
                }
            ]
        }
    }
}
```


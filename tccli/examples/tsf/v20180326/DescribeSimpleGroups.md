**Example 1: 查询简单部署组列表**



Input: 

```
tccli tsf DescribeSimpleGroups --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20 \
    --ApplicationId application-6a79x94v
```

Output: 
```
{
    "Response": {
        "RequestId": "f92318c2-55c5-479f-b73e-f63683bee456",
        "Result": {
            "TotalCount": 1,
            "Content": [
                {
                    "GroupId": "group-6a79x94v",
                    "GroupName": "group-mock",
                    "ClusterId": "cls-6a79x94v",
                    "ClusterName": "cls-mock",
                    "ClusterType": "C",
                    "NamespaceId": "namespace-6a79x94v",
                    "NamespaceName": "default",
                    "ApplicationId": "application-6a79x94v",
                    "ApplicationName": "java-service",
                    "ApplicationType": "C",
                    "AppMicroServiceType": "N",
                    "GroupResourceType": "DEF",
                    "StartupParameters": "-Dspring.application.name=java-service"
                }
            ]
        }
    }
}
```


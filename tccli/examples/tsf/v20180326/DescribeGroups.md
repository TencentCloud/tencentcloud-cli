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
                    "GroupId": "group-xxxxxxx",
                    "ClusterId": "cluster-xxxxxxx",
                    "StartupParameters": "-Xms128m -Xmx512m -XX:MetaspaceSize=128m -XX:MaxMetaspaceSize=512m",
                    "ClusterName": "test",
                    "ApplicationName": "test1",
                    "NamespaceName": "test2",
                    "GroupDesc": null,
                    "UpdateTime": "2019-03-11 16:51:55",
                    "GroupName": "test",
                    "NamespaceId": "namespace-xxxxxxx",
                    "CreateTime": "2019-03-11 16:51:55",
                    "ApplicationId": "application-xxxxxxx"
                }
            ]
        }
    }
}
```


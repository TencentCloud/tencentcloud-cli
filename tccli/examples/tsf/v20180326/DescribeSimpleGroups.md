**Example 1: 查询简单部署组列表**



Input: 

```
tccli tsf DescribeSimpleGroups --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20 \
    --ApplicationId application-xxxxxxx
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
                    "GroupId": "group-xxxxxxx",
                    "GroupName": "test",
                    "ClusterId": "cls-xxxxxxx",
                    "ClusterName": "test",
                    "ClusterType": "C",
                    "NamespaceId": "namespace-xxxxxxx",
                    "NamespaceName": "test",
                    "ApplicationId": "application-xxxxxxx",
                    "ApplicationName": "test",
                    "ApplicationType": "C"
                }
            ]
        }
    }
}
```


**Example 1: 查询应用更新触发器**



Input: 

```
tccli tcr DescribeApplicationTriggerPersonal --cli-unfold-argument  \
    --RepoName test/test123
```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalCount": 1,
            "TriggerInfo": [
                {
                    "TriggerName": "test2",
                    "InvokeSource": "IMAGE_PUSH",
                    "InvokeAction": "SERVICE_UPDATE",
                    "CreateTime": "2020-01-23 17:06:17",
                    "UpdateTime": "2020-01-23 17:44:26",
                    "InvokeCondition": {
                        "InvokeMethod": "taglist",
                        "InvokeExpr": "abc"
                    },
                    "InvokePara": {
                        "AppId": "1251006373",
                        "ClusterId": "cls-aj3c8wz5",
                        "Namespace": "default",
                        "ServiceName": "Deployment:testdp",
                        "ContainerName": "testcon",
                        "ClusterRegion": 16
                    }
                }
            ]
        },
        "RequestId": "7d27c2f4-0473-484c-b62e-fcb379758289"
    }
}
```


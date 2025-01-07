**Example 1: 查询应用更新触发器**



Input: 

```
tccli tcr DescribeApplicationTriggerPersonal --cli-unfold-argument  \
    --Limit 3
```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalCount": 29,
            "TriggerInfo": [
                {
                    "CreateTime": "2021-11-18 11:51:13",
                    "InvokeAction": "SERVICE_UPDATE",
                    "InvokeCondition": {
                        "InvokeExpr": "",
                        "InvokeMethod": "all"
                    },
                    "InvokePara": {
                        "AppId": "1251707795",
                        "ClusterId": "cls-prnklzue",
                        "ClusterRegion": 1,
                        "ContainerName": "nginx",
                        "Namespace": "default",
                        "ServiceName": "Deployment:nginx-deployment"
                    },
                    "InvokeSource": "IMAGE_PUSH",
                    "TriggerName": "aaaa",
                    "UpdateTime": "2021-11-18 11:51:13"
                },
                {
                    "CreateTime": "2021-10-27 10:11:30",
                    "InvokeAction": "SERVICE_UPDATE",
                    "InvokeCondition": {
                        "InvokeExpr": "",
                        "InvokeMethod": "all"
                    },
                    "InvokePara": {
                        "AppId": "1251707795",
                        "ClusterId": "cls-94j6nzm8",
                        "ClusterRegion": 33,
                        "ContainerName": "nginx",
                        "Namespace": "default",
                        "ServiceName": "Deployment:nginx"
                    },
                    "InvokeSource": "IMAGE_PUSH",
                    "TriggerName": "sss",
                    "UpdateTime": "2021-10-27 10:11:30"
                },
                {
                    "CreateTime": "2020-12-22 10:45:36",
                    "InvokeAction": "SERVICE_UPDATE",
                    "InvokeCondition": {
                        "InvokeExpr": "",
                        "InvokeMethod": "all"
                    },
                    "InvokePara": {
                        "AppId": "1251707795",
                        "ClusterId": "clust-xxx",
                        "ClusterRegion": 1,
                        "ContainerName": "web",
                        "Namespace": "default",
                        "ServiceName": "Deployment:kofj"
                    },
                    "InvokeSource": "IMAGE_PUSH",
                    "TriggerName": "kofj-test-20201222",
                    "UpdateTime": "2020-12-22 10:45:36"
                }
            ]
        },
        "RequestId": "a904482e-68ec-47d9-9f1f-87908659bd81"
    }
}
```


**Example 1: 查询应用更新触发器触发日志**



Input: 

```
tccli tcr DescribeApplicationTriggerLogPersonal --cli-unfold-argument  \
    --RepoName ccs-dev/nginx \
    --Offset 0 \
    --Limit 10 \
    --Order desc \
    --OrderBy invoke_time
```

Output: 
```
{
    "Response": {
        "Data": {
            "LogInfo": [
                {
                    "InvokeAction": "SERVICE_UPDATE",
                    "InvokeCondition": {
                        "InvokeExpr": "",
                        "InvokeMethod": "all"
                    },
                    "InvokePara": {
                        "AppId": "1251707795",
                        "ClusterId": "cls-37rckkhe",
                        "ClusterRegion": 1,
                        "ContainerName": "nginx",
                        "Namespace": "default",
                        "ServiceName": "nginx"
                    },
                    "InvokeResult": {
                        "ReturnCode": 0,
                        "ReturnMsg": "ok"
                    },
                    "InvokeSource": "IMAGE_PUSH",
                    "InvokeTime": "2020-02-08 00:12:36",
                    "RepoName": "ccs-dev/nginx",
                    "TagName": "latest",
                    "TriggerName": "penglei-debug"
                },
                {
                    "InvokeAction": "SERVICE_UPDATE",
                    "InvokeCondition": {
                        "InvokeExpr": "",
                        "InvokeMethod": "all"
                    },
                    "InvokePara": {
                        "AppId": "1251707795",
                        "ClusterId": "cls-37rckkhe",
                        "ClusterRegion": 1,
                        "ContainerName": "nginx",
                        "Namespace": "default",
                        "ServiceName": "nginx"
                    },
                    "InvokeResult": {
                        "ReturnCode": 0,
                        "ReturnMsg": "ok"
                    },
                    "InvokeSource": "IMAGE_PUSH",
                    "InvokeTime": "2018-01-17 15:40:43",
                    "RepoName": "ccs-dev/nginx",
                    "TagName": "penglei-debug-trigger-v10",
                    "TriggerName": "penglei-debug"
                },
                {
                    "InvokeAction": "SERVICE_UPDATE",
                    "InvokeCondition": {
                        "InvokeExpr": "",
                        "InvokeMethod": "all"
                    },
                    "InvokePara": {
                        "AppId": "1251707795",
                        "ClusterId": "cls-37rckkhe",
                        "ClusterRegion": 1,
                        "ContainerName": "nginx",
                        "Namespace": "default",
                        "ServiceName": "nginx"
                    },
                    "InvokeResult": {
                        "ReturnCode": 0,
                        "ReturnMsg": "ok"
                    },
                    "InvokeSource": "IMAGE_PUSH",
                    "InvokeTime": "2018-01-17 15:36:06",
                    "RepoName": "ccs-dev/nginx",
                    "TagName": "penglei-debug-trigger-v9",
                    "TriggerName": "penglei-debug"
                },
                {
                    "InvokeAction": "SERVICE_UPDATE",
                    "InvokeCondition": {
                        "InvokeExpr": "",
                        "InvokeMethod": "all"
                    },
                    "InvokePara": {
                        "AppId": "1251707795",
                        "ClusterId": "cls-37rckkhe",
                        "ClusterRegion": 1,
                        "ContainerName": "nginx",
                        "Namespace": "default",
                        "ServiceName": "nginx"
                    },
                    "InvokeResult": {
                        "ReturnCode": 0,
                        "ReturnMsg": "ok"
                    },
                    "InvokeSource": "IMAGE_PUSH",
                    "InvokeTime": "2018-01-17 15:33:30",
                    "RepoName": "ccs-dev/nginx",
                    "TagName": "penglei-debug-trigger-v8",
                    "TriggerName": "penglei-debug"
                },
                {
                    "InvokeAction": "SERVICE_UPDATE",
                    "InvokeCondition": {
                        "InvokeExpr": "",
                        "InvokeMethod": "all"
                    },
                    "InvokePara": {
                        "AppId": "1251707795",
                        "ClusterId": "cls-37rckkhe",
                        "ClusterRegion": 1,
                        "ContainerName": "nginx",
                        "Namespace": "default",
                        "ServiceName": "nginx"
                    },
                    "InvokeResult": {
                        "ReturnCode": 0,
                        "ReturnMsg": "ok"
                    },
                    "InvokeSource": "IMAGE_PUSH",
                    "InvokeTime": "2018-01-17 15:31:19",
                    "RepoName": "ccs-dev/nginx",
                    "TagName": "penglei-debug-trigger-v7",
                    "TriggerName": "penglei-debug"
                },
                {
                    "InvokeAction": "SERVICE_UPDATE",
                    "InvokeCondition": {
                        "InvokeExpr": "",
                        "InvokeMethod": "all"
                    },
                    "InvokePara": {
                        "AppId": "1251707795",
                        "ClusterId": "cls-37rckkhe",
                        "ClusterRegion": 1,
                        "ContainerName": "nginx",
                        "Namespace": "default",
                        "ServiceName": "nginx"
                    },
                    "InvokeResult": {
                        "ReturnCode": 0,
                        "ReturnMsg": "ok"
                    },
                    "InvokeSource": "IMAGE_PUSH",
                    "InvokeTime": "2018-01-17 15:27:57",
                    "RepoName": "ccs-dev/nginx",
                    "TagName": "penglei-debug-trigger-v6",
                    "TriggerName": "penglei-debug"
                },
                {
                    "InvokeAction": "SERVICE_UPDATE",
                    "InvokeCondition": {
                        "InvokeExpr": "",
                        "InvokeMethod": "all"
                    },
                    "InvokePara": {
                        "AppId": "1251707795",
                        "ClusterId": "cls-37rckkhe",
                        "ClusterRegion": 1,
                        "ContainerName": "nginx",
                        "Namespace": "default",
                        "ServiceName": "nginx"
                    },
                    "InvokeResult": {
                        "ReturnCode": 0,
                        "ReturnMsg": "ok"
                    },
                    "InvokeSource": "IMAGE_PUSH",
                    "InvokeTime": "2018-01-17 15:00:03",
                    "RepoName": "ccs-dev/nginx",
                    "TagName": "penglei-debug-trigger-v5",
                    "TriggerName": "penglei-debug"
                },
                {
                    "InvokeAction": "SERVICE_UPDATE",
                    "InvokeCondition": {
                        "InvokeExpr": "",
                        "InvokeMethod": "all"
                    },
                    "InvokePara": {
                        "AppId": "1251707795",
                        "ClusterId": "cls-37rckkhe",
                        "ClusterRegion": 1,
                        "ContainerName": "nginx",
                        "Namespace": "default",
                        "ServiceName": "nginx"
                    },
                    "InvokeResult": {
                        "ReturnCode": 0,
                        "ReturnMsg": "ok"
                    },
                    "InvokeSource": "IMAGE_PUSH",
                    "InvokeTime": "2018-01-17 14:58:37",
                    "RepoName": "ccs-dev/nginx",
                    "TagName": "penglei-debug-trigger-v4",
                    "TriggerName": "penglei-debug"
                },
                {
                    "InvokeAction": "SERVICE_UPDATE",
                    "InvokeCondition": {
                        "InvokeExpr": "",
                        "InvokeMethod": "all"
                    },
                    "InvokePara": {
                        "AppId": "1251707795",
                        "ClusterId": "cls-37rckkhe",
                        "ClusterRegion": 1,
                        "ContainerName": "nginx",
                        "Namespace": "default",
                        "ServiceName": "nginx"
                    },
                    "InvokeResult": {
                        "ReturnCode": 0,
                        "ReturnMsg": "ok"
                    },
                    "InvokeSource": "IMAGE_PUSH",
                    "InvokeTime": "2018-01-17 14:53:29",
                    "RepoName": "ccs-dev/nginx",
                    "TagName": "penglei-debug-trigger-v3",
                    "TriggerName": "penglei-debug"
                },
                {
                    "InvokeAction": "SERVICE_UPDATE",
                    "InvokeCondition": {
                        "InvokeExpr": "",
                        "InvokeMethod": "all"
                    },
                    "InvokePara": {
                        "AppId": "1251707795",
                        "ClusterId": "cls-37rckkhe",
                        "ClusterRegion": 1,
                        "ContainerName": "nginx",
                        "Namespace": "default",
                        "ServiceName": "nginx"
                    },
                    "InvokeResult": {
                        "ReturnCode": 0,
                        "ReturnMsg": "ok"
                    },
                    "InvokeSource": "IMAGE_PUSH",
                    "InvokeTime": "2018-01-17 11:00:03",
                    "RepoName": "ccs-dev/nginx",
                    "TagName": "penglei-debug-trigger-v2",
                    "TriggerName": "penglei-debug"
                }
            ],
            "TotalCount": 10
        },
        "RequestId": "7d9dd5f4-62df-45e0-8e84-587d33eaf0ba"
    }
}
```


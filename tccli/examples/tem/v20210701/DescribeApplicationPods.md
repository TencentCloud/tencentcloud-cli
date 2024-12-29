**Example 1: 获取应用实例列表**

获取应用实例列表

Input: 

```
tccli tem DescribeApplicationPods --cli-unfold-argument  \
    --Status Running \
    --EnvironmentId en-xxxxxx \
    --Offset 0 \
    --SourceChannel 0 \
    --Limit 20 \
    --PodName pod-name-xxx \
    --ApplicationId app-xxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "0f09d0d3-3414-48ba-b8cc-e1c543b1fc1a",
        "Result": {
            "Offset": 0,
            "Limit": 3,
            "TotalCount": 3,
            "PodList": [
                {
                    "Zone": "ap-shanghai-2",
                    "NodeInfo": {
                        "Name": "eklet-subnet-kctzw7nj-711231",
                        "Zone": "ap-shanghai-2",
                        "SubnetId": "subnet-kctzw7nj",
                        "AvailableIpCount": "243",
                        "Cidr": "10.0.10.0-24"
                    },
                    "DeployVersion": "20241202165113",
                    "RestartCount": 0,
                    "Ready": false,
                    "StartTime": "2024-12-20T09:01:01Z",
                    "ContainerState": "waiting",
                    "Unhealthy": null,
                    "UnhealthyWarningMsg": "",
                    "VersionId": "revision-jorxnl6j",
                    "ApplicationName": "app0925",
                    "Status": "CrashLoopBackOff",
                    "CreateTime": "2024-12-20 17:00:23",
                    "Webshell": "https://tkecache.cloud.tencent.com/xxx",
                    "PodId": "app0925-4sbct",
                    "PodIp": "10.0.10.220"
                },
                {
                    "Zone": "ap-shanghai-2",
                    "NodeInfo": {
                        "Name": "eklet-subnet-qau65gm1-638453",
                        "Zone": "ap-shanghai-2",
                        "SubnetId": "subnet-qau65gm1",
                        "AvailableIpCount": "246",
                        "Cidr": "10.0.20.0-24"
                    },
                    "DeployVersion": "20241202165113",
                    "RestartCount": 0,
                    "Ready": false,
                    "StartTime": "2024-12-20T09:01:11Z",
                    "ContainerState": "waiting",
                    "Unhealthy": null,
                    "UnhealthyWarningMsg": "",
                    "VersionId": "revision-jorxnl6j",
                    "ApplicationName": "app0925",
                    "Status": "CrashLoopBackOff",
                    "CreateTime": "2024-12-20 17:00:23",
                    "Webshell": "https://tkecache.cloud.tencent.com/xxx",
                    "PodId": "app0925-s4vpj",
                    "PodIp": "10.0.20.37"
                },
                {
                    "Zone": "ap-shanghai-2",
                    "NodeInfo": {
                        "Name": "eklet-subnet-8indzsuv-457482",
                        "Zone": "ap-shanghai-2",
                        "SubnetId": "subnet-8indzsuv",
                        "AvailableIpCount": "226",
                        "Cidr": "10.0.30.0-24"
                    },
                    "DeployVersion": "20241202165113",
                    "RestartCount": 0,
                    "Ready": true,
                    "StartTime": "2024-12-19T03:12:44Z",
                    "ContainerState": "running",
                    "Unhealthy": null,
                    "UnhealthyWarningMsg": "",
                    "VersionId": "revision-57moqvm5",
                    "ApplicationName": "app0925",
                    "Status": "Running",
                    "CreateTime": "2024-12-19 11:11:32",
                    "Webshell": "https://tkecache.cloud.tencent.com/xxx",
                    "PodId": "app0925-jt5bn",
                    "PodIp": "10.0.30.158"
                }
            ],
            "RequestId": "0f09d0d3-xxx-xxx-xxx"
        }
    }
}
```


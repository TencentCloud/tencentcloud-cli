**Example 1: 获取分批发布详情**

获取分批发布详情

Input: 

```
tccli tem DescribeDeployApplicationDetail --cli-unfold-argument  \
    --ApplicationId app-xxxxxx \
    --EnvironmentId en-xxxxxx \
    --VersionId version-xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "7559e31e-4e32-476d-93f2-db6bcbab530a",
        "Result": {
            "DeployStrategyConf": {
                "TotalBatchCount": 1,
                "BetaBatchNum": 0,
                "DeployStrategyType": 3,
                "BatchInterval": 0,
                "MinAvailable": 1,
                "Force": true
            },
            "StartTime": "2024-12-20 17:00:17",
            "EndTime": "",
            "Status": "Error",
            "CurrentBatchStatus": "Finish",
            "ErrorMessage": "",
            "BetaBatchDetail": null,
            "OtherBatchDetail": [
                {
                    "OldPods": [],
                    "NewPods": [
                        {
                            "PodId": "app0925-4sbct",
                            "PodVersion": "",
                            "CreateTime": "2024-12-20 17:00:23",
                            "Zone": "ap-shanghai-2",
                            "Webshell": "https://tkecache.cloud.tencent.com/xxx",
                            "Status": "CrashLoopBackOff",
                            "PodStatus": [
                                "CrashLoopBackOff"
                            ]
                        },
                        {
                            "PodId": "app0925-s4vpj",
                            "PodVersion": "",
                            "CreateTime": "2024-12-20 17:00:23",
                            "Zone": "ap-shanghai-2",
                            "Webshell": "https://tkecache.cloud.tencent.com/xxx",
                            "Status": "CrashLoopBackOff",
                            "PodStatus": [
                                "CrashLoopBackOff"
                            ]
                        }
                    ],
                    "BatchStatus": "Finish",
                    "PodNum": 3,
                    "BatchIndex": 0,
                    "NextBatchStartTime": 0,
                    "OldPodList": null,
                    "NewPodList": null
                }
            ],
            "OldVersionPodList": {
                "Offset": 0,
                "Limit": 1,
                "TotalCount": 1,
                "PodList": [
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
                "RequestId": ""
            },
            "CurrentBatchIndex": 0,
            "NewVersionPackageInfo": "K8sEventDemo-1.0.jar",
            "NewDeployVersion": "20241202165113",
            "OldDeployVersion": "20241202165113",
            "NextBatchStartTime": null
        }
    }
}
```


**Example 1: 获取分批发布详情**

获取分批发布详情

Input: 

```
tccli tem DescribeDeployApplicationDetail --cli-unfold-argument  \
    --EnvironmentId xx \
    --ApplicationId xx
```

Output: 
```
{
    "Response": {
        "Result": {
            "Status": "xx",
            "NewVersionPackageInfo": "xx",
            "NextBatchStartTime": 0,
            "OldDeployVersion": "xx",
            "BetaBatchDetail": {
                "NewPods": [
                    {
                        "Webshell": "xx",
                        "PodStatus": [
                            "xx"
                        ],
                        "Zone": "xx",
                        "PodId": "xx",
                        "CreateTime": "xx",
                        "PodVersion": "xx"
                    }
                ],
                "NewPodList": {
                    "Webshell": "xx",
                    "PodStatus": [
                        "xx"
                    ],
                    "Zone": "xx",
                    "PodId": "xx",
                    "CreateTime": "xx",
                    "PodVersion": "xx"
                },
                "BatchIndex": 0,
                "OldPodList": {
                    "Webshell": "xx",
                    "PodStatus": [
                        "xx"
                    ],
                    "Zone": "xx",
                    "PodId": "xx",
                    "CreateTime": "xx",
                    "PodVersion": "xx"
                },
                "NextBatchStartTime": 0,
                "OldPods": [
                    {
                        "Webshell": "xx",
                        "PodStatus": [
                            "xx"
                        ],
                        "Zone": "xx",
                        "PodId": "xx",
                        "CreateTime": "xx",
                        "PodVersion": "xx"
                    }
                ],
                "BatchStatus": "xx",
                "PodNum": 0
            },
            "ErrorMessage": "xx",
            "DeployStrategyConf": {
                "TotalBatchCount": 0,
                "DeployStrategyType": 0,
                "BatchInterval": 0,
                "BetaBatchNum": 0
            },
            "NewDeployVersion": "xx",
            "StartTime": "xx",
            "OtherBatchDetail": [
                {
                    "NewPods": [
                        {
                            "Webshell": "xx",
                            "PodStatus": [
                                "xx"
                            ],
                            "Zone": "xx",
                            "PodId": "xx",
                            "CreateTime": "xx",
                            "PodVersion": "xx"
                        }
                    ],
                    "NewPodList": {
                        "Webshell": "xx",
                        "PodStatus": [
                            "xx"
                        ],
                        "Zone": "xx",
                        "PodId": "xx",
                        "CreateTime": "xx",
                        "PodVersion": "xx"
                    },
                    "BatchIndex": 0,
                    "OldPodList": {
                        "Webshell": "xx",
                        "PodStatus": [
                            "xx"
                        ],
                        "Zone": "xx",
                        "PodId": "xx",
                        "CreateTime": "xx",
                        "PodVersion": "xx"
                    },
                    "NextBatchStartTime": 0,
                    "OldPods": [
                        {
                            "Webshell": "xx",
                            "PodStatus": [
                                "xx"
                            ],
                            "Zone": "xx",
                            "PodId": "xx",
                            "CreateTime": "xx",
                            "PodVersion": "xx"
                        }
                    ],
                    "BatchStatus": "xx",
                    "PodNum": 0
                }
            ],
            "CurrentBatchIndex": 0,
            "EndTime": "xx",
            "CurrentBatchStatus": "xx",
            "OldVersionPodList": {
                "TotalCount": 0,
                "Limit": 0,
                "RequestId": "xx",
                "PodList": [
                    {
                        "Webshell": "xx",
                        "Status": "xx",
                        "RestartCount": 0,
                        "Zone": "xx",
                        "PodId": "xx",
                        "DeployVersion": "xx",
                        "PodIp": "xx",
                        "ContainerState": "xx",
                        "Ready": true,
                        "CreateTime": "xx"
                    }
                ],
                "Offset": 0
            }
        },
        "RequestId": "xx"
    }
}
```


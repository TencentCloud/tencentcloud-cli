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
            "BetaBatchDetail": {
                "NewPodList": {
                    "PodVersion": "xx",
                    "Zone": "xx",
                    "CreateTime": "xx",
                    "PodStatus": [
                        "xx"
                    ],
                    "PodId": "xx"
                },
                "BatchIndex": 0,
                "BatchStatus": "xx",
                "OldPodList": {
                    "PodVersion": "xx",
                    "Zone": "xx",
                    "CreateTime": "xx",
                    "PodStatus": [
                        "xx"
                    ],
                    "PodId": "xx"
                },
                "PodNum": 0
            },
            "ErrorMessage": "xx",
            "DeployStrategyConf": {
                "TotalBatchCount": 0,
                "DeployStrategyType": 0,
                "BatchInterval": 0,
                "BetaBatchNum": 0
            },
            "OtherBatchDetail": [
                {
                    "NewPodList": {
                        "PodVersion": "xx",
                        "Zone": "xx",
                        "CreateTime": "xx",
                        "PodStatus": [
                            "xx"
                        ],
                        "PodId": "xx"
                    },
                    "BatchIndex": 0,
                    "BatchStatus": "xx",
                    "OldPodList": {
                        "PodVersion": "xx",
                        "Zone": "xx",
                        "CreateTime": "xx",
                        "PodStatus": [
                            "xx"
                        ],
                        "PodId": "xx"
                    },
                    "PodNum": 0
                }
            ],
            "StartTime": "xx",
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


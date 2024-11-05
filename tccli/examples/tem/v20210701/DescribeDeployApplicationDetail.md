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
        "Result": {
            "DeployStrategyConf": {
                "TotalBatchCount": 0,
                "BetaBatchNum": 0,
                "DeployStrategyType": 0,
                "BatchInterval": 0,
                "MinAvailable": 0,
                "Force": true
            },
            "StartTime": "abc",
            "EndTime": "abc",
            "Status": "abc",
            "BetaBatchDetail": {
                "OldPodList": {
                    "PodId": "abc",
                    "PodStatus": [
                        "abc"
                    ],
                    "PodVersion": "abc",
                    "CreateTime": "abc",
                    "Zone": "abc",
                    "Webshell": "abc",
                    "Status": "abc"
                },
                "NewPodList": {
                    "PodId": "abc",
                    "PodStatus": [
                        "abc"
                    ],
                    "PodVersion": "abc",
                    "CreateTime": "abc",
                    "Zone": "abc",
                    "Webshell": "abc",
                    "Status": "abc"
                },
                "BatchStatus": "abc",
                "PodNum": 0,
                "BatchIndex": 0,
                "OldPods": [
                    {
                        "PodId": "abc",
                        "PodStatus": [
                            "abc"
                        ],
                        "PodVersion": "abc",
                        "CreateTime": "abc",
                        "Zone": "abc",
                        "Webshell": "abc",
                        "Status": "abc"
                    }
                ],
                "NextBatchStartTime": 0
            },
            "OtherBatchDetail": [
                {
                    "BatchStatus": "abc",
                    "PodNum": 0,
                    "BatchIndex": 0,
                    "NextBatchStartTime": 0
                }
            ],
            "OldVersionPodList": {
                "Offset": 0,
                "Limit": 0,
                "TotalCount": 0,
                "RequestId": "abc",
                "PodList": [
                    {
                        "Webshell": "abc",
                        "PodId": "abc",
                        "Status": "abc",
                        "CreateTime": "abc",
                        "PodIp": "abc",
                        "Zone": "abc",
                        "DeployVersion": "abc",
                        "RestartCount": 0,
                        "Ready": true,
                        "ContainerState": "abc",
                        "NodeInfo": {
                            "Name": "abc",
                            "Zone": "abc",
                            "SubnetId": "abc",
                            "AvailableIpCount": "abc",
                            "Cidr": "abc"
                        },
                        "StartTime": "abc",
                        "Unhealthy": true,
                        "UnhealthyWarningMsg": "abc",
                        "VersionId": "abc",
                        "ApplicationName": "abc"
                    }
                ]
            },
            "CurrentBatchIndex": 0,
            "ErrorMessage": "abc",
            "CurrentBatchStatus": "abc",
            "NewDeployVersion": "abc",
            "OldDeployVersion": "abc",
            "NewVersionPackageInfo": "abc",
            "NextBatchStartTime": 0
        },
        "RequestId": "abc-xxx-xxx"
    }
}
```


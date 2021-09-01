**Example 1: 查询升级状态**



Input: 

```
tccli tke GetUpgradeInstanceProgress --cli-unfold-argument  \
    --ClusterId cls-xxxxxx
```

Output: 
```
{
    "Response": {
        "LifeState": "xx",
        "Instances": [
            {
                "StartAt": "xx",
                "InstanceID": "xx",
                "Detail": [
                    {
                        "StartAt": "xx",
                        "Step": "xx",
                        "LifeState": "xx",
                        "EndAt": "xx",
                        "FailedMsg": "xx"
                    },
                    {
                        "LifeState": "xx",
                        "Step": "xx",
                        "StartAt": "xx",
                        "EndAt": "xx",
                        "FailedMsg": "xx"
                    },
                    {
                        "LifeState": "xx",
                        "Step": "xx",
                        "StartAt": "xx",
                        "EndAt": "xx",
                        "FailedMsg": "xx"
                    },
                    {
                        "LifeState": "xx",
                        "Step": "xx",
                        "StartAt": "xx",
                        "EndAt": "xx",
                        "FailedMsg": "xx"
                    }
                ],
                "EndAt": "xx",
                "CheckResult": {
                    "Items": [
                        {
                            "WorkLoadKind": "xx",
                            "After": 1,
                            "Namespace": "xx",
                            "WorkLoadName": "xx",
                            "Pods": [
                                "xx"
                            ],
                            "Before": 1
                        }
                    ],
                    "CheckPass": true,
                    "SinglePods": [
                        "xx"
                    ]
                },
                "LifeState": "xx"
            }
        ],
        "Done": 1,
        "RequestId": "xx",
        "ClusterStatus": {
            "PodTotal": 0,
            "NotReadyPod": 0
        },
        "Total": 3
    }
}
```


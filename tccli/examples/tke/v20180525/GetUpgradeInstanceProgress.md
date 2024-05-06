**Example 1: 查询升级状态**

查询升级状态

Input: 

```
tccli tke GetUpgradeInstanceProgress --cli-unfold-argument  \
    --ClusterId cls-xxxxxx
```

Output: 
```
{
    "Response": {
        "Total": 0,
        "Done": 0,
        "LifeState": "abc",
        "Instances": [
            {
                "InstanceID": "ins-wggphft5",
                "LifeState": "paused",
                "StartAt": "2021-02-08T16:29:46+08:00",
                "EndAt": "2021-02-08T16:39:46+08:00",
                "CheckResult": {
                    "CheckPass": false,
                    "Items": [
                        {
                            "Namespace": "default",
                            "WorkLoadKind": "ReplicaSet",
                            "WorkLoadName": "kubernetes-proxy-67fd23cf4d",
                            "Before": 1,
                            "After": 0,
                            "Pods": [
                                "kubernetes-proxy-67fd23cf4d-2tcxw"
                            ]
                        }
                    ],
                    "SinglePods": []
                },
                "Detail": [
                    {
                        "EndAt": null,
                        "FailedMsg": "precheck failed",
                        "LifeState": "failed",
                        "StartAt": "2023-02-08T08:29:51Z",
                        "Step": "preCheck"
                    },
                    {
                        "EndAt": null,
                        "FailedMsg": "",
                        "LifeState": "pending",
                        "StartAt": null,
                        "Step": "drain"
                    },
                    {
                        "EndAt": null,
                        "FailedMsg": "",
                        "LifeState": "pending",
                        "StartAt": null,
                        "Step": "remove"
                    },
                    {
                        "EndAt": null,
                        "FailedMsg": "",
                        "LifeState": "pending",
                        "StartAt": null,
                        "Step": "reset"
                    },
                    {
                        "EndAt": null,
                        "FailedMsg": "",
                        "LifeState": "pending",
                        "StartAt": null,
                        "Step": "postCheck"
                    }
                ]
            }
        ],
        "ClusterStatus": {
            "PodTotal": 10,
            "NotReadyPod": 0
        },
        "RequestId": "b224fa4b-fedf-4061-baa9-d547ew858df"
    }
}
```


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
        "ClusterStatus": {
            "PodTotal": 0,
            "NotReadyPod": 0
        },
        "Done": 0,
        "Instances": [
            {
                "CheckResult": {
                    "CheckPass": false,
                    "Items": [
                        {
                            "After": 0,
                            "Before": 2,
                            "Namespace": "default",
                            "Pods": [
                                "kubernetes-proxy-67fd23cf4d-2tcxw",
                                "kubernetes-proxy-67fd23cf4d-qd99j"
                            ],
                            "WorkLoadKind": "ReplicaSet",
                            "WorkLoadName": "kubernetes-proxy-67fd23cf4d"
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
                ],
                "EndAt": null,
                "InstanceID": "ins-wggphft5",
                "LifeState": "paused",
                "StartAt": "2023-02-08T16:29:46+08:00"
            }
        ],
        "LifeState": "aborted",
        "RequestId": "b224fa4b-fedf-4061-baa9-d547ew858df",
        "Total": 1
    }
}
```


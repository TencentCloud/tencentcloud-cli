**Example 1: 获取状态**

获取状态

Input: 

```
tccli monitor DescribeClusterAgentCreatingProgress --cli-unfold-argument  \
    --InstanceId prom-nr3w4z9e \
    --ClusterIds cls-pg4ft0gc
```

Output: 
```
{
    "Response": {
        "RequestId": "",
        "Response": [
            {
                "ClusterId": "cls-pg4ft0gc",
                "Status": "binding",
                "Steps": [
                    {
                        "EndAt": "2023-01-12T13:16:49Z",
                        "FailedMsg": "",
                        "LifeState": "success",
                        "StartAt": "2023-01-12T13:16:49Z",
                        "Step": "prepare_env"
                    },
                    {
                        "EndAt": "2023-01-12T13:16:50Z",
                        "FailedMsg": "",
                        "LifeState": "success",
                        "StartAt": "2023-01-12T13:16:49Z",
                        "Step": "check_target"
                    },
                    {
                        "EndAt": "2023-01-12T13:16:50Z",
                        "FailedMsg": "",
                        "LifeState": "success",
                        "StartAt": "2023-01-12T13:16:50Z",
                        "Step": "install_crd"
                    },
                    {
                        "EndAt": "2023-01-12T13:16:50Z",
                        "FailedMsg": "",
                        "LifeState": "success",
                        "StartAt": "2023-01-12T13:16:50Z",
                        "Step": "install_rbac"
                    },
                    {
                        "EndAt": "2023-01-12T13:16:52Z",
                        "FailedMsg": "",
                        "LifeState": "success",
                        "StartAt": "2023-01-12T13:16:50Z",
                        "Step": "install_agent"
                    },
                    {
                        "EndAt": "2023-01-12T13:17:43Z",
                        "FailedMsg": "",
                        "LifeState": "success",
                        "StartAt": "2023-01-12T13:16:52Z",
                        "Step": "install_cr"
                    },
                    {
                        "EndAt": "2023-01-12T13:17:45Z",
                        "FailedMsg": "",
                        "LifeState": "success",
                        "StartAt": "2023-01-12T13:17:43Z",
                        "Step": "install_basic"
                    }
                ]
            }
        ]
    }
}
```


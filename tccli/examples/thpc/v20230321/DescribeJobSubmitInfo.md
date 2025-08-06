**Example 1: 查询指定作业的提交信息**

查询指定作业的提交信息

Input: 

```
tccli thpc DescribeJobSubmitInfo --cli-unfold-argument  \
    --JobId job-7lbm9sss8
```

Output: 
```
{
    "Response": {
        "ClusterId": "hpc-qjwi17gr",
        "QueueName": "compute",
        "Job": {
            "JobName": "jobj-test",
            "JobDescription": "demo",
            "Priority": 1,
            "Tasks": [
                {
                    "TaskInstanceNum": 1,
                    "Application": {
                        "Commands": [
                            {
                                "Command": "sleep 30"
                            }
                        ],
                        "Docker": {
                            "Image": "ccr.ccs.tencentyun.com/taco/taco-train:ngc24.03-ofed5.8-hccpnv6-v1.0",
                            "RunArgs": [
                                "--privileged",
                                "--cap-add=IPC_LOCK",
                                "--ulimit memlock=-1",
                                "--ulimit stack=67108864",
                                "--net=host",
                                "--ipc=host",
                                "--gpus all"
                            ]
                        },
                        "JobType": "Custom"
                    },
                    "Timeout": 86400,
                    "TaskName": "Task_1"
                }
            ]
        },
        "RequestId": "d00db282-3ebb-438d-82da-73e376ff9b31"
    }
}
```


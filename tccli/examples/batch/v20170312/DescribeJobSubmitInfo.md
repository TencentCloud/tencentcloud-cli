**Example 1: 获取作业的提交信息**



Input: 

```
tccli batch DescribeJobSubmitInfo --cli-unfold-argument  \
    --JobId job-97zcl3wt
```

Output: 
```
{
    "Response": {
        "Tasks": [
            {
                "TaskInstanceNum": 2,
                "ComputeEnv": {
                    "EnvType": "MANAGED",
                    "EnvData": {
                        "InstanceType": "S1.SMALL1",
                        "ImageId": "img-bd78fy2t"
                    }
                },
                "RedirectInfo": {
                    "StdoutRedirectPath": "cos://bucket-appid.cosgz.myqcloud.com/hello2/logs/",
                    "StderrRedirectPath": "cos://bucket-appid..cosgz.myqcloud.com/hello2/logs/"
                },
                "Application": {
                    "Command": "python -c \"fib=lambda n:1 if n&lt=2 else fib(n-1)+fib(n-2); print(fib(20))\" ",
                    "DeliveryForm": "LOCAL"
                },
                "MaxRetryCount": 0,
                "FailedAction": "TERMINATE",
                "TaskName": "A"
            },
            {
                "TaskInstanceNum": 2,
                "ComputeEnv": {
                    "EnvType": "MANAGED",
                    "EnvData": {
                        "InstanceType": "S1.SMALL1",
                        "ImageId": "img-bd78fy2t"
                    }
                },
                "RedirectInfo": {
                    "StdoutRedirectPath": "cos://bucket-appid.cosgz.myqcloud.com/hello2/logs/",
                    "StderrRedirectPath": "cos://bucket-appid.cosgz.myqcloud.com/hello2/logs/"
                },
                "Application": {
                    "Command": "python -c \"fib=lambda n:1 if n&lt=2 else fib(n-1)+fib(n-2); print(fib(20))\" ",
                    "DeliveryForm": "LOCAL"
                },
                "MaxRetryCount": 0,
                "FailedAction": "TERMINATE",
                "TaskName": "B"
            },
            {
                "TaskInstanceNum": 2,
                "ComputeEnv": {
                    "EnvType": "MANAGED",
                    "EnvData": {
                        "InstanceType": "S1.SMALL1",
                        "ImageId": "img-bd78fy2t"
                    }
                },
                "RedirectInfo": {
                    "StdoutRedirectPath": "cos://bucket-appid.cosgz.myqcloud.com/hello2/logs/",
                    "StderrRedirectPath": "cos://bucket-appid.cosgz.myqcloud.com/hello2/logs/"
                },
                "Application": {
                    "Command": "python -c \"fib=lambda n:1 if n&lt=2 else fib(n-1)+fib(n-2); print(fib(20))\" ",
                    "DeliveryForm": "LOCAL"
                },
                "MaxRetryCount": 0,
                "FailedAction": "TERMINATE",
                "TaskName": "C"
            },
            {
                "TaskInstanceNum": 2,
                "ComputeEnv": {
                    "EnvType": "MANAGED",
                    "EnvData": {
                        "InstanceType": "S1.SMALL1",
                        "ImageId": "img-bd78fy2t"
                    }
                },
                "RedirectInfo": {
                    "StdoutRedirectPath": "cos://bucket-appid.cosgz.myqcloud.com/hello2/logs/",
                    "StderrRedirectPath": "cos://bucket-appid.cosgz.myqcloud.com/hello2/logs/"
                },
                "Application": {
                    "Command": "python -c \"fib=lambda n:1 if n&lt=2 else fib(n-1)+fib(n-2); print(fib(20))\" ",
                    "DeliveryForm": "LOCAL"
                },
                "MaxRetryCount": 0,
                "FailedAction": "TERMINATE",
                "TaskName": "D"
            }
        ],
        "Dependences": [
            {
                "StartTask": "A",
                "EndTask": "B"
            },
            {
                "StartTask": "A",
                "EndTask": "C"
            },
            {
                "StartTask": "B",
                "EndTask": "D"
            },
            {
                "StartTask": "C",
                "EndTask": "D"
            }
        ],
        "JobName": "test job",
        "Priority": 1,
        "JobDescription": "xxx",
        "JobId": "job-97zcl3wt",
        "Tags": [
            {
                "Key": "batch-test-tag-job-key",
                "Value": "batch-test-tag-job-value"
            }
        ],
        "RequestId": "1a69db97-95ff-4bf7-9eb2-875ea6e5737b"
    }
}
```


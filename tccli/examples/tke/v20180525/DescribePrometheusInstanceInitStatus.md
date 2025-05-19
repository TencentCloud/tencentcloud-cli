**Example 1: 获取初始化任务状态**



Input: 

```
tccli tke DescribePrometheusInstanceInitStatus --cli-unfold-argument  \
    --InstanceId abc
```

Output: 
```
{
    "Response": {
        "Status": "abc",
        "EksClusterId": "abc",
        "Steps": [
            {
                "StartAt": "abc",
                "Step": "abc",
                "LifeState": "abc",
                "EndAt": "abc",
                "FailedMsg": "abc"
            },
            {
                "LifeState": "abc",
                "Step": "abc",
                "StartAt": "abc",
                "EndAt": "abc",
                "FailedMsg": "abc"
            },
            {
                "LifeState": "abc",
                "Step": "abc",
                "StartAt": "abc",
                "EndAt": "abc",
                "FailedMsg": "abc"
            },
            {
                "LifeState": "abc",
                "Step": "abc",
                "StartAt": "abc",
                "EndAt": "abc",
                "FailedMsg": "abc"
            },
            {
                "LifeState": "abc",
                "Step": "abc",
                "StartAt": "abc",
                "EndAt": "abc",
                "FailedMsg": "abc"
            },
            {
                "LifeState": "abc",
                "Step": "abc",
                "StartAt": "abc",
                "EndAt": "abc",
                "FailedMsg": "abc"
            },
            {
                "LifeState": "abc",
                "Step": "abc",
                "StartAt": "abc",
                "EndAt": "abc",
                "FailedMsg": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```


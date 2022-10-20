**Example 1: 获取初始化任务状态**



Input: 

```
tccli tke DescribePrometheusInstanceInitStatus --cli-unfold-argument  \
    --InstanceId xx
```

Output: 
```
{
    "Response": {
        "Status": "xx",
        "EksClusterId": "xx",
        "Steps": [
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
        "RequestId": "xx"
    }
}
```

**Example 2: 获取2.0实例初始化任务状态**



Input: 

```
tccli tke DescribePrometheusInstanceInitStatus --cli-unfold-argument  \
    --InstanceId prom-7vp71ppt
```

Output: 
```
{
    "Response": {
        "Status": "xx",
        "EksClusterId": "xx",
        "Steps": [
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
        "RequestId": "xx"
    }
}
```


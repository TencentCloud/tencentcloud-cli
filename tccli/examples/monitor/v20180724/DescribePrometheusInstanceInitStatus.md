**Example 1: 获取初始化任务状态**

获取初始化任务状态

Input: 

```
tccli monitor DescribePrometheusInstanceInitStatus --cli-unfold-argument  \
    --InstanceId abc
```

Output: 
```
{
    "Response": {
        "Status": "abc",
        "Steps": [
            {
                "Step": "abc",
                "LifeState": "abc",
                "StartAt": "abc",
                "EndAt": "abc",
                "FailedMsg": "abc"
            }
        ],
        "EksClusterId": "abc",
        "RequestId": "abc"
    }
}
```

**Example 2: 获取2.0实例初始化任务状态**

获取2.0实例初始化任务状态

Input: 

```
tccli monitor DescribePrometheusInstanceInitStatus --cli-unfold-argument  \
    --InstanceId prom-7vp71ppt
```

Output: 
```
{
    "Response": {
        "Status": "abc",
        "Steps": [
            {
                "Step": "abc",
                "LifeState": "abc",
                "StartAt": "abc",
                "EndAt": "abc",
                "FailedMsg": "abc"
            }
        ],
        "EksClusterId": "abc",
        "RequestId": "abc"
    }
}
```


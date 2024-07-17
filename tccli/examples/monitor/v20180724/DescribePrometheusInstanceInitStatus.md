**Example 1: 获取初始化任务状态**

获取初始化任务状态

Input: 

```
tccli monitor DescribePrometheusInstanceInitStatus --cli-unfold-argument  \
    --InstanceId prom-asdf1234
```

Output: 
```
{
    "Response": {
        "Status": "initializing",
        "Steps": [
            {
                "Step": "preCheck",
                "LifeState": "success",
                "StartAt": "2022-04-19T07:29:46Z",
                "EndAt": "2022-04-19T07:30:46Z",
                "FailedMsg": "message"
            }
        ],
        "EksClusterId": "cls-asdf1234",
        "SecurityGroupId": "sg-asdf1234",
        "RequestId": "abc-123-asdfghjk"
    }
}
```

**Example 2: 获取2.0实例初始化任务状态**

获取2.0实例初始化任务状态

Input: 

```
tccli monitor DescribePrometheusInstanceInitStatus --cli-unfold-argument  \
    --InstanceId prom-asdf1234
```

Output: 
```
{
    "Response": {
        "Status": "initializing",
        "Steps": [
            {
                "Step": "preCheck",
                "LifeState": "success",
                "StartAt": "2022-04-19T07:29:46Z",
                "EndAt": "2022-04-19T07:30:46Z",
                "FailedMsg": "message"
            }
        ],
        "EksClusterId": "cls-asdf1234",
        "SecurityGroupId": "sg-asdf1234",
        "RequestId": "abc-123-asdfghjk"
    }
}
```


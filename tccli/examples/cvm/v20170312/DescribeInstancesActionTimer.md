**Example 1: 查询定时任务**



Input: 

```
tccli cvm DescribeInstancesActionTimer --cli-unfold-argument  \
    --InstanceIds ins-37qv3ucj
```

Output: 
```
{
    "Response": {
        "ActionTimers": [
            {
                "TimerAction": "TerminateInstances",
                "ActionTime": "2020-02-02 10:00:00",
                "Externals": {}
            }
        ],
        "RequestId": "af3ab130-244d-4c66-a8a0-03cad009f825"
    }
}
```


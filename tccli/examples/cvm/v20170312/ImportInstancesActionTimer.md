**Example 1: 导入定时任务**



Input: 

```
tccli cvm ImportInstancesActionTimer --cli-unfold-argument  \
    --ActionTimer.TimerAction TerminateInstances \
    --ActionTimer.ActionTime 2018-08-01 20:00:00 \
    --InstanceIds ins-37qv3ucj
```

Output: 
```
{
    "Response": {
        "ActionTimerIds": [
            "865d042d-0219-46c3-9821-6028c96cfb7c"
        ],
        "RequestId": "d4617dd8-071a-4bd6-aabf-f8026f757189"
    }
}
```


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
                "ActionTime": "2024-10-23T11:26:40Z",
                "ActionTimerId": "913d357c-ac08-449d-b283-5999f4fb7965",
                "Externals": {},
                "InstanceId": "ins-gs4iu6u3",
                "Status": "UNDO",
                "TimerAction": "TerminateInstances"
            }
        ],
        "RequestId": "a247225e-261b-4289-8426-feadc9a3c39c"
    }
}
```


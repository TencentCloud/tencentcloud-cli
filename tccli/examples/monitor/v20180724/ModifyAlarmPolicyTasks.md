**Example 1: 修改告警策略的触发任务**

修改告警策略的触发任务

Input: 

```
tccli monitor ModifyAlarmPolicyTasks --cli-unfold-argument  \
    --Module monitor \
    --PolicyId policy-29ng82fs \
    --TriggerTasks.0.Type AS \
    --TriggerTasks.0.TaskConfig {"Region":"ap-guangzhou","Group":"asg-0zhspjx","Policy":"asp-ganig28"}
```

Output: 
```
{
    "Response": {
        "RequestId": "29ghj2hh-45-h53h234h-23"
    }
}
```


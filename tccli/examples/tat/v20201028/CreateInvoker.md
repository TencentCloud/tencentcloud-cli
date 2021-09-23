**Example 1: 创建单次执行器**

北京时间 2021-09-01 00:00:00 在实例 ins-yx05ky8j 执行命令 cmd-m7uma92n

Input: 

```
tccli tat CreateInvoker --cli-unfold-argument  \
    --Name test-invoker \
    --CommandId cmd-m7uma92n \
    --InstanceIds ins-yx05ky8j \
    --Type SCHEDULE \
    --ScheduleSettings.Policy ONCE \
    --ScheduleSettings.InvokeTime 2021-09-01T00:00:00+08:00
```

Output: 
```
{
    "Response": {
        "RequestId": "97268137-e0f7-477d-833b-766273d0ea47",
        "InvokerId": "ivk-le1g3x2h"
    }
}
```

**Example 2: 创建周期执行命令**

在北京时间每月1日零点，在实例 ins-yx05ky8j 执行命令 cmd-m7uma92n

Input: 

```
tccli tat CreateInvoker --cli-unfold-argument  \
    --Name cron-invoker \
    --CommandId cmd-m7uma92n \
    --InstanceIds ins-yx05ky8j \
    --Type SCHEDULE \
    --ScheduleSettings.Policy RECURRENCE \
    --ScheduleSettings.Recurrence 0 0 1 * *
```

Output: 
```
{
    "Response": {
        "RequestId": "d1d7ce29-b6ac-436d-93e0-b454f096cc50",
        "InvokerId": "ivk-n0t6rxtv"
    }
}
```


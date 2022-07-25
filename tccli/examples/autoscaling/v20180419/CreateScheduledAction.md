**Example 1: 创建单次执行的定时任务**

创建定时任务，在指定时间（北京时间2018年8月28日23点）调整伸缩组的最大实例数、最小实例数和期望实例数至 10、4、6。

Input: 

```
tccli as CreateScheduledAction --cli-unfold-argument  \
    --DesiredCapacity 6 \
    --AutoScalingGroupId asg-2nr9xh8h \
    --MinSize 4 \
    --MaxSize 10 \
    --ScheduledActionName scheduled-action-0 \
    --StartTime 2018-08-28T23:00:00+08:00
```

Output: 
```
{
    "Response": {
        "ScheduledActionId": "asst-chwbkq4c",
        "RequestId": "193a710f-8dbf-46aa-8b4a-195532244df8"
    }
}
```

**Example 2: 创建重复执行的定时任务**

创建定时任务，从北京时间2018年8月28日开始，每天 23:00 调整伸缩组的最大实例数、最小实例数和期望实例数至 7、2、3，在北京时间2019年1月1日 00:00 后结束。

Input: 

```
tccli as CreateScheduledAction --cli-unfold-argument  \
    --Recurrence 0 23 */1 * * \
    --DesiredCapacity 3 \
    --AutoScalingGroupId asg-2nr9xh8h \
    --MinSize 2 \
    --MaxSize 7 \
    --ScheduledActionName scheduled-action-1 \
    --StartTime 2018-08-28T23:00:00+08:00 \
    --EndTime 2019-01-01T00:00:00+08:00
```

Output: 
```
{
    "Response": {
        "ScheduledActionId": "asst-le3us530",
        "RequestId": "502fd6fa-44ff-4c79-b77e-ee20f72bddc0"
    }
}
```


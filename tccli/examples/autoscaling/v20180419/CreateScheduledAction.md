**Example 1: Creating a single-run scheduled action**

This example shows you how to create a scheduled action to adjust the maximum, minimum, and desired capacity of the scaling group to 10, 4, and 6 respectively at 23:00, August 28, 2018 (UTC+8).

Input: 

```
tccli as CreateScheduledAction --cli-unfold-argument  \
    --AutoScalingGroupId asg-2nr9xh8h\
    --ScheduledActionName scheduled-action-0\
    --MaxSize 10\
    --MinSize 4\
    --DesiredCapacity 6\
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

**Example 2: Creating a recurring scheduled action**

This example shows you how to create a scheduled action to adjust the maximum, minimum, and desired capacity of a scaling group to 7, 2, and 3 respectively at 23:00 every day starting from August 28, 2018 and ending at 00:00, January 1, 2019 (UTC+8).

Input: 

```
tccli as CreateScheduledAction --cli-unfold-argument  \
    --AutoScalingGroupId asg-2nr9xh8h\
    --ScheduledActionName scheduled-action-1\
    --MaxSize 7\
    --MinSize 2\
    --DesiredCapacity 3\
    --StartTime 2018-08-28T23:00:00+08:00\
    --EndTime 2019-01-01T00:00:00+08:00\
    --Recurrence '0 23 */1 * *'
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


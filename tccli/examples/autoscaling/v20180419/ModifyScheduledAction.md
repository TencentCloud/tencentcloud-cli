**Example 1: Modifying a scheduled action**



Input: 

```
tccli as ModifyScheduledAction --cli-unfold-argument  \
    --ScheduledActionId asst-chwbkq4c \
    --ScheduledActionName scheduled-action-0 \
    --MaxSize 5 \
    --MinSize 0 \
    --DesiredCapacity 3 \
    --StartTime 2018-08-28T23:00:00+08:00
```

Output: 
```
{
    "Response": {
        "RequestId": "5f6f0f95-216f-4745-a2e6-617897e9cedb"
    }
}
```


**Example 1: 修改定时任务名称**



Input: 

```
tccli thpc ModifyScheduledAction --cli-unfold-argument  \
    --ScheduledActionId as-6be93212 \
    --ScheduledActionName scale-out-morning \
    --Status ACTIVE
```

Output: 
```
{
    "Response": {
        "RequestId": "f9540742-a232-4707-a2a7-7f358215e561"
    }
}
```


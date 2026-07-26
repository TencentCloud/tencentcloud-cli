**Example 1: 成功**



Input: 

```
tccli adp ModifyAppTrigger --cli-unfold-argument  \
    --AppId 2072866150944382336 \
    --Trigger.TriggerName 每隔30分钟执行一次 \
    --TriggerId 64201696-52ee-49f6-a95b-0773b60a8e6b \
    --UpdateMask.Paths TriggerName
```

Output: 
```
{
    "Response": {
        "RequestId": "4a0ed855-acc1-4bd1-b297-119dc5f5b5ab"
    }
}
```


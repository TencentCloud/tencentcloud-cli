**Example 1: CreateTimerTask**



Input: 

```
tccli adp CreateTimerTask --cli-unfold-argument  \
    --CreateSource 1 \
    --Prompt 1 \
    --Schedule.ManualOnly.Enabled True \
    --Schedule.ScheduleType 1 \
    --SpaceId default_space \
    --TaskName 1
```

Output: 
```
{
    "Response": {
        "TimerId": "bbe5163d-7900-4230-941a-9b196a9bdfcc",
        "RequestId": "6d08ceab-46df-4a07-a1be-0fd325b1ef02"
    }
}
```


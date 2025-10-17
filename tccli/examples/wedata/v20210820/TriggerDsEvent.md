**Example 1: 触发事件**

触发事件

Input: 

```
tccli wedata TriggerDsEvent --cli-unfold-argument  \
    --ProjectId 1470547050521227264 \
    --EventCaseList.0.Name event_0811 \
    --EventCaseList.0.Dimension 20250811 \
    --ScheduleTimeZone UTC+8
```

Output: 
```
{
    "Response": {
        "Data": {
            "FailCount": 0,
            "FailMessageList": [],
            "SuccessCount": 1,
            "TotalCount": 1
        },
        "RequestId": "edf02697-ae38-49f2-8682-057fd340d197"
    }
}
```


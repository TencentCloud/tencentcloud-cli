**Example 1: 删除任务告警规则**



Input: 

```
tccli wedata DeleteTaskAlarmRegular --cli-unfold-argument  \
    --ProjectId xx \
    --Id xx \
    --TaskId xx \
    --TaskType 0
```

Output: 
```
{
    "Response": {
        "Data": true,
        "RequestId": "xx"
    }
}
```


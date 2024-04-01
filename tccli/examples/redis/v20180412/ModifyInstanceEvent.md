**Example 1: 修改实例事件信息**

修改实例事件信息

Input: 

```
tccli redis ModifyInstanceEvent --cli-unfold-argument  \
    --InstanceId crs-b6wst31p \
    --EventId 10 \
    --StartTime 22:00 \
    --EndTime 23:01 \
    --ExecutionDate 2023-09-18
```

Output: 
```
{
    "Response": {
        "EventId": 10,
        "RequestId": "abc"
    }
}
```


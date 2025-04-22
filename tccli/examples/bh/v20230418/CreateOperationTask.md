**Example 1: 创建周期性运维任务**



Input: 

```
tccli bh CreateOperationTask --cli-unfold-argument  \
    --Name 周期运维任务 \
    --Type 2 \
    --Period 1 \
    --FirstTime 2025-03-25T08:00:01+08:00 \
    --Account root \
    --Timeout 5 \
    --Script ls \
    --Encoding 1 \
    --DeviceIdSet 34 56
```

Output: 
```
{
    "Response": {
        "TaskId": 10,
        "RequestId": "31js-hapqhxmaj-h12knsk2weq"
    }
}
```

**Example 2: 创建运维任务**



Input: 

```
tccli bh CreateOperationTask --cli-unfold-argument  \
    --Name 运维任务 \
    --Type 1 \
    --Account root \
    --Timeout 5 \
    --Script ls -al \
    --Encoding 0 \
    --DeviceIdSet 44 66
```

Output: 
```
{
    "Response": {
        "TaskId": 11,
        "RequestId": "31sfasw-ewffq-wesvfxvd"
    }
}
```


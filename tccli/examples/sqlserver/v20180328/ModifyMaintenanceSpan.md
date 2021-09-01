**Example 1: 修改实例的可维护时间窗**

修改实例的可维护时间窗：修改为每周的周一，周二，周三，从0点开始持续6个小时。

Input: 

```
tccli sqlserver ModifyMaintenanceSpan --cli-unfold-argument  \
    --InstanceId mssql-6upluvd5 \
    --StartTime 00:00 \
    --Span 6 \
    --Weekly 1 2 3
```

Output: 
```
{
    "Response": {
        "RequestId": "2941128b-d8fb-4af4-bb73-d79c413e1a7d"
    }
}
```


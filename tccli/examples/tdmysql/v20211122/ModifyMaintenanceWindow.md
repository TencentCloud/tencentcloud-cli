**Example 1: 修改运维窗口时间**



Input: 

```
tccli tdmysql ModifyMaintenanceWindow --cli-unfold-argument  \
    --InstanceId tdsql3-99c63ac1 \
    --StartTime 04:33 \
    --Duration 3 \
    --WeekDays Friday
```

Output: 
```
{
    "Response": {
        "RequestId": "153a2f65-5593-4cc3-9e5c-66d72da44450"
    }
}
```


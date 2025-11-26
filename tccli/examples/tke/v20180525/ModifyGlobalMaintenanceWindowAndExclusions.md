**Example 1: 更新全局维护窗口和排除项**

更新一个全局维护窗口和排除项

Input: 

```
tccli tke ModifyGlobalMaintenanceWindowAndExclusions --cli-unfold-argument  \
    --ID 1 \
    --TargetRegions * \
    --MaintenanceTime 20:00:00 \
    --Duration 4 \
    --DayOfWeek MO WE
```

Output: 
```
{
    "Response": {
        "RequestId": "f1048559-c7e4-4a7b-9d12-bc0256be3e26"
    }
}
```


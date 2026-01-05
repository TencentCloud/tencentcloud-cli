**Example 1: 任务部分属性更新**

任务部分属性更新

Input: 

```
tccli wedata UpdateTaskPartially --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --TaskId 20251009170834756 \
    --NewSetting.TaskBaseAttribute.TaskName hive_1 \
    --NewSetting.TaskConfiguration.CodeContent LS1IaXZlIFNRTAotLSoqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKi0tCi0tYXV0aG9yOiBrZXZpbm5pZQotLWNyZWF0ZSB0aW1lOiAyMDI1LTEwLTA5IDE3OjA4OjMwCi0tKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqLS0Kc2VsZWN0IDE= \
    --NewSetting.TaskConfiguration.SourceServiceId 8444 \
    --FieldToRemoveList TaskSchedulerConfiguration/DownStreamDependencyConfigList:20250123151934646
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": true
        },
        "RequestId": "1548f7fd-1bba-4aeb-95e1-82e36643f721"
    }
}
```


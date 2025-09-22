**Example 1: 成功**

查询工作流信息成功

Input: 

```
tccli wedata GetWorkflow --cli-unfold-argument  \
    --ProjectId 1486804694126882816 \
    --WorkflowId 0b785b8d-bd8e-4513-be65-36f989bc8a64
```

Output: 
```
{
    "Response": {
        "Data": {
            "BundleId": null,
            "BundleInfo": null,
            "CreateUserUin": "100043191163",
            "OwnerUin": "100043191163",
            "Path": "/u9ed8u8ba4u6587u4ef6u5939/u6620u5c04u573au666f2",
            "WorkflowDesc": "",
            "WorkflowName": "u6620u5c04u573au666f2",
            "WorkflowParams": [],
            "WorkflowSchedulerConfiguration": {
                "CalendarId": "105",
                "CalendarName": "u4ea4u6613u6240u65e5u5386",
                "CalendarOpen": "1",
                "CrontabExpression": "0 0 0 * * ?",
                "CycleType": "HOUR_CYCLE",
                "DependencyWorkflow": "no",
                "EndTime": "2099-12-31 23:59:59",
                "ExecutionEndTime": "23:59",
                "ExecutionStartTime": "00:00",
                "ScheduleTimeZone": "UTC+8",
                "SelfDepend": "serial",
                "StartTime": "2025-09-11 00:00:00"
            },
            "WorkflowType": "cycle"
        },
        "RequestId": "c1ee28f6-319f-43aa-8fa5-a26d2865518e"
    }
}
```


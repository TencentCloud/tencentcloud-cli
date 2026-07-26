**Example 1: DescribeTimerTask**



Input: 

```
tccli adp DescribeTimerTask --cli-unfold-argument  \
    --SpaceId default_space \
    --TimerId bbe5163d-7900-4230-941a-9b196a9bdfcc
```

Output: 
```
{
    "Response": {
        "Task": {
            "Config": {
                "PushConfig": {
                    "PushChannel": 1,
                    "PushTargetId": "",
                    "PushTargetType": 2
                },
                "Schedule": {
                    "ManualOnly": {},
                    "ScheduleType": 1,
                    "Timezone": "Asia/Shanghai"
                }
            },
            "OwnerUserId": "1932008810606356480",
            "PolicySummary": "仅手动触发",
            "Profile": {
                "CreateSource": 1,
                "InputContextSnapshot": "",
                "ModelId": "TCADP/glm-5.1",
                "Prompt": "你好",
                "SkillSnapshot": "",
                "TaskName": "你好任务",
                "ToolSnapshot": "",
                "WorkspaceId": "default-folder"
            },
            "SpaceId": "default_space",
            "Status": {
                "FailedCount": "0",
                "LastFireTime": "",
                "LastSessionId": "",
                "NextFireTime": "",
                "Status": 1,
                "SuccessCount": "0",
                "UnreadRunLogCount": "0"
            },
            "TimerId": "bbe5163d-7900-4230-941a-9b196a9bdfcc"
        },
        "RequestId": "29cd28a7-931e-4af6-aef9-909a2e274189"
    }
}
```


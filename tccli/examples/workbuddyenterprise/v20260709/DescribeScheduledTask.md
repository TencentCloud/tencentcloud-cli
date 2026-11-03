**Example 1: 查看任务详情**



Input: 

```
tccli workbuddyenterprise DescribeScheduledTask --cli-unfold-argument  \
    --TaskId 1001
```

Output: 
```
{
    "Response": {
        "TaskId": 1001,
        "TaskKey": "task-20260720090000-a1b2c3",
        "TaskName": "每日晨报",
        "Description": "工作日报",
        "AgentId": "ag-xxx",
        "CronExpr": "0 0 9 * * *",
        "DeliveryTargetSet": [
            {
                "Type": "BOT_CHANNEL",
                "Enabled": true,
                "Options": {
                    "ChannelType": "QQ",
                    "ChannelId": "1905263717",
                    "RecipientIdSet": [
                        "oc_xxx"
                    ]
                }
            }
        ],
        "Status": "ACTIVE",
        "LastRunTime": "",
        "NextRunTime": "2026-07-21T09:00:00+08:00",
        "CreatedTime": "2026-07-20T09:00:00+08:00",
        "ModifiedTime": "2026-07-20T09:00:00+08:00",
        "RequestId": "3c6d138e-1234-5678-9abc-def012345678",
        "AgentConfig": {
            "Prompt": "总结昨天的项目进展",
            "AgentId": "ag-xxx"
        }
    }
}
```


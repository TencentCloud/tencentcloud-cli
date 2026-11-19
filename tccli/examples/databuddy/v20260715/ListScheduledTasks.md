**Example 1: 查询工作空间下的定时任务**

分页查询命中一条任务

Input: 

```
tccli databuddy ListScheduledTasks --cli-unfold-argument  \
    --WorkspaceId 17761588656557477
```

Output: 
```
{
    "Response": {
        "Data": {
            "Tasks": [
                {
                    "ScheduledTaskId": "59800",
                    "Name": "每日精选任务-1",
                    "Prompt": "分析今日数据趋势并生成报告",
                    "Schedule": "0 0 9 * * *",
                    "Status": 1,
                    "SessionType": 1,
                    "AnalysisSpaceId": "as-1024",
                    "WorkspaceId": "17761588656557477",
                    "CreateUserUin": "700002164618",
                    "CreateTime": "1779273675952",
                    "ModifyTime": "1779274998199",
                    "StartTime": "1759161600000",
                    "EndTime": "0",
                    "SkillIds": "skill-abnormal-detect",
                    "ModelId": "hunyuan-turbo",
                    "ScheduleType": 1,
                    "UpdateUserUin": "700002164618",
                    "MCPIds": "mcp-github-001,mcp-jira-002"
                }
            ],
            "Total": 1,
            "Page": 1,
            "PageSize": 20
        },
        "RequestId": "991014a1-bbb8-4610-a814-896725742863"
    }
}
```


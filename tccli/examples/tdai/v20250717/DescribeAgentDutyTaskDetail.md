**Example 1: 查询值守任务详情**

用于查询智能体后台值守任务详情

Input: 

```
tccli tdai DescribeAgentDutyTaskDetail --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AgentDutyTask": {
            "TaskId": "task-x89ool0j",
            "CreateTime": "2025-09-01 10:00:00",
            "FinishTime": "0000-00-00 00:00:00",
            "Status": "running",
            "ResultExtraKey": [],
            "Extra": []
        },
        "RequestId": "4744e0fa-7827-4ae6-8eda-f5de924e1adb"
    }
}
```


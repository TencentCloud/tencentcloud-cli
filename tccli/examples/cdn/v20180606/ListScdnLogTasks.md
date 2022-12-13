**Example 1: 查询SCDN事件日志下载任务列表**



Input: 

```
tccli cdn ListScdnLogTasks --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "TaskList": [
            {
                "Status": "created",
                "Domain": "test.com",
                "StartTime": "2020-09-22 00:00:00",
                "Area": "mainland",
                "DefenceMode": "observe",
                "DownloadUrl": "https://downlaod.com",
                "Mode": "waf",
                "AttackType": "xss",
                "TaskID": "taskId",
                "EndTime": "2020-09-22 00:00:00",
                "Conditions": [
                    {
                        "Operator": "include",
                        "Value": "10.0.0.1",
                        "Key": "ip"
                    }
                ],
                "CreateTime": "2020-09-22 00:00:00"
            }
        ],
        "RequestId": "1abbe623-4b0e-4727-ab51-7624902d47f4"
    }
}
```


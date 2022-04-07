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
                "Status": "xx",
                "Domain": "xx",
                "StartTime": "2020-09-22 00:00:00",
                "Area": "xx",
                "DefenceMode": "xx",
                "DownloadUrl": "xx",
                "Mode": "xx",
                "AttackType": "xx",
                "TaskID": "xx",
                "EndTime": "2020-09-22 00:00:00",
                "Conditions": [
                    {
                        "Operator": "xx",
                        "Value": "xx",
                        "Key": "xx"
                    }
                ],
                "CreateTime": "2020-09-22 00:00:00"
            }
        ],
        "RequestId": "xx"
    }
}
```


**Example 1: 查询任务**



Input: 

```
tccli ses ListSendTasks --cli-unfold-argument  \
    --Status 1 \
    --Offset 1 \
    --Limit 1 \
    --ReceiverId 123 \
    --TaskType 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Data": [
            {
                "CacheCount": 1,
                "UpdateTime": "2021-09-09 10:10:10",
                "SendCount": 1,
                "TimedParam": {
                    "BeginTime": "2021-09-09 10:10:10"
                },
                "FromEmailAddress": "abc@cd.com",
                "TaskStatus": 1,
                "ReceiverId": 1,
                "RequestCount": 1,
                "TaskId": "123",
                "TaskType": 1,
                "Template": {
                    "TemplateData": "{\"name\":\"name\"}",
                    "TemplateID": 1
                },
                "CycleParam": {
                    "IntervalTime": 1,
                    "BeginTime": "2021-09-09 10:10:10",
                    "TermCycle": 1
                },
                "CreateTime": "2021-09-09 10:10:10",
                "Subject": "邮件主题",
                "ErrMsg": "",
                "ReceiversName": "名称"
            }
        ],
        "RequestId": "xx"
    }
}
```


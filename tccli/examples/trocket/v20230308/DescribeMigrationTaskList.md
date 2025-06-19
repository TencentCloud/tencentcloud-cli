**Example 1: 获取数据迁移任务列表**



Input: 

```
tccli trocket DescribeMigrationTaskList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "RequestId": "bd8c6783-04a4-419f-bc51-9af603872490",
        "TotalCount": 1,
        "Tasks": [
            {
                "TaskId": "603872-7a11-c67",
                "Type": 1,
                "InstanceId": "rmq-47zbegoa",
                "TopicNum": 4,
                "GroupNum": 0,
                "Status": 1,
                "CreateTime": 1693219938000
            }
        ]
    }
}
```


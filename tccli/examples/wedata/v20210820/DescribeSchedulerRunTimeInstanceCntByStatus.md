**Example 1: 实例运行时长排行示例**

实例运行时长排行示例

Input: 

```
tccli wedata DescribeSchedulerRunTimeInstanceCntByStatus --cli-unfold-argument  \
    --ProjectId 1 \
    --TimeUnit 12h
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "TaskId": "1",
                "TaskName": "taskName",
                "InCharge": ";jaydenjhu;",
                "CycleUnit": "I",
                "State": "RUNNING",
                "RunTime": 27220,
                "WaitScheduleTime": 1234,
                "CurRunTime": "2023-01-01 12:12:12"
            }
        ],
        "RequestId": "12312312"
    }
}
```


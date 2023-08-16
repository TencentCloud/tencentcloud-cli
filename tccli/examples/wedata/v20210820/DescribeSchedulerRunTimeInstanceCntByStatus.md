**Example 1: 示例1**

Demo

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
                "CurRunTime": "2023-01-01 12:12:12"
            }
        ],
        "RequestId": "12312312"
    }
}
```

**Example 2: 1**

1

Input: 

```
tccli wedata DescribeSchedulerRunTimeInstanceCntByStatus --cli-unfold-argument  \
    --ProjectId 1 \
    --CycleUnit 1 \
    --TimeUnit 1 \
    --StartTime 1 \
    --EndTime 1 \
    --TaskType 1 \
    --InCharge 1
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "UnauthorizedOperation",
            "Message": "未授权操作"
        },
        "RequestId": "23a27e89-4bc1-4572-8efb-7a77f155d743"
    }
}
```


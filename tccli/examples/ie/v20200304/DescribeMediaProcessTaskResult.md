**Example 1: 查询编辑处理任务结果**



Input: 

```
tccli ie DescribeMediaProcessTaskResult --cli-unfold-argument  \
    --TaskId 12001326083614739554304
```

Output: 
```
{
    "Response": {
        "TaskResult": {
            "ErrCode": 100,
            "ErrMsg": "Task is under processing.",
            "MediaCuttingTaskResult": null,
            "Progress": 24,
            "Status": 1200,
            "TaskId": "12001331787046041444352",
            "Type": "MediaCutting"
        },
        "RequestId": "e4de90c2-2836-44d4-8513-f4ff06596fe9"
    }
}
```


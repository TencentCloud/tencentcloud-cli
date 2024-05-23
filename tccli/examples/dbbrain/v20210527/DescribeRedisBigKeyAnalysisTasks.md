**Example 1: 获取Redis大Key分析任务列表**

获取某个Redis实例的大Key分析任务列表。

Input: 

```
tccli dbbrain DescribeRedisBigKeyAnalysisTasks --cli-unfold-argument  \
    --InstanceId crs-7i2test \
    --Product redis \
    --Limit 50 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Tasks": [
            {
                "Progress": 100,
                "AsyncRequestId": 7309733,
                "EndTime": "2024-01-12 11:41:53",
                "CreateTime": "2024-01-12 11:38:37",
                "StartTime": "2024-01-12 11:38:38",
                "TaskStatus": "finished",
                "ShardIds": [
                    "2",
                    "3"
                ]
            }
        ],
        "RequestId": "e9833850-b113-11ee-8376-93f024a9a001"
    }
}
```


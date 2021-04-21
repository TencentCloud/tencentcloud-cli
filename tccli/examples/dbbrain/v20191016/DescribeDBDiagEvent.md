**Example 1: 获取诊断事件详情**



Input: 

```
tccli dbbrain DescribeDBDiagEvent --cli-unfold-argument  \
    --InstanceId test \
    --EventId 5
```

Output: 
```
{
    "Response": {
        "Suggestions": "[]",
        "DiagType": "数据库快照",
        "EndTime": "2019-11-06 12:05:50",
        "RequestId": "78cf7bb1-0608-11ea-a9ef-2736f0f7f829",
        "Explanation": "[]",
        "StartTime": "2019-11-06 12:05:40",
        "Severity": 4,
        "EventId": 5,
        "Outline": "数据库健康检查，发现1个问题",
        "Problem": "[{\"DataType\":\"title\",\"Data\":{\"Name\":\"会话快照\"}},{\"DataType\":\"title\",\"Data\":{\"Name\":\"事务快照\"}},{\"DataType\":\"title\",\"Data\":{\"Name\":\"Innodb状态快照\"}}]",
        "Metric": "",
        "DiagItem": "健康巡检"
    }
}
```


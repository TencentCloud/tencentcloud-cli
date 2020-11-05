**Example 1: Getting diagnosis event details**



Input: 

```
tccli dbbrain DescribeDBDiagEvent --cli-unfold-argument  \
    --InstanceId test\
    --EventId 5
```

Output: 
```
{
    "Response": {
        "Suggestions": "[]",
        "DiagType": "Database snapshot",
        "EndTime": "2019-11-06 12:05:50",
        "RequestId": "78cf7bb1-0608-11ea-a9ef-2736f0f7f829",
        "Explanation": "[]",
        "StartTime": "2019-11-06 12:05:40",
        "EventId": 5,
        "Severity": 4,
        "Outline": "1 problem found during database health check",
        "Problem": "[{\"DataType\":\"title\",\"Data\":{\"Name\":\"Session snapshot\"}},{\"DataType\":\"title\",\"Data\":{\"Name\":\"Transaction snapshot\"}},{\"DataType\":\"title\",\"Data\":{\"Name\":\"InnoDB status snapshot\"}}]",
        "Metric": "",
        "DiagItem": "Health check"
    }
}
```


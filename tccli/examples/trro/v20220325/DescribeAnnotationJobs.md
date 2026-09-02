**Example 1: 调用示例1**



Input: 

```
tccli trro DescribeAnnotationJobs --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --Status 1 \
    --InputPath ai-annotation-test-input
```

Output: 
```
{
    "Response": {
        "Jobs": [
            {
                "AnnotationType": 3,
                "CreateTime": "1788184838",
                "FinishTime": "0",
                "IngestStatus": 1,
                "InputPath": "ai-annotation-test-input-1258344699/batch-test/1qLIfbvfNo_0099.mp4",
                "JobId": "3ufulistdemo01",
                "JobType": 1,
                "Status": 1,
                "TotalNumber": 2
            }
        ],
        "Limit": 10,
        "Offset": 0,
        "TotalCount": 4,
        "RequestId": "c814dcbd-4269-49d6-999f-da2eea7ee42f"
    }
}
```


**Example 1: 调用示例1**



Input: 

```
tccli trro DescribeAnnotationTasks --cli-unfold-argument  \
    --JobId 3ueigpf29yac \
    --Offset 0 \
    --Limit 10 \
    --FileName 1qLI \
    --Status 1
```

Output: 
```
{
    "Response": {
        "JobId": "3ueigpf29yac",
        "Limit": 10,
        "Offset": 0,
        "Tasks": [
            {
                "CreateTime": "1788184646",
                "ErrorMsg": "",
                "FileName": "1qLIfbvfNo_0099.mp4",
                "FinishTime": "0",
                "InputPath": "ai-annotation-test-input-1258344699/batch-test/1qLIfbvfNo_0099.mp4",
                "Status": 1,
                "TaskId": "3ueigpf29yac_99"
            }
        ],
        "TotalCount": 1,
        "RequestId": "6f129a1c-7ddd-48a4-b298-bfb8273d4d97"
    }
}
```

**Example 2: 调用示例2**



Input: 

```
tccli trro DescribeAnnotationTasks --cli-unfold-argument  \
    --JobId 3ufulistdemo01 \
    --Offset 0 \
    --Limit 10 \
    --Status 4
```

Output: 
```
{
    "Response": {
        "JobId": "3ufulistdemo01",
        "Limit": 10,
        "Offset": 0,
        "Tasks": [
            {
                "CreateTime": "1788184838",
                "ErrorMsg": "stage2 semantic failed: VLM call timeout after 3 retries",
                "FileName": "1qLIfbvfNo_0098.mp4",
                "FinishTime": "1788185661",
                "InputPath": "ai-annotation-test-input-1258344699/batch-test/1qLIfbvfNo_0098.mp4",
                "Status": 4,
                "TaskId": "3ufulistdemo01_1"
            }
        ],
        "TotalCount": 1,
        "RequestId": "f23d2625-15d8-4180-bdd9-3d2c35d116c2"
    }
}
```


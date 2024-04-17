**Example 1: 查询工作流任务数**

查询工作流任务数

Input: 

```
tccli wedata DescribeWorkflowTaskCount --cli-unfold-argument  \
    --ProjectId 1531609690365952 \
    --WorkflowId 92b97aae-699a-11ee-8d13-a4ae120f8272
```

Output: 
```
{
    "Response": {
        "Data": {
            "Count": 7,
            "CycleCount": [
                {
                    "Key": "D",
                    "Value": "4"
                },
                {
                    "Key": "I",
                    "Value": "1"
                },
                {
                    "Key": "O",
                    "Value": "2"
                }
            ],
            "TypeCount": [
                {
                    "Key": "离线同步",
                    "Value": "1"
                },
                {
                    "Key": "Shell",
                    "Value": "4"
                },
                {
                    "Key": "JDBC SQL",
                    "Value": "2"
                }
            ]
        },
        "RequestId": "44d59b5b-a3a7-40d5-a2ef-edb0c3ba0f0a"
    }
}
```


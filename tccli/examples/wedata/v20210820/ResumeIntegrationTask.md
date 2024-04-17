**Example 1: 继续集成任务**

继续集成任务

Input: 

```
tccli wedata ResumeIntegrationTask --cli-unfold-argument  \
    --TaskId 4c187b4a-394b-4eb7-b9b0-948ca0552378 \
    --ProjectId 1486446569620893696 \
    --Event RESUME \
    --ExtConfig.0.Name timestamp \
    --ExtConfig.0.Value 1686811933000
```

Output: 
```
{
    "Response": {
        "Data": true,
        "RequestId": "b214be7-c5a0-44ca-bd92-9d21a68e2931"
    }
}
```


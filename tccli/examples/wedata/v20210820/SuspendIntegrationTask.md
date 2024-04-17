**Example 1: 暂停集成任务**

暂停集成任务

Input: 

```
tccli wedata SuspendIntegrationTask --cli-unfold-argument  \
    --ProjectId 1486446569620893696 \
    --TaskId v234b22e9-69d0-43e1-800f-420d6a468abc \
    --Event SUSPEND_WITHOUT_SP
```

Output: 
```
{
    "Response": {
        "RequestId": "bb214be7-c5a0-44ca-bd92-9d21a68e2931",
        "Data": true
    }
}
```


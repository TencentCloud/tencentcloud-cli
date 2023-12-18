**Example 1: 暂停集成任务**

暂停集成任务

Input: 

```
tccli wedata SuspendIntegrationTask --cli-unfold-argument  \
    --ProjectId 1123567888 \
    --TaskId v234b22e9-69d0-43e1-800f-420d6a468abc \
    --Event SUSPEND_WITHOUT_SP
```

Output: 
```
{
    "Response": {
        "RequestId": "abcdefj56789",
        "Data": true
    }
}
```


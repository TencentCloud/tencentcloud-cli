**Example 1: 获取异步任务执行结果**

获取异步任务执行结果,可以从RemoveDatabase,RemoveSchema中获取JobId

Input: 

```
tccli wedata GetJobStatus --cli-unfold-argument  \
    --JobId 244
```

Output: 
```
{
    "Response": {
        "Completed": true,
        "CreateTime": "1751612208000",
        "ErrorMessage": "",
        "JobId": "244",
        "RequestId": "5d9d6049-167c-43f6-bdc4-1acb37a39559",
        "Status": "SUCCESS"
    }
}
```


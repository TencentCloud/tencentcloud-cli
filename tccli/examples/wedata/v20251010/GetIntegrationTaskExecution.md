**Example 1: 查询任务调试执行信息**



Input: 

```
tccli wedata GetIntegrationTaskExecution --cli-unfold-argument  \
    --WorkspaceId 17623497097012366 \
    --TaskId f5aaa5c0-5ace-4904-8ee3-79f9b6869bc1
```

Output: 
```
{
    "Response": {
        "Data": {
            "CreateTime": "1767865432916",
            "ExecJobStatus": "COMPLETED",
            "JobId": "6820260108174352028",
            "ResourceGroupId": "resource_1",
            "RunParams": "{'pt':20260119}",
            "RunUserName": "wedata30-dev@tencent.com",
            "RunUserUin": "700002164618",
            "TaskId": "f5aaa5c0-5ace-4904-8ee3-79f9b6869bc1",
            "TaskName": "MYSQL_20260106_163141",
            "TaskVersion": "20260106190916",
            "WorkspaceId": "17623497097012366"
        },
        "RequestId": "5e460685-6381-4cb2-969c-edd6e615d417"
    }
}
```


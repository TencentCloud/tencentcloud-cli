**Example 1: 查询作业的taskmanger和subtask**

查询作业的taskmanger和subtask

Input: 

```
tccli oceanus DescribeJobRuntimeInfo --cli-unfold-argument  \
    --JobId cql-xxx \
    --WorkSpaceId space-xxx \
    --IncludeInfo TaskManagers SubTasks
```

Output: 
```
{
    "Response": {
        "JobRuntimeInfo": [
            {
                "Key": "TaskManagers",
                "Value": "WyJjcWwtbDkzZzJ3eGotNDI0MS10YXNrbWFuYWdlci0xLTEiXQ=="
            },
            {
                "Key": "SubTasks",
                "Value": "W3siVGFza0lkIjoiY2JjMzU3Y2NiNzYzZGYyODUyZmVlOGM0ZmM3ZDU1ZjIiLCJUYXNrRGVzY3JpcHRpb24iOiJTb3VyY2U6IFRhYmxlU291cmNlU2Nhbih0YWJsZT1bW2RlZmF1bHRfY2F0YWxvZywgZGVmYXVsdF9kYXRhYmFzZSwgZGF0YWdlbl9zb3VyY2VfdGFibGVdXSwgZmllbGRzPVtpZCwgbmFtZV0pIC1cdTAwMjZndDsgU2luazogU2luayh0YWJsZT1bZGVmYXVsdF9jYXRhbG9nLmRlZmF1bHRfZGF0YWJhc2UubG9nZ2VyX3NpbmtfdGFibGVdLCBmaWVsZHM9W2lkLCBuYW1lXSlfMCIsIlN1YlRhc2tJbmRleCI6MH1d"
            }
        ],
        "RequestId": "51964833-6e61-4909-b93b-3d4996c9360d"
    }
}
```


**Example 1: 提交代码**



Input: 

```
tccli tchousex CreateNotebookSessionStatement --cli-unfold-argument  \
    --SessionId livy-session-8pu64i \
    --Code c2MudmVyc2lvbgo= \
    --Kind spark
```

Output: 
```
{
    "Response": {
        "RequestId": "301aa5ff-436e-45cd-aaf8-3f81c5eb015d",
        "ErrorMsg": "",
        "NotebookSessionStatement": {
            "StatementId": "1",
            "Code": "sc.version\n",
            "Output": {
                "Status": "",
                "ExecutionCount": 0,
                "Data": "null"
            },
            "State": "waiting",
            "Progress": 0,
            "Started": 0,
            "Completed": 0
        }
    }
}
```


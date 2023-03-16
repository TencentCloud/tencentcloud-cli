**Example 1: 获取函数运行日志**

获取函数运行日志

Input: 

```
tccli scf GetFunctionLogs --cli-unfold-argument  \
    --FunctionName <FunctionName>
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Data": [
            {
                "MemUsage": 3174400,
                "RetCode": 1,
                "RetMsg": "Success",
                "Log": "",
                "BillDuration": 100,
                "InvokeFinished": 1,
                "RequestId": "bc309eaa-6d64-11e8-a7fe-5254000b4175",
                "StartTime": "2018-06-11 18:46:45",
                "Duration": 0.532,
                "FunctionName": "APITest",
                "Level": "",
                "Source": "",
                "RetryNum": 1
            }
        ],
        "SearchContext": {
            "Offset": "",
            "Limit": 0,
            "Keyword": "",
            "Type": ""
        },
        "RequestId": "e2571ff3-da04-4c53-8438-f58bf057ce4a"
    }
}
```


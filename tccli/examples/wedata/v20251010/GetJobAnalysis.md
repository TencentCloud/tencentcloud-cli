**Example 1: 获取任务数据洞察信息**



Input: 

```
tccli wedata GetJobAnalysis --cli-unfold-argument  \
    --WorkspaceId 17663856806379896 \
    --JobId 6820260113153427078 \
    --SubJobId sub_6820260113153427078
```

Output: 
```
{
    "Response": {
        "Data": {
            "Suggestion": "建议优化SQL查询，减少全表扫描，可添加分区过滤条件以提升查询性能",
            "ExecuteTaskStage": {
                "CPUTime": 120000,
                "ScanBytes": 1073741824,
                "ScanRows": 10000000,
                "ShuffleBytes": 536870912,
                "ShuffleRows": 5000000,
                "OutputRows": 1000,
                "OutputBytes": 102400,
                "OutputFilesNum": 10,
                "OutputSmallFilesNum": 2
            },
            "CompleteTaskStage": {
                "WaitExecTime": 5000,
                "EngineExecTime": 60000,
                "GetResultTime": 3000
            }
        },
        "RequestId": "5a678494-1b3c-43d1-b897-8748beb25f6d"
    }
}
```


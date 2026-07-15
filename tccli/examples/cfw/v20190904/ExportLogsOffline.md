**Example 1: 日志分析日志离线导出**

日志分析日志离线导出

Input: 

```
tccli cfw ExportLogsOffline --cli-unfold-argument  \
    --Index cfw_netflow_border \
    --TaskType LogAnalysis \
    --Query protocol:HTTP \
    --StartTime 2023-01-01 00:00:00 \
    --EndTime 2023-01-01 23:59:59 \
    --TaskName 导出日志 \
    --DataFormat .json \
    --CompressionFormat .zip \
    --Order desc \
    --Length 100
```

Output: 
```
{
    "Response": {
        "ReturnCode": 0,
        "ReturnMsg": "success",
        "RequestId": "b12dee5f-bca2-49bc-88c1-a838c7b93089"
    }
}
```


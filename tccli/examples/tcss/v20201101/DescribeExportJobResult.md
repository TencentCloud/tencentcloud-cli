**Example 1: 查询导出任务的结果**



Input: 

```
tccli tcss DescribeExportJobResult --cli-unfold-argument  \
    --JobId xxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxxx",
        "ExportStatus": "RUNNING",
        "ExportProgress": 90,
        "DownloadURL": "",
        "FailureMsg": ""
    }
}
```


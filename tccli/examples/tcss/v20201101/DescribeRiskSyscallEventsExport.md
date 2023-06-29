**Example 1: 查询运行时异常进程事件列表信息导出**



Input: 

```
tccli tcss DescribeRiskSyscallEventsExport --cli-unfold-argument  \
    --ExportField xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "DownloadUrl": "xx",
        "JobId": "xx"
    }
}
```


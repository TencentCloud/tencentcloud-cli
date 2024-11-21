**Example 1: 查询运行时异常进程事件列表信息导出**



Input: 

```
tccli tcss DescribeRiskSyscallEventsExport --cli-unfold-argument  \
    --ExportField filed_name
```

Output: 
```
{
    "Response": {
        "RequestId": "8bc803fd-d85d-47b8-9e2b-9644674be677",
        "DownloadUrl": "",
        "JobId": "10001"
    }
}
```


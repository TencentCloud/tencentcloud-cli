**Example 1: 查询运行时反弹shell事件列表信息导出**



Input: 

```
tccli tcss DescribeReverseShellEventsExport --cli-unfold-argument  \
    --ExportField xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "DownloadUrl": "xx",
        "JobId": "xxx"
    }
}
```


**Example 1: 查询运行时访问控制事件列表导出**

查询运行时访问控制事件列表导出

Input: 

```
tccli tcss DescribeAccessControlEventsExport --cli-unfold-argument  \
    --ExportField xxx
```

Output: 
```
{
    "Response": {
        "DownloadUrl": "abc",
        "JobId": "abc",
        "RequestId": "abc"
    }
}
```


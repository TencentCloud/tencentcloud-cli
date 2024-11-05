**Example 1: 查询运行时访问控制事件列表导出**

查询运行时访问控制事件列表导出

Input: 

```
tccli tcss DescribeAccessControlEventsExport --cli-unfold-argument  \
    --ExportField filed_name
```

Output: 
```
{
    "Response": {
        "DownloadUrl": "https://cwp-1258344***.cos.ap-guangzhou.myqcloud.com/file.txt",
        "JobId": "10001",
        "RequestId": "8bc803fd-d85d-47b8-9e2b-9644674be677"
    }
}
```


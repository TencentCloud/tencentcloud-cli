**Example 1: 导出任务结果下载URL**



Input: 

```
tccli csip DescribeExportJobDownloadURL --cli-unfold-argument  \
    --JobID cc518a49-273a-4076-80c8-f5f5e5bfea95
```

Output: 
```
{
    "Response": {
        "DownloadURL": "test",
        "ExportStatus": "SUCCESS",
        "RequestId": "749d7e7d-8232-4d7a-be99-bc4c3a520fab"
    }
}
```


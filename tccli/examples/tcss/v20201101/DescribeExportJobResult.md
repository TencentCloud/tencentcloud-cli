**Example 1: 查询导出任务的结果**

查询导出任务的结果

Input: 

```
tccli tcss DescribeExportJobResult --cli-unfold-argument  \
    --JobId e4409223-8e92-45db-a857-11b1ff547c79
```

Output: 
```
{
    "Response": {
        "DownloadURL": "https://yunjing.cos.ap-guangzhou.myqcloud.com",
        "ExportProgress": 100,
        "ExportStatus": "SUCCESS",
        "FailureMsg": "FailureMsg",
        "RequestId": "c66b2b1f-9c85-481a-8eea-1a254ffd61df"
    }
}
```


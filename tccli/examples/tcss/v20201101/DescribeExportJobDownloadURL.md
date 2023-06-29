**Example 1: 查询导出任务下载URL**



Input: 

```
tccli tcss DescribeExportJobDownloadURL --cli-unfold-argument  \
    --JobID xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "522d7714-ef53-4940-b0ed-46d59a3cf0fd",
        "DownloadURL": "xxx"
    }
}
```


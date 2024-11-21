**Example 1: 查询导出任务下载URL**



Input: 

```
tccli tcss DescribeExportJobDownloadURL --cli-unfold-argument  \
    --JobID 15cf63db-11a9-4885-b1a3-211dd54b83b7
```

Output: 
```
{
    "Response": {
        "RequestId": "522d7714-ef53-4940-b0ed-46d59a3cf0fd",
        "DownloadURL": "http://1.2.3.4/result.csv"
    }
}
```


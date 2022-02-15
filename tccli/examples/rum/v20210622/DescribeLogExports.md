**Example 1: 获取日志下载任务列表**



Input: 

```
tccli rum DescribeLogExports --cli-unfold-argument  \
    --ID 1
```

Output: 
```
{
    "Response": {
        "LogExportSet": [
            {
                "CosPath": "https://export-gz.xxx.xxx.com",
                "Count": 1,
                "CreateTime": "2022-01-21 17:05:57",
                "EndTime": "2022-01-21 00:00:00",
                "ExportID": "export-1",
                "FileName": "log_tar.gz",
                "FileSize": 862,
                "Format": "json",
                "Order": "desc",
                "Query": "*",
                "StartTime": "2022-01-20 00:00:00",
                "Status": "Completed"
            }
        ],
        "RequestId": "a4c0bd54-d2d5-4045-a831-38a6f1fd294d"
    }
}
```


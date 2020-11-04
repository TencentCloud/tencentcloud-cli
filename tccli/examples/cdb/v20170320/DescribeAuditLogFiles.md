**Example 1: 查询审计日志文件**



Input: 

```
tccli cdb DescribeAuditLogFiles --cli-unfold-argument  \
    --InstanceId cdb-qwerasdf
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "TotalCount": 1,
        "Items": [
            {
                "FileName": "test.txt",
                "Status": "running",
                "CreateTime": "2019-03-20 17:09:13",
                "FileSize": 3,
                "DownloadUrl": "http://xxxxxx"
            }
        ]
    }
}
```


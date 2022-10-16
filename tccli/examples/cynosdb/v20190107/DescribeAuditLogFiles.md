**Example 1: 创建审计日志文件**



Input: 

```
tccli cynosdb DescribeAuditLogFiles --cli-unfold-argument  \
    --InstanceId cynosdbmysql-ins-qwerasdf
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "TotalCount": 1,
        "Items": [
            {
                "Status": "creating",
                "FileName": "audit_log_file",
                "DownloadUrl": "xx",
                "FileSize": 123,
                "CreateTime": "2019-03-20 17:09:13",
                "ErrMsg": ""
            }
        ]
    }
}
```


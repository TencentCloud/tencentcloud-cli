**Example 1: 查询日志下载任务**



Input: 

```
tccli sqlserver DescribeExportTasks --cli-unfold-argument  \
    --LogType auditLog \
    --Limit 10 \
    --Offset 0 \
    --InstanceId mssql-8lv5ti3v
```

Output: 
```
{
    "Response": {
        "Items": [],
        "TotalCount": 0,
        "RequestId": "5191e7bc-df5f-4266-abc8-2df2f2e0c4f3"
    }
}
```


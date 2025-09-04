**Example 1: 查询资源组健康检测任务列表**

查询资源组健康检测任务列表

Input: 

```
tccli tione DescribeBillingResourceGroupHealthCheckTasks --cli-unfold-argument  \
    --ResourceGroupId ersg-9hw7jfk6 \
    --Filters.0.Name TaskStatus \
    --Filters.0.Values STOPPED \
    --Filters.0.Negative True \
    --Filters.0.Fuzzy True \
    --Offset 1 \
    --Limit 1 \
    --Order ASC \
    --OrderField CreateTime
```

Output: 
```
{
    "Response": {
        "HealthCheckTaskSet": [
            {
                "CreateTime": "2025-04-29 16:33:04",
                "Id": "jkjc-jbft2233",
                "ResourceInstanceIds": [
                    "sm-v8ml2233"
                ],
                "SubUin": "100035780233",
                "SubUinName": "jack",
                "TaskStatus": "RUNNING"
            }
        ],
        "RequestId": "1dd7baad-d7dd-4a35-8bfd-4c5f6790esbc",
        "TotalCount": 1
    }
}
```


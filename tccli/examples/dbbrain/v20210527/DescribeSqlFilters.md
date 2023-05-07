**Example 1: 查询实例SQL限流任务列表**

查询实例SQL限流任务列表

Input: 

```
tccli dbbrain DescribeSqlFilters --cli-unfold-argument  \
    --Product mysql \
    --InstanceId cdb-test \
    --Statuses RUNNING \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "Id": 1234,
                "ExpireTime": "2020-04-20T10:10:00+08:00",
                "CurrentTime": "2020-04-20T10:05:00+08:00",
                "CreateTime": "2020-04-20T10:00:00+08:00",
                "Status": "RUNNING",
                "MaxConcurrency": 10,
                "CurrentConcurrency": 5,
                "RejectedSqlCount": 1000,
                "SqlType": "SELECT",
                "OriginRule": "xxxx",
                "OriginKeys": "k1,k2"
            }
        ],
        "RequestId": "b49053b9-f21c-40ec-a1ce-d1a5fae5193f",
        "TotalCount": 339
    }
}
```


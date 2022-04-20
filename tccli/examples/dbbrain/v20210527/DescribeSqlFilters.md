**Example 1: DescribeSqlFilters**



Input: 

```
tccli dbbrain DescribeSqlFilters --cli-unfold-argument  \
    --InstanceId cdb-test
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


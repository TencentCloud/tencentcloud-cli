**Example 1: Querying time range available for rolling back db1 in the instance mssql-j8kv137v**



Input: 

```
tccli sqlserver DescribeRollbackTime --cli-unfold-argument  \
    --InstanceId mssql-j8kv137v\
    --DBs db1
```

Output: 
```
{
    "Response": {
        "RequestId": "780339f6-30d7-419a-a30c-c2dc0933af1c",
        "Details": [
            {
                "DBName": "db1",
                "StartTime": "2018-08-07 11:09:03",
                "EndTime": "2018-08-09 11:09:03"
            }
        ]
    }
}
```


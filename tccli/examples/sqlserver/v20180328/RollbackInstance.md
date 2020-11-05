**Example 1: Rolling back the "db1" database in the "mssql-j8kv137v" instance to 11:32:29, August 7, 2018**



Input: 

```
tccli sqlserver RollbackInstance --cli-unfold-argument  \
    --InstanceId mssql-j8kv137v\
    --Type 0\
    --Time 2018-08-0711:32:29\
    --DBs db1
```

Output: 
```
{
    "Response": {
        "RequestId": "780339f6-30d7-419a-a30c-c2dc0933af1c",
        "FlowId": 1234
    }
}
```


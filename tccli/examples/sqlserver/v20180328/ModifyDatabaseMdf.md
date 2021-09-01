**Example 1: 收缩数据库mdf**



Input: 

```
tccli sqlserver ModifyDatabaseMdf --cli-unfold-argument  \
    --InstanceId mssql-j8kv137v \
    --DBNames test_db
```

Output: 
```
{
    "Response": {
        "FlowId": 9999,
        "RequestId": "a989d733-1099-4f44-84ad-991da182d0w3"
    }
}
```


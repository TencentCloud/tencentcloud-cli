**Example 1: 启用、禁用数据库数据变更跟踪CT**



Input: 

```
tccli sqlserver ModifyDatabaseCT --cli-unfold-argument  \
    --InstanceId mssql-j8kv137v \
    --DBNames test_db \
    --ModifyType enable
```

Output: 
```
{
    "Response": {
        "FlowId": 9999,
        "RequestId": "a928d733-1099-4f44-84ad-991da182d0s3"
    }
}
```


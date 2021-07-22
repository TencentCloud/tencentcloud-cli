**Example 1: 开启、关闭数据库数据变更捕获CDC**



Input: 

```
tccli sqlserver ModifyDatabaseCDC --cli-unfold-argument  \
    --InstanceId mssql-j8kv137v \
    --DBNames test_db \
    --ModifyType enable
```

Output: 
```
{
    "Response": {
        "FlowId": 9999,
        "RequestId": "a928d733-109a-4f44-84ad-991da182d0s3"
    }
}
```


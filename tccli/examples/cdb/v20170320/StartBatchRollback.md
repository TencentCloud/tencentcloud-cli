**Example 1: 回档数据库表**



Input: 

```
tccli cdb StartBatchRollback --cli-unfold-argument  \
    --Instances.0.InstanceId cdb-xxxxxxxx \
    --Instances.0.Strategy full \
    --Instances.0.RollbackTime '2018-08-01 16:27:43' \
    --Instances.0.Databases.0.DatabaseName old_db \
    --Instances.0.Databases.0.NewDatabaseName new_db
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "AsyncRequestId": "a6040589-3b098df5-b551d9e5-81c6bfdc"
    }
}
```


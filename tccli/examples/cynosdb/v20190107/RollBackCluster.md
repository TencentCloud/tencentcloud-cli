**Example 1: 集群回档**

集群回档

Input: 

```
tccli cynosdb RollBackCluster --cli-unfold-argument  \
    --RollbackId 1 \
    --ClusterId cynosdbmysql-xxxxxxxx \
    --ExpectTimeThresh 1 \
    --RollbackStrategy snapRollback \
    --RollbackTables.0.Tables.0.OldTable old_table \
    --RollbackTables.0.Tables.0.NewTable new_table \
    --RollbackTables.0.Database old_db1 \
    --ExpectTime 2022-01-20 00:00:00 \
    --RollbackDatabases.0.NewDatabase new_db2 \
    --RollbackDatabases.0.OldDatabase old_db2
```

Output: 
```
{
    "Response": {
        "RequestId": "128046",
        "FlowId": "123"
    }
}
```


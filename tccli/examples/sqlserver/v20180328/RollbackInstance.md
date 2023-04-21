**Example 1: 按照时间点回档数据库**

本接口（RollbackInstance）用于按照时间点回档数据库

Input: 

```
tccli sqlserver RollbackInstance --cli-unfold-argument  \
    --InstanceId mssql-aj89iq78 \
    --Type 1 \
    --DBs abc \
    --Time 2020-09-22 00:00:00 \
    --TargetInstanceId mssql-aj89iq79 \
    --RenameRestore.0.OldName abc \
    --RenameRestore.0.NewName abc
```

Output: 
```
{
    "Response": {
        "FlowId": 100023,
        "RequestId": "cd7a35be-2fbf-f3a6-210a-ea9afe158817"
    }
}
```


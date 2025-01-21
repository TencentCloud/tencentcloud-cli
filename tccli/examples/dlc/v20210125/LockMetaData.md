**Example 1: 元数据加锁**



Input: 

```
tccli dlc LockMetaData --cli-unfold-argument  \
    --LockComponentList.0.DataOperationType UNSET \
    --LockComponentList.0.IsDynamicPartitionWrite True \
    --LockComponentList.0.LockLevel TABLE \
    --LockComponentList.0.Partition  \
    --LockComponentList.0.TableName dlc_table \
    --LockComponentList.0.LockType EXCLUSIVE \
    --LockComponentList.0.IsAcid True \
    --LockComponentList.0.DbName dbdlc \
    --TxnId 0 \
    --DatasourceConnectionName DataLakeCatalog
```

Output: 
```
{
    "Response": {
        "LockId": 0,
        "LockState": "ACQUIRED",
        "RequestId": "776333b3-fab2-44eb-ad5c-98ea6fb4506b"
    }
}
```


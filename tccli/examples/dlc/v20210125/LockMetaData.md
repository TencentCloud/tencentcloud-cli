**Example 1: 元数据加锁**



Input: 

```
tccli dlc LockMetaData --cli-unfold-argument  \
    --LockComponentList.0.DataOperationType xx \
    --LockComponentList.0.IsDynamicPartitionWrite True \
    --LockComponentList.0.LockLevel xx \
    --LockComponentList.0.Partition xx \
    --LockComponentList.0.TableName xx \
    --LockComponentList.0.LockType xx \
    --LockComponentList.0.IsAcid True \
    --LockComponentList.0.DbName xx \
    --TxnId 0 \
    --DatasourceConnectionName xx
```

Output: 
```
{
    "Response": {
        "LockId": 0,
        "LockState": "xx",
        "RequestId": "xx"
    }
}
```


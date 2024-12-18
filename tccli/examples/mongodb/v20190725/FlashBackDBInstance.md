**Example 1: 执行按key回档**



Input: 

```
tccli mongodb FlashBackDBInstance --cli-unfold-argument  \
    --InstanceId cmgo-igjysqkr \
    --TargetFlashbackTime 2023-08-04 14:00:00 \
    --TargetDatabases.0.DBName my_test \
    --TargetDatabases.0.Collections.0.CollectionName my_test1 \
    --TargetDatabases.0.Collections.0.KeyValues.0.Key name \
    --TargetDatabases.0.Collections.0.KeyValues.0.Value name-demo \
    --TargetDatabases.0.Collections.0.TargetResultCollectionName my_test_bak0804143230 \
    --TargetDatabases.0.Collections.0.FilterKey name \
    --TargetInstanceId cmgo-0517****
```

Output: 
```
{
    "Response": {
        "FlowId": 1234567,
        "RequestId": "59b477da-6473-4ea8-85b3-7f4473744****"
    }
}
```


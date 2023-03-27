**Example 1: 迁移cdb**

迁移cdb

Input: 

```
tccli cynosdb TransferFromCDB --cli-unfold-argument  \
    --InstanceId cdb-xx
```

Output: 
```
{
    "Response": {
        "MigrateDBTaskId": 123,
        "RequestId": "abc"
    }
}
```


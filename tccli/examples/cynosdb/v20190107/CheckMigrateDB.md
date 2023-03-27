**Example 1: 允许一键迁移**

允许一键迁移

Input: 

```
tccli cynosdb CheckMigrateDB --cli-unfold-argument  \
    --InstanceId cdb-xx
```

Output: 
```
{
    "Response": {
        "IrreparableForbiddenReasons": [],
        "IsAllowMigration": "yes",
        "RepairableForbiddenReasons": [],
        "RequestId": "63e31387f0332"
    }
}
```


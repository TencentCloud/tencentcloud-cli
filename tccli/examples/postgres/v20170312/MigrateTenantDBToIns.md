**Example 1: 迁移多租户到独立实例**



Input: 

```
tccli postgres MigrateTenantDBToIns --cli-unfold-argument  \
    --DatabaseName pgdb-nf****** \
    --Storage 20 \
    --DBMajorVersion 17 \
    --SpecCode pg.it.small2 \
    --InstanceCategory cloudbase \
    --CallerSource cloudbase \
    --CallerToken ****/*********b**************6AA************ \
    --RestConfig.0.Name jwt-secret \
    --RestConfig.0.ExpectedValue ***fjald****a***f************fjalds**** \
    --SwitchTag 1 \
    --SwitchStartTime 21:00:00 \
    --SwitchEndTime 23:00:00
```

Output: 
```
{
    "Response": {
        "DBInstanceId": "postgres-8jbcswht",
        "TaskId": 3254,
        "RequestId": "2ba9a352-89fe-419b-8655-ce1daa144969"
    }
}
```


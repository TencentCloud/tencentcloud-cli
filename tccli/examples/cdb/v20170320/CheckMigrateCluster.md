**Example 1: 高可用实例一键迁移到云盘版校验**



Input: 

```
tccli cdb CheckMigrateCluster --cli-unfold-argument  \
    --InstanceId cdb-f35wr6wj
```

Output: 
```
{
    "Response": {
        "CheckResult": "pass",
        "Items": [
            {
                "Name": "SubVersion",
                "Status": "pass"
            }
        ],
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
```


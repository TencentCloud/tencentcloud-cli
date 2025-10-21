**Example 1: 查询迁移实例列表**

查询迁移实例列表

Input: 

```
tccli dts DescribeMigrateDBInstances --cli-unfold-argument  \
    --InstanceId cdb-eur39922 \
    --DatabaseType mysql \
    --MigrateRole src
```

Output: 
```
{
    "Response": {
        "Instances": [
            {
                "Hint": "ok",
                "InstanceId": "cdb-chtaoop0",
                "InstanceName": "evan-test2",
                "Usable": 1,
                "Vip": "172.21.0.31",
                "Vport": 10086
            },
            {
                "Hint": "ok",
                "InstanceId": "cdb-o3dplch0",
                "InstanceName": "evan-test1",
                "Usable": 1,
                "Vip": "172.21.0.37",
                "Vport": 10086
            },
            {
                "Hint": "ok",
                "InstanceId": "cdb-hbfybwlq",
                "InstanceName": "joyce-dts2",
                "Usable": 1,
                "Vip": "172.21.0.104",
                "Vport": 3306
            },
            {
                "Hint": "ok",
                "InstanceId": "cdb-kgmdn6iq",
                "InstanceName": "joyce-dts1",
                "Usable": 1,
                "Vip": "172.21.0.100",
                "Vport": 3306
            }
        ],
        "RequestId": "a4a8f147-1898-4130-a1cf-f4bd3c92d083",
        "TotalCount": 4
    }
}
```


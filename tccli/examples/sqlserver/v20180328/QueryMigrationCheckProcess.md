**Example 1: 查询迁移校验任务进度**



Input: 

```
tccli sqlserver QueryMigrationCheckProcess --cli-unfold-argument  \
    --MigrateId 1066
```

Output: 
```
{
    "Response": {
        "RequestId": "4be5990d-a4b5-49dc-b2b4-e713b6aa7ba3",
        "TotalStep": 8,
        "CurrentStep": 8,
        "StepDetails": [
            {
                "Name": "源库连接性检查",
                "Status": 0,
                "Msg": "检查数据传输服务器是否能连通源数据库"
            },
            {
                "Name": "目的库连接性检查",
                "Status": 0,
                "Msg": "检查数据传输服务器是否能连通目的数据库"
            },
            {
                "Name": "硬盘空间检查",
                "Status": 0,
                "Msg": "检查目的服务器硬盘空间是否足够"
            },
            {
                "Name": "字符集检查",
                "Status": 0,
                "Msg": "检查字符集是否一致"
            },
            {
                "Name": "数据库版本检查",
                "Status": 0,
                "Msg": "检查数据库版本号是否一致"
            },
            {
                "Name": "用户权限检查",
                "Status": 0,
                "Msg": "检查目的实例权限是否存在"
            },
            {
                "Name": "源库存在性检查",
                "Status": 0,
                "Msg": "检查源数据库是否存在"
            },
            {
                "Name": "目的库存在性检查",
                "Status": 0,
                "Msg": "检查目的数据库是否存在"
            }
        ]
    }
}
```


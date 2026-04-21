**Example 1: 查询实例架构信息**



Input: 

```
tccli cdb DescribeDBInstanceConfig --cli-unfold-argument  \
    --InstanceId cdbro-j99ornco
```

Output: 
```
{
    "Response": {
        "BackupConfig": {
            "ReplicationMode": "sync",
            "Vip": "",
            "Vport": 0,
            "Zone": "ap-guangzhou-4"
        },
        "DeployMode": 0,
        "ProtectMode": 2,
        "RequestId": "e6ad4a50-f251-4236-9c30-1887f330a38c",
        "SlaveConfig": {
            "ReplicationMode": "sync",
            "Zone": "ap-guangzhou-4"
        },
        "Switched": false,
        "Zone": "ap-guangzhou-4"
    }
}
```


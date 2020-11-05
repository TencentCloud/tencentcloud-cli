**Example 1: Querying the configuration information of TencentDB instance**



Input: 

```
tccli cdb DescribeDBInstanceConfig --cli-unfold-argument  \
    --InstanceId cdb-f35wr6wj
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "SlaveConfig": {
            "ReplicationMode": "async",
            "Zone": "ap-guangzhou-3"
        },
        "ProtectMode": 0,
        "Zone": "ap-guangzhou-3",
        "DeployMode": 1
    }
}
```


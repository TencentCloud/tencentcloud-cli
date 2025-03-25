**Example 1: 查询实例详情**

查询实例详情

Input: 

```
tccli dcdb DescribeDCDBInstanceDetail --cli-unfold-argument  \
    --InstanceId tdsqlshard-cgg0czdx
```

Output: 
```
{
    "Response": {
        "AutoRenewFlag": 0,
        "Cpu": 2,
        "CreateTime": "2025-03-07 10:46:30",
        "DbEngine": "MySQL",
        "DbVersion": "8.0.24",
        "DbVersionId": "8.0",
        "DcnDstNum": 0,
        "DcnFlag": 0,
        "DcnStatus": 0,
        "EncryptStatus": 0,
        "ExclusterId": "",
        "ExclusterType": 0,
        "InstanceId": "tdsqlshard-cgg0czdx",
        "InstanceName": "2.5",
        "InstanceType": 2,
        "Ipv6Flag": 0,
        "IsAuditSupported": 1,
        "IsDcnStrongSyncSupported": 0,
        "IsDcnSwitchSupported": 1,
        "IsEncryptSupported": 0,
        "IsMaxUserConnectionsSupported": true,
        "IsPhysicalReplicationSupported": false,
        "LogStorage": 16,
        "Machine": "TS85",
        "MasterZone": "ap-guangzhou-3",
        "Memory": 4,
        "NodeCount": 2,
        "PayMode": "postpaid",
        "PeriodEndTime": "0001-01-01 00:00:00",
        "Pid": 1001670,
        "ProjectId": 0,
        "Qps": 2100,
        "Region": "ap-guangzhou",
        "RequestId": "8e1df28e-3cfd-4735-991a-85356104c5c5",
        "ReservedNetResources": [],
        "ResourceTags": [],
        "RsAccessStrategy": 0,
        "Shards": [
            {
                "Cpu": 1,
                "CreateTime": "2025-03-07 10:46:30",
                "LogDisk": 8,
                "Memory": 2,
                "NodeCount": 2,
                "NodesInfo": [
                    {
                        "NodeId": "e352195dbcc7",
                        "Role": "master"
                    },
                    {
                        "NodeId": "7686cda46e3c",
                        "Role": "slave"
                    }
                ],
                "ProxyVersion": "",
                "ShardInstanceId": "shard-p6hy8o3t",
                "ShardMasterZone": "ap-guangzhou-3",
                "ShardSerialId": "set_1741315924_3",
                "ShardSlaveZones": [
                    "ap-guangzhou-3"
                ],
                "Status": 1,
                "StatusDesc": "调整配置中",
                "Storage": 10,
                "StorageUsage": 0.012
            },
            {
                "Cpu": 1,
                "CreateTime": "2025-03-07 10:46:30",
                "LogDisk": 8,
                "Memory": 2,
                "NodeCount": 2,
                "NodesInfo": [
                    {
                        "NodeId": "262cf711c6cc",
                        "Role": "master"
                    },
                    {
                        "NodeId": "7ade05da7488",
                        "Role": "slave"
                    }
                ],
                "ProxyVersion": "",
                "ShardInstanceId": "shard-502tx32l",
                "ShardMasterZone": "ap-guangzhou-3",
                "ShardSerialId": "set_1741315737_1",
                "ShardSlaveZones": [
                    "ap-guangzhou-3"
                ],
                "Status": 1,
                "StatusDesc": "调整配置中",
                "Storage": 10,
                "StorageUsage": 0.012
            }
        ],
        "SlaveZones": [
            "ap-guangzhou-3"
        ],
        "Status": 1,
        "StatusDesc": "调整配置中",
        "Storage": 20,
        "StorageUsage": 0.012,
        "SubnetId": "subnet-ms3w1jlq",
        "Vip": "10.1.1.45",
        "Vip6": "",
        "VpcId": "vpc-mgfyl2p3",
        "Vport": 3306,
        "WanDomain": "",
        "WanPort": 0,
        "WanPortIpv6": 0,
        "WanStatus": 0,
        "WanStatusIpv6": 0,
        "WanVip": "",
        "WanVipv6": ""
    }
}
```


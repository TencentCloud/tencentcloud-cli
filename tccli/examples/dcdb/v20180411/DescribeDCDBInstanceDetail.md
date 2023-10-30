**Example 1: 查询实例详细信息**

查询分布式实例 dcdbt-21dfpcv1 的详细信息

Input: 

```
tccli dcdb DescribeDCDBInstanceDetail --cli-unfold-argument  \
    --InstanceId dcdbt-21dfpcv1
```

Output: 
```
{
    "Response": {
        "AutoRenewFlag": 0,
        "Cpu": 3,
        "CreateTime": "2016-07-13 11:08:38",
        "DbEngine": "MariaDB",
        "DbVersion": "10.0.10",
        "DcnDstNum": 0,
        "DcnFlag": 0,
        "DcnStatus": 0,
        "ExclusterId": "",
        "InstanceId": "dcdbt-21dfpcv1",
        "InstanceName": "dcdbt-21dfpcv1",
        "InstanceType": 2,
        "Ipv6Flag": 0,
        "IsAuditSupported": 1,
        "IsEncryptSupported": 0,
        "LogStorage": 16,
        "Machine": "TS85",
        "MasterZone": "ap-guangzhou-1",
        "Memory": 6,
        "NodeCount": 2,
        "PayMode": "prepaid",
        "PeriodEndTime": "2023-01-01 11:12:24",
        "Pid": 1001670,
        "ProjectId": 0,
        "Qps": 4000,
        "Region": "ap-guangzhou",
        "RequestId": "e1828feb-9a21-409a-8964-309215615d84",
        "ResourceTags": [],
        "Shards": [
            {
                "Cpu": 2,
                "CreateTime": "2021-12-01 11:49:54",
                "LogDisk": 8,
                "Memory": 4,
                "NodeCount": 2,
                "NodesInfo": [
                    {
                        "NodeId": "85409b834943",
                        "Role": "master"
                    },
                    {
                        "NodeId": "9de9c0321ccd",
                        "Role": "slave"
                    }
                ],
                "ProxyVersion": "\"1.17.6-M-V2.0R723D002\"",
                "ShardInstanceId": "shard-ngbrea6b",
                "ShardMasterZone": "ap-guangzhou-1",
                "ShardSerialId": "set_1643096858_1",
                "ShardSlaveZones": [
                    "ap-guangzhou-1"
                ],
                "Status": 2,
                "StatusDesc": "运行中",
                "Storage": 10,
                "StorageUsage": 0.01
            },
            {
                "Cpu": 1,
                "CreateTime": "2021-12-01 11:49:54",
                "LogDisk": 8,
                "Memory": 2,
                "NodeCount": 2,
                "NodesInfo": [
                    {
                        "NodeId": "1e2025d21782",
                        "Role": "master"
                    },
                    {
                        "NodeId": "b228c46e9b63",
                        "Role": "slave"
                    }
                ],
                "ProxyVersion": "\"1.17.6-M-V2.0R723D002\"",
                "ShardInstanceId": "shard-5zf65smf",
                "ShardMasterZone": "ap-guangzhou-1",
                "ShardSerialId": "set_1643096949_3",
                "ShardSlaveZones": [
                    "ap-guangzhou-1"
                ],
                "Status": 2,
                "StatusDesc": "运行中",
                "Storage": 10,
                "StorageUsage": 0.011
            }
        ],
        "SlaveZones": [
            "ap-guangzhou-1"
        ],
        "Status": 2,
        "StatusDesc": "运行中",
        "Storage": 20,
        "StorageUsage": 0.0105,
        "SubnetId": "subnet-ovkcc9x6",
        "Vip": "10.1.0.5",
        "Vip6": "",
        "VpcId": "vpc-j97vcvb5",
        "Vport": 3306,
        "WanDomain": "",
        "WanPort": 0,
        "WanPortIpv6": 0,
        "WanStatus": 0,
        "WanStatusIpv6": 0,
        "WanVip": "",
        "WanVipv6": "",
        "IsMaxUserConnectionsSupported": true,
        "DbVersionId": "5.7",
        "EncryptStatus": 0,
        "ExclusterType": 0,
        "RsAccessStrategy": 0,
        "ReservedNetResources": [
            {
                "VpcId": "vpc-p6alckzx",
                "SubnetId": "subnet-3pz073lq",
                "Vip": "172.16.0.40",
                "Vports": [
                    3306
                ],
                "RecycleTime": "2023-05-19 16:12:32"
            }
        ],
        "IsPhysicalReplicationSupported": true,
        "IsDcnStrongSyncSupported": 1,
        "IsDcnSwitchSupported": 1
    }
}
```


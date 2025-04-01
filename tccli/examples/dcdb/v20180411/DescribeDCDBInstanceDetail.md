**Example 1: 获取实例详情**

本接口用于查询实例详细信息

Input: 

```
tccli dcdb DescribeDCDBInstanceDetail --cli-unfold-argument  \
    --InstanceId tdsqlshard-hn35cf0n
```

Output: 
```
{
    "Response": {
        "AutoRenewFlag": 0,
        "Cpu": 2,
        "CpuType": "Intel/AMD",
        "CreateTime": "2025-03-22 17:01:11",
        "DbEngine": "MySQL",
        "DbVersion": "8.0.30",
        "DbVersionId": "8.0",
        "DcnDstNum": 0,
        "DcnFlag": 0,
        "DcnStatus": 0,
        "EncryptStatus": 0,
        "ExclusterId": "dbdc-00wb5kz5",
        "ExclusterType": 0,
        "InstanceId": "tdsqlshard-hn35cf0n",
        "InstanceName": "QT4st6gv8.0",
        "InstanceType": 1,
        "Ipv6Flag": 0,
        "IsAuditSupported": 1,
        "IsDcnStrongSyncSupported": 0,
        "IsDcnSwitchSupported": 1,
        "IsEncryptSupported": 1,
        "IsMaxUserConnectionsSupported": true,
        "IsPhysicalReplicationSupported": false,
        "LogStorage": 16,
        "Machine": "SH12",
        "MasterZone": "ap-guangzhou-2",
        "Memory": 4,
        "NodeCount": 2,
        "PayMode": "prepaid",
        "PeriodEndTime": "2025-03-28 15:33:44",
        "Pid": 11128,
        "ProjectId": 0,
        "Qps": 2100,
        "Region": "ap-guangzhou",
        "RequestId": "37f48ae6-6e19-421c-bc3d-9e5215bce840",
        "ReservedNetResources": [],
        "ResourceTags": [],
        "RsAccessStrategy": 0,
        "Shards": [
            {
                "Cpu": 1,
                "CreateTime": "2025-03-22 17:01:12",
                "LogDisk": 8,
                "Memory": 2,
                "NodeCount": 2,
                "NodesInfo": [
                    {
                        "NodeId": "412f4810600c",
                        "Role": "master",
                        "Zone": "ap-guangzhou-2"
                    },
                    {
                        "NodeId": "a0872cc18e43",
                        "Role": "slave",
                        "Zone": "ap-guangzhou-2"
                    }
                ],
                "ProxyVersion": "",
                "ShardInstanceId": "shard-alt5mizl",
                "ShardMasterZone": "ap-guangzhou-2",
                "ShardSerialId": "set_1742635118_5",
                "ShardSlaveZones": [
                    "ap-guangzhou-2"
                ],
                "Status": 2,
                "StatusDesc": "运行中",
                "Storage": 10,
                "StorageUsage": 0.01
            },
            {
                "Cpu": 1,
                "CreateTime": "2025-03-22 17:01:12",
                "LogDisk": 8,
                "Memory": 2,
                "NodeCount": 2,
                "NodesInfo": [
                    {
                        "NodeId": "557c152b5be8",
                        "Role": "master",
                        "Zone": "ap-guangzhou-2"
                    },
                    {
                        "NodeId": "5fa1b08b00e8",
                        "Role": "slave",
                        "Zone": "ap-guangzhou-2"
                    }
                ],
                "ProxyVersion": "",
                "ShardInstanceId": "shard-l4vjg0a3",
                "ShardMasterZone": "ap-guangzhou-2",
                "ShardSerialId": "set_1742635315_7",
                "ShardSlaveZones": [
                    "ap-guangzhou-2"
                ],
                "Status": 2,
                "StatusDesc": "运行中",
                "Storage": 10,
                "StorageUsage": 0.01
            }
        ],
        "SlaveZones": [
            "ap-guangzhou-2"
        ],
        "Status": 2,
        "StatusDesc": "运行中",
        "Storage": 20,
        "StorageUsage": 0.01,
        "SubnetId": "subnet-6rq8ehaq",
        "Vip": "10.0.0.50",
        "Vip6": "",
        "VpcId": "vpc-ilhphh7v",
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


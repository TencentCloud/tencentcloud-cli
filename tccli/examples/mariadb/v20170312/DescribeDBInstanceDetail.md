**Example 1: 查询实例详细信息**



Input: 

```
tccli mariadb DescribeDBInstanceDetail --cli-unfold-argument  \
    --InstanceId tdsql-jv8z8fhl
```

Output: 
```
{
    "Response": {
        "WanStatus": 0,
        "Zone": "ap-guangzhou-2",
        "Pid": 1002231,
        "WanPortIpv6": 0,
        "Storage": 10,
        "Machine": "SH12",
        "AutoRenewFlag": 0,
        "NodesInfo": [
            {
                "Role": "xx",
                "NodeId": "xx"
            }
        ],
        "Memory": 2,
        "Status": 2,
        "Vip6": "",
        "MasterZone": "ap-guangzhou-1",
        "VpcId": "vpc-hqxhp43z",
        "IsEncryptSupported": 0,
        "InstanceId": "tdsql-jv8z8fhl",
        "WanVipv6": "",
        "SlaveZones": [
            "ap-guangzhou-2",
            "ap-guangzhou-2"
        ],
        "TdsqlVersion": "基于MariaDB 10.0.10设计(兼容MySQL 5.5)",
        "WanStatusIpv6": 0,
        "SubnetId": "subnet-15y3y4eo",
        "InstanceType": 0,
        "StorageUsage": "10.1",
        "DcnStatus": 0,
        "DbVersion": "5.7.17",
        "DcnDstNum": 0,
        "ProjectId": 0,
        "Region": "ap-guangzhou",
        "DbEngine": "Percona",
        "IsTmp": 0,
        "PayMode": "1",
        "PeriodEndTime": "2020-09-22 00:00:00",
        "ResourceTags": [
            {
                "TagKey": "k1",
                "TagValue": "v1"
            }
        ],
        "RequestId": "14f6980a-7fe1-11ea-b896-525400542aa6",
        "Ipv6Flag": 0,
        "StatusDesc": "运行中",
        "InstanceName": "cos_test",
        "Cpu": 1,
        "DcnFlag": 0,
        "IsAuditSupported": true,
        "WanDomain": "",
        "WanPort": 0,
        "CreateTime": "2020-09-22 00:00:00",
        "Vip": "192.168.240.44",
        "ExclusterId": "",
        "LogStorage": 8,
        "NodeCount": 3,
        "Qps": 2100,
        "Vport": 3306,
        "WanVip": "",
        "IsMaxUserConnectionsSupported": true,
        "DbVersionId": "5.7",
        "ReplicaConfig": {
            "DelayReplicationType": "xx",
            "ReplicationDelay": 0,
            "RoReplicationMode": "xx",
            "DueTime": "xx"
        },
        "ReplicaStatus": {
            "Status": "xx",
            "Delay": 0
        },
        "EncryptStatus": 0,
        "ExclusterType": 0
    }
}
```


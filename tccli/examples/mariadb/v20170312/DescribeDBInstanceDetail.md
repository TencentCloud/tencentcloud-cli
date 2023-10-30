**Example 1: 查询实例详细信息**

查询集中式实例的详细信息

Input: 

```
tccli mariadb DescribeDBInstanceDetail --cli-unfold-argument  \
    --InstanceId tdsql-h178kq75
```

Output: 
```
{
    "Response": {
        "AutoRenewFlag": 0,
        "Cpu": 1,
        "CreateTime": "2023-02-27 17:58:50",
        "DbEngine": "MySQL",
        "DbVersion": "8.0.24",
        "DbVersionId": "8.0",
        "DcnDstNum": 1,
        "DcnFlag": 1,
        "DcnStatus": 2,
        "EncryptStatus": 0,
        "ExclusterId": "",
        "ExclusterType": 0,
        "InstanceId": "tdsql-h178kq75",
        "InstanceName": "cdz",
        "InstanceType": 2,
        "Ipv6Flag": 0,
        "IsAuditSupported": true,
        "IsEncryptSupported": 0,
        "IsMaxUserConnectionsSupported": true,
        "IsTmp": 0,
        "LogStorage": 8,
        "Machine": "TS85",
        "MasterZone": "ap-guangzhou-3",
        "Memory": 2,
        "NodeCount": 2,
        "NodesInfo": [
            {
                "NodeId": "60af5538060f",
                "Role": "master"
            },
            {
                "NodeId": "12c58811dbfd",
                "Role": "slave"
            }
        ],
        "PayMode": "postpaid",
        "PeriodEndTime": "0001-01-01 00:00:00",
        "Pid": 1002231,
        "ProjectId": 0,
        "Qps": 2100,
        "Region": "ap-guangzhou",
        "ReplicaConfig": null,
        "ReplicaStatus": null,
        "RequestId": "40b4a902-5217-4e18-8db1-10e0ff01be62",
        "ResourceTags": [],
        "RsAccessStrategy": 0,
        "SlaveZones": [
            "ap-guangzhou-3"
        ],
        "Status": 2,
        "StatusDesc": "运行中",
        "Storage": 10,
        "StorageUsage": "0.010",
        "SubnetId": "subnet-8ve8m3xy",
        "TdsqlVersion": "基于MySQL 8.0.24设计(兼容Mysql 8.0)",
        "Vip": "10.1.0.13",
        "Vip6": "",
        "VpcId": "vpc-0rjtvrlz",
        "Vport": 3306,
        "WanDomain": "",
        "WanPort": 0,
        "WanPortIpv6": 0,
        "WanStatus": 0,
        "WanStatusIpv6": 0,
        "WanVip": "",
        "WanVipv6": "",
        "Zone": "ap-guangzhou-3",
        "ReservedNetResources": [
            {
                "VpcId": "vpc-5rske1or",
                "SubnetId": "subnet-0z3os0xe",
                "Vip": "10.1.0.6",
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


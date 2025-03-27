**Example 1: 获取实例详情**

获取实例详情

Input: 

```
tccli mariadb DescribeDBInstanceDetail --cli-unfold-argument  \
    --InstanceId tdsql-pkahzscp
```

Output: 
```
{
    "Response": {
        "AutoRenewFlag": 0,
        "Cpu": 1,
        "CreateTime": "2025-03-24 21:10:39",
        "DbEngine": "MySQL",
        "DbVersion": "8.0.30",
        "DbVersionId": "8.0",
        "DcnDstNum": 0,
        "DcnFlag": 0,
        "DcnStatus": 0,
        "EncryptStatus": 0,
        "ExclusterId": "",
        "ExclusterType": 0,
        "InstanceId": "tdsql-pkahzscp",
        "InstanceName": "tdsql-pkahzscp",
        "InstanceType": 2,
        "Ipv6Flag": 0,
        "IsAuditSupported": true,
        "IsDcnStrongSyncSupported": 0,
        "IsDcnSwitchSupported": 1,
        "IsEncryptSupported": 1,
        "IsMaxUserConnectionsSupported": true,
        "IsPhysicalReplicationSupported": false,
        "IsTmp": 0,
        "LogStorage": 8,
        "Machine": "TS85",
        "MasterZone": "ap-guangzhou-3",
        "Memory": 2,
        "NodeCount": 2,
        "NodesInfo": [
            {
                "NodeId": "289d9348f2b7",
                "Role": "master"
            },
            {
                "NodeId": "fae3b3bdf61b",
                "Role": "slave"
            }
        ],
        "PayMode": "prepaid",
        "PeriodEndTime": "2025-04-24 21:10:39",
        "Pid": 1002231,
        "ProjectId": 0,
        "ProxyVersion": "proxy-22.3.11",
        "Qps": 2100,
        "Region": "ap-guangzhou",
        "ReplicaConfig": null,
        "ReplicaStatus": null,
        "RequestId": "1e82daa5-5111-4f1c-9cc6-9b4e1609f3f2",
        "ReservedNetResources": [],
        "ResourceTags": [],
        "RsAccessStrategy": 0,
        "SlaveZones": [
            "ap-guangzhou-3"
        ],
        "Status": 3,
        "StatusDesc": "未初始化",
        "Storage": 10,
        "StorageUsage": "0.010",
        "SubnetId": "subnet-25p24z86",
        "TdsqlVersion": "基于MySQL 8.0.30设计(兼容Mysql 8.0)",
        "Vip": "10.0.0.2",
        "Vip6": "",
        "VpcId": "vpc-fqie18p3",
        "Vport": 3306,
        "WanDomain": "",
        "WanPort": 0,
        "WanPortIpv6": 0,
        "WanStatus": 0,
        "WanStatusIpv6": 0,
        "WanVip": "",
        "WanVipv6": "",
        "Zone": "ap-guangzhou-3"
    }
}
```


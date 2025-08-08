**Example 1: 获取实例详情**

改接口用于获取实例的详细信息

Input: 

```
tccli mariadb DescribeDBInstanceDetail --cli-unfold-argument  \
    --InstanceId tdsql-3ensoqb3
```

Output: 
```
{
    "Response": {
        "AutoRenewFlag": 0,
        "Cpu": 1,
        "CpuType": "Intel/AMD",
        "CreateTime": "2025-03-22 17:01:06",
        "DbEngine": "MySQL",
        "DbVersion": "8.0.30",
        "DbVersionId": "8.0",
        "DcnDstNum": 0,
        "DcnFlag": 0,
        "DcnStatus": 0,
        "EncryptStatus": 0,
        "ExclusterId": "dbdc-00wb5kz5",
        "ExclusterType": 0,
        "InstanceId": "tdsql-3ensoqb3",
        "InstanceName": "QT4sth9v8.0",
        "InstanceType": 1,
        "Ipv6Flag": 0,
        "IsAuditSupported": true,
        "IsDcnStrongSyncSupported": 0,
        "IsDcnSwitchSupported": 1,
        "IsEncryptSupported": 1,
        "IsMaxUserConnectionsSupported": true,
        "IsPhysicalReplicationSupported": false,
        "IsTmp": 0,
        "LogStorage": 8,
        "Machine": "",
        "MasterZone": "ap-guangzhou-2",
        "Memory": 2,
        "NodeCount": 2,
        "NodesInfo": [
            {
                "NodeId": "064eeaff8314",
                "Role": "master",
                "Zone": "ap-guangzhou-2"
            },
            {
                "NodeId": "2981e04659a2",
                "Role": "slave",
                "Zone": "ap-guangzhou-2"
            }
        ],
        "PayMode": "prepaid",
        "PeriodEndTime": "2025-03-28 15:33:44",
        "Pid": 10890,
        "ProjectId": 0,
        "ProxyVersion": "proxy-22.3.5",
        "Qps": 2100,
        "Region": "ap-guangzhou",
        "ReplicaConfig": null,
        "ReplicaStatus": null,
        "RequestId": "e86f7f08-d005-4f04-b917-7c9709299ff7",
        "ReservedNetResources": [],
        "ResourceTags": [],
        "RsAccessStrategy": 0,
        "SlaveZones": [
            "ap-guangzhou-2"
        ],
        "Status": 2,
        "StatusDesc": "运行中",
        "Storage": 10,
        "StorageUsage": "0.010",
        "SubnetId": "subnet-6rq8ehaq",
        "TdsqlVersion": "基于MySQL 8.0.30设计(兼容Mysql 8.0)",
        "Vip": "10.0.0.56",
        "Vip6": "",
        "VpcId": "vpc-ilhphh7v",
        "Vport": 3306,
        "WanDomain": "",
        "WanPort": 0,
        "WanPortIpv6": 0,
        "WanStatus": 0,
        "WanStatusIpv6": 0,
        "WanVip": "",
        "WanVipv6": "",
        "Zone": "ap-guangzhou-2",
        "ProtectedProperty": 1
    }
}
```


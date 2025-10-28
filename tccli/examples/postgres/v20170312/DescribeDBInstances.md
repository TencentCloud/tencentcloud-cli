**Example 1: 查询所有实例列表**

按指定分页查询实例列表

Input: 

```
tccli postgres DescribeDBInstances --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "DBInstanceSet": [
            {
                "AppId": 2512400000,
                "AutoRenew": 0,
                "CreateTime": "2024-09-01 16:00:45",
                "DBCharset": "UTF8",
                "DBEngine": "postgresql",
                "DBEngineConfig": "",
                "DBInstanceClass": "pg.it.small2",
                "DBInstanceCpu": 1,
                "DBInstanceId": "postgres-dnlizio3",
                "DBInstanceMemory": 2,
                "DBInstanceName": "Unnamed",
                "DBInstanceNetInfo": [
                    {
                        "Address": "",
                        "Ip": "10.*.*.*",
                        "NetType": "private",
                        "Port": 5432,
                        "ProtocolType": "postgresql",
                        "Status": "opened",
                        "SubnetId": "subnet-b23o6b22",
                        "VpcId": "vpc-49ab5lb9"
                    },
                    {
                        "Address": "",
                        "Ip": "",
                        "NetType": "public",
                        "Port": 0,
                        "ProtocolType": "",
                        "Status": "initing",
                        "SubnetId": "",
                        "VpcId": ""
                    }
                ],
                "DBInstanceStatus": "running",
                "DBInstanceStorage": 100,
                "DBInstanceType": "primary",
                "DBInstanceVersion": "standard",
                "DBKernelVersion": "v16.2_r1.5",
                "DBMajorVersion": "16",
                "DBNodeSet": [
                    {
                        "DedicatedClusterId": "",
                        "Role": "Primary",
                        "Zone": "ap-guangzhou-7"
                    },
                    {
                        "DedicatedClusterId": "",
                        "Role": "Standby",
                        "Zone": "ap-guangzhou-7"
                    }
                ],
                "DBVersion": "16.2",
                "ExpireTime": "0000-00-00 00:00:00",
                "IsSupportTDE": 0,
                "IsolatedTime": "0000-00-00 00:00:00",
                "MasterDBInstanceId": "",
                "NetworkAccessList": null,
                "OfflineTime": "0001-01-04 00:00:00",
                "PayType": "postpaid",
                "ProjectId": 0,
                "ReadOnlyInstanceNum": 0,
                "Region": "ap-guangzhou",
                "StatusInReadonlyGroup": "",
                "SubnetId": "subnet-b23o6b22",
                "SupportIpv6": 0,
                "TagList": [],
                "Type": "",
                "Uid": 421842,
                "UpdateTime": "2024-09-29 10:10:57",
                "VpcId": "vpc-49ab5lb9",
                "Zone": "ap-guangzhou-7"
            }
        ],
        "RequestId": "9e87cd50-5daf-44bf-8f67-3d3f017a87e7",
        "TotalCount": 1
    }
}
```

**Example 2: 根据实例ID查询实例信息**

例如：查询实例ID为postgres-xxxxx的实例信息

Input: 

```
tccli postgres DescribeDBInstances --cli-unfold-argument  \
    --Limit 10 \
    --Filters.0.Values postgres-dnlizio3 \
    --Filters.0.Name db-instance-id \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "DBInstanceSet": [
            {
                "AppId": 2512400000,
                "AutoRenew": 0,
                "CreateTime": "2024-09-01 16:00:45",
                "DBCharset": "UTF8",
                "DBEngine": "postgresql",
                "DBEngineConfig": "",
                "DBInstanceClass": "pg.it.small2",
                "DBInstanceCpu": 1,
                "DBInstanceId": "postgres-dnlizio3",
                "DBInstanceMemory": 2,
                "DBInstanceName": "Unnamed",
                "DBInstanceNetInfo": [
                    {
                        "Address": "",
                        "Ip": "10.*.*.*",
                        "NetType": "private",
                        "Port": 5432,
                        "ProtocolType": "postgresql",
                        "Status": "opened",
                        "SubnetId": "subnet-b23o6b22",
                        "VpcId": "vpc-49ab5lb9"
                    },
                    {
                        "Address": "",
                        "Ip": "",
                        "NetType": "public",
                        "Port": 0,
                        "ProtocolType": "",
                        "Status": "initing",
                        "SubnetId": "",
                        "VpcId": ""
                    }
                ],
                "DBInstanceStatus": "running",
                "DBInstanceStorage": 100,
                "DBInstanceType": "primary",
                "DBInstanceVersion": "standard",
                "DBKernelVersion": "v16.2_r1.5",
                "DBMajorVersion": "16",
                "DBNodeSet": [
                    {
                        "DedicatedClusterId": "",
                        "Role": "Primary",
                        "Zone": "ap-guangzhou-7"
                    },
                    {
                        "DedicatedClusterId": "",
                        "Role": "Standby",
                        "Zone": "ap-guangzhou-7"
                    }
                ],
                "DBVersion": "16.2",
                "ExpireTime": "0000-00-00 00:00:00",
                "IsSupportTDE": 0,
                "IsolatedTime": "0000-00-00 00:00:00",
                "MasterDBInstanceId": "",
                "NetworkAccessList": null,
                "OfflineTime": "0001-01-04 00:00:00",
                "PayType": "postpaid",
                "ProjectId": 0,
                "ReadOnlyInstanceNum": 0,
                "Region": "ap-guangzhou",
                "StatusInReadonlyGroup": "",
                "SubnetId": "subnet-b23o6b22",
                "SupportIpv6": 0,
                "TagList": [],
                "Type": "",
                "Uid": 421842,
                "UpdateTime": "2024-09-29 10:10:57",
                "VpcId": "vpc-49ab5lb9",
                "Zone": "ap-guangzhou-7"
            }
        ],
        "RequestId": "9e87cd50-5daf-44bf-8f67-3d3f017a87e7",
        "TotalCount": 1
    }
}
```


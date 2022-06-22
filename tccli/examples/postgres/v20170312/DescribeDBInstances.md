**Example 1: 查询所有实例列表**



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
        "TotalCount": 1,
        "DBInstanceSet": [
            {
                "Zone": "ap-guangzhou-2",
                "DBInstanceName": "xxx",
                "DBNodeSet": [
                    {
                        "Role": "Primary",
                        "Zone": "ap-guangzhou-2"
                    }
                ],
                "Type": 1,
                "IsSupportTDE": 0,
                "DBMajorVersion": "10",
                "ReadOnlyInstanceNum": 1,
                "MasterDBInstanceId": "",
                "UpdateTime": "2020-09-22 00:00:00",
                "VpcId": "vpc-xxxxxxxx",
                "IsolatedTime": "2020-09-22 00:00:00",
                "DBVersion": "10",
                "DBKernelVersion": "v10.4_r1.0",
                "DBInstanceVersion": "standard",
                "AutoRenew": 1,
                "StatusInReadonlyGroup": "running",
                "SubnetId": "subnet-xxxxxxxx",
                "DBInstanceMemory": 1,
                "DBInstanceType": "primary",
                "DBInstanceStatus": "running",
                "OfflineTime": "2019-12-28 19:23:19",
                "Region": "ap-guangzhou",
                "ProjectId": 1,
                "DBInstanceNetInfo": [
                    {
                        "Address": "",
                        "Ip": "10.10.10.220",
                        "Port": 5432,
                        "Status": "opened",
                        "NetType": "private",
                        "VpcId": "vpc-xxxxxxxx",
                        "SubnetId": "subnet-xxxxxxxx"
                    },
                    {
                        "Address": "",
                        "Ip": "",
                        "Port": 0,
                        "Status": "",
                        "NetType": "public",
                        "VpcId": "",
                        "SubnetId": ""
                    }
                ],
                "DBInstanceStorage": 1,
                "Uid": 1,
                "DBCharset": "UTF8",
                "DBInstanceId": "postgres-xxxxxxxx",
                "PayType": "prepaid",
                "ExpireTime": "2020-09-22 00:00:00",
                "SupportIpv6": 1,
                "AppId": 1,
                "DBInstanceClass": "cdb.pg.z1.4g",
                "CreateTime": "2020-09-22 00:00:00",
                "DBInstanceCpu": 1,
                "TagList": [
                    {
                        "TagKey": "tag1",
                        "TagValue": "v1"
                    }
                ],
                "NetworkAccessList": []
            }
        ],
        "RequestId": "d849664a-191c-48bf-b42f-444caa189557"
    }
}
```

**Example 2: 根据实例ID查询实例信息**

例如：查询实例ID为postgres-xxxxxxxx的实例信息

Input: 

```
tccli postgres DescribeDBInstances --cli-unfold-argument  \
    --Limit 10 \
    --Filters.0.Values postgres-xxxxxxxx \
    --Filters.0.Name db-instance-id \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "d849664a-191c-48bf-b42f-444caa189557",
        "TotalCount": 1,
        "DBInstanceSet": [
            {
                "Region": "ap-guangzhou",
                "Zone": "ap-guangzhou-2",
                "AppId": 100000000,
                "Uid": 1000001,
                "ProjectId": 0,
                "VpcId": "vpc-xxxxxxxx",
                "SubnetId": "subnet-xxxxxxxx",
                "Type": 1,
                "DBNodeSet": [
                    {
                        "Role": "Primary",
                        "Zone": "ap-guangzhou-2"
                    }
                ],
                "DBInstanceId": "postgres-xxxxxxxx",
                "MasterDBInstanceId": "",
                "DBInstanceName": "test",
                "DBInstanceStatus": "running",
                "DBInstanceMemory": 4,
                "DBInstanceStorage": 20,
                "DBInstanceCpu": 2,
                "DBInstanceClass": "cdb.pg.z1.4g",
                "DBInstanceType": "primary",
                "DBInstanceVersion": "standard",
                "DBInstanceNetInfo": [
                    {
                        "Address": "",
                        "Ip": "10.10.10.220",
                        "Port": 5432,
                        "Status": "opened",
                        "NetType": "private",
                        "VpcId": "vpc-xxxxxxxx",
                        "SubnetId": "subnet-xxxxxxxx"
                    },
                    {
                        "Address": "",
                        "Ip": "",
                        "Port": 0,
                        "Status": "",
                        "NetType": "public",
                        "VpcId": "",
                        "SubnetId": ""
                    }
                ],
                "DBCharset": "UTF8",
                "DBVersion": "10",
                "IsSupportTDE": 0,
                "DBMajorVersion": "10",
                "DBKernelVersion": "v10.4_r1.0",
                "CreateTime": "2017-12-28 19:23:19",
                "UpdateTime": "2018-01-18 15:54:32",
                "ExpireTime": "2018-01-28 19:23:23",
                "IsolatedTime": "0000-00-00 00:00:00",
                "OfflineTime": "2019-12-28 19:23:19",
                "StatusInReadonlyGroup": "running",
                "ReadOnlyInstanceNum": 1,
                "PayType": "prepaid",
                "AutoRenew": 1,
                "SupportIpv6": 0,
                "TagList": [
                    {
                        "TagKey": "tag1",
                        "TagValue": "v1"
                    }
                ],
                "NetworkAccessList": []
            }
        ]
    }
}
```

